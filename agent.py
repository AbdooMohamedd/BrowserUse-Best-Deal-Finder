import asyncio
import json
import os
from datetime import datetime
from dotenv import load_dotenv
from typing import List

from browser_use import Agent, Browser
from langchain_openai import ChatOpenAI
from pydantic import SecretStr

from models import Product, BestDealsResult

# Load environment variables
load_dotenv()

# Configuration
TARGET_WEBSITES = [
    "https://www.jumia.com.eg/",
    "https://btech.com/"
]

# Initialize DeepSeek model
api_key = os.getenv("DEEPSEEK_API_KEY")
if not api_key:
    raise ValueError("DEEPSEEK_API_KEY environment variable not set")

# Initialize models with DeepSeek
llm = ChatOpenAI(
    base_url='https://api.deepseek.com/v1',
    model='deepseek-chat',
    api_key=SecretStr(api_key)
)
planner_llm = llm

async def search_product_on_website(search_term: str, website_url: str, browser: Browser) -> List[Product]:
    """
    Search for products on a specific website and extract the best deals
    """
    # Create initial actions to navigate to website and search for the product
    initial_actions = [
        {'open_tab': {'url': website_url}},
    ]
    
    # Extract website domain for reporting
    website_domain = website_url.split("//")[1].split("/")[0].replace("www.", "")
    
    task = f"""
    Find the best price for {search_term} on this website.

    1. Navigate to the website and search for the exact product
    2. Record the current price, original price if on sale, and any available discounts
    3. Note shipping costs and estimated delivery time
    4. Check if the product is in stock
    5. scroll down to load more products if necessary

    Return the data as a JSON object in this exact format:
    {{
      "top_products": [
        {{
          "name": "Product Name",
          "price": "Price with currency",
          "url": "Product URL",
          "image_url": "Image URL",
          "description": "Product description",
          "availability": "Availability status"
        }},
        ... more products ...
      ]
    }}
    """
    # Create a new context for each search
    async with await browser.new_context() as context:
        agent = Agent(
            task=task,
            llm=llm,
            planner_llm=planner_llm,
            initial_actions=initial_actions,
            browser_context=context,
            use_vision=False,  
        )
          # Run the agent
        history = await agent.run()
        
        # Extract and process the result
        result_data = history.final_result()
        products = []
        product_data = []
        
        # Extract products from different result formats
        if isinstance(result_data, str):
            try:
                # Try to find JSON in the string response
                start_idx = result_data.find('{')
                end_idx = result_data.rfind('}') + 1
                if start_idx >= 0 and end_idx > start_idx:
                    data_dict = json.loads(result_data[start_idx:end_idx])
                    product_data = data_dict.get("top_products") or data_dict.get("products") or []
            except json.JSONDecodeError:
                pass
        elif isinstance(result_data, dict):
            product_data = result_data.get("top_products") or result_data.get("products") or []
        elif isinstance(result_data, list):
            product_data = result_data
        
        # Convert to Product objects
        for item in product_data[:10]:  
            try:
                # Handle price format variations
                price_str = item.get("price", "0")
                if isinstance(price_str, str):
                    import re
                    price_match = re.search(r'[\d,]+\.?\d*', price_str.replace(",", ""))
                    if price_match:
                        price = float(price_match.group())
                    else:
                        price = 0.0
                else:
                    price = float(price_str) if price_str else 0.0
                
                # Handle image URL
                image_url = item.get("image_url") or item.get("image") or ""
                products.append(
                    Product(
                        name=item.get("name", "Unknown"),
                        price=price,
                        url=item.get("url", ""),
                        image=image_url,
                        description=item.get("description", ""),
                        availability=item.get("availability", "Unknown"),
                        website_source=website_domain,
                        search_term=search_term,
                        extracted_at=datetime.now()
                    )
                )
            except Exception as e:
                print(f"Error creating Product object: {e}")
        return products

async def main():
    print("🔍 BrowserUse Best Deal Finder")
    
    # Get user input
    query = input("Enter a product to search for: ")
    
    # Initialize browser
    browser = Browser()
    all_products = []
    total_products = 0
    
    try:
        print(f"\n🔎 Searching for '{query}'...")
        
        # Search on all websites
        for website in TARGET_WEBSITES:
            website_domain = website.split("//")[1].split("/")[0].replace("www.", "")
            print(f"  📱 Searching on {website_domain}...")
            
            products = await search_product_on_website(query, website, browser)
            total_products += len(products)
            
            print(f"  ✅ Found {len(products)} products on {website_domain}")
            all_products.extend(products)
        
        # Just sort by price
        sorted_products = sorted(all_products, key=lambda p: p.price if p.price > 0 else float('inf'))
        
        # Take the top 3 products
        best_products = sorted_products[:3]
        result = BestDealsResult(
            original_query=query,
            search_terms=[query], 
            best_products=best_products,
            total_products_found=total_products
        )
        
        # Output results to console
        print("\n🏆 Best Deals Found:")
        for i, product in enumerate(best_products):
            print(f"\n#{i+1}: {product.name}")
            print(f"  💰 Price: {product.price}")
            print(f"  🌐 Website: {product.website_source}")
            print(f"  🔗 URL: {product.url}")
            print(f"  ✅ Availability: {product.availability}")
        
        # Save to JSON file
        with open("best_prices.json", "w") as f:
            f.write(result.model_dump_json(indent=2))
        
        print("\n💾 Results saved to best_prices.json")
    
    finally:
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())