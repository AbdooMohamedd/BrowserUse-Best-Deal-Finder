# 🔍 BrowserUse Best Deal Finder

An AI-powered price comparison tool built with [Browser-Use](https://github.com/microsoft/browsing-assistant) and DeepSeek AI. Find the best deals across multiple e-commerce websites without the hassle of manual searching.

## What it does

BrowserUse Best Deal Finder is a powerful tool that automates the tedious process of searching for the best product deals across multiple e-commerce websites. It leverages the Browser-Use framework's AI agent capabilities to navigate websites, extract product information, and identify the best deals based on price.

The tool:

1. Takes a product name as input from the user
2. Automatically searches for it on configured e-commerce websites (Jumia, B.Tech, etc.)
3. Extracts detailed product information including name, price, image, URL, and availability
4. Sorts all results by price to identify the best deals
5. Presents the top 3 best deals in the console
6. Saves all product data in a structured JSON format for further processing

### Key Features

- **Automated Web Browsing**: Uses Browser-Use's AI agent to navigate e-commerce sites just like a human would
- **Multi-Website Comparison**: Searches across multiple e-commerce websites in parallel
- **Price-Based Ranking**: Identifies the best deals based on actual prices
- **Detailed Product Information**: Extracts product names, prices, images, URLs, descriptions and availability
- **Structured Data Output**: Saves all results to a clean JSON file for further processing or analysis
- **DeepSeek AI Integration**: Uses DeepSeek's powerful language model for web navigation and information extraction

## Installation

### Prerequisites

- Python 3.11 or higher
- Chrome or Edge browser installed
- DeepSeek API key ([Get one here](https://platform.deepseek.com/))
- Git (optional, for cloning the repository)

### Setup Instructions

1. **Clone or download the repository:**

   ```powershell
   git clone https://github.com/AbdooMohamedd/BrowserUse-Best-Deal-Finder.git
   cd BrowserUse-Best-Deal-Finder
   ```

2. **Install UV package manager (if not already installed):**

   ```powershell
   pip install uv
   ```

3. **Create and activate a UV environment:**

   ```powershell
   uv venv
   .\.venv\Scripts\Activate.ps1
   ```

4. **Install required packages using UV:**

   ```powershell
   uv pip install -r requirements.txt
   ```

5. **Set up your DeepSeek API key:**

   Create a `.env` file in the project root directory with your API key:

   ```
   DEEPSEEK_API_KEY=your_api_key_here
   ```

## Usage

1. **Run the price comparison tool:**

   ```powershell
   python agent.py
   ```

2. **Enter your product search term** when prompted

   - Example: "iPhone 13", "Samsung TV 55 inch", "Nike Air Max"

3. **Wait for the search to complete**

   - The tool will display progress as it searches each website

4. **View the results**
   - The top 3 best deals will be displayed in the console
   - Full results are saved to `best_prices.json` file

### Customizing websites

You can modify which websites are searched by editing the `TARGET_WEBSITES` list in `agent.py`:

```python
TARGET_WEBSITES = [
    "https://www.jumia.com.eg/",
    "https://btech.com/",
    # Add more websites as needed
]
```

## Example Output

### Console Output

```
🔍 BrowserUse Best Deal Finder
Enter a product to search for: iphone 13

🔎 Searching for 'iphone 13'...
  📱 Searching on jumia.com.eg...
  ✅ Found 8 products on jumia.com.eg

🏆 Best Deals Found:

#1: Apple Iphone 13 Mobile Phone - 6.1 Inches - Single SIM 5G 128GB/4GB - Blue
  💰 Price: 26444.0
  🌐 Website: jumia.com.eg
  🔗 URL: https://www.jumia.com.eg/iphone-13-6.1-inch-128gb4gb-5g-mobile-phone-blue-e-apple-mpg3818239.html
  ✅ Availability: Add to cart

#2: Apple IPhone 13 Single SIM, 128GB, 4GB RAM, 5G - Midnight Black
  💰 Price: 33566.0
  🌐 Website: jumia.com.eg
  🔗 URL: https://www.jumia.com.eg/apple-iphone-13-single-sim-128gb-4gb-ram-5g-midnight-black-132062176.html
  ✅ Availability: Add to cart

#3: Apple IPhone 13 Single SIM, 128GB, 4GB RAM, 5G - Starlight
  💰 Price: 33766.0
  🌐 Website: jumia.com.eg
  🔗 URL: https://www.jumia.com.eg/apple-iphone-13-single-sim-128gb-4gb-ram-5g-starlight-132062167.html
  ✅ Availability: Add to cart

💾 Results saved to best_prices.json
```

### JSON Output (`best_prices.json`)

```json
{
  "original_query": "iphone 13",
  "search_terms": ["iphone 13"],
  "best_products": [
    {
      "name": "Apple Iphone 13 Mobile Phone - 6.1 Inches - Single SIM 5G 128GB/4GB - Blue",
      "url": "https://www.jumia.com.eg/iphone-13-6.1-inch-128gb4gb-5g-mobile-phone-blue-e-apple-mpg3818239.html",
      "price": 26444.0,
      "website_source": "jumia.com.eg",
      "search_term": "iphone 13",
      "image": "https://eg.jumia.is/unsafe/fit-in/300x300/filters:fill(white)/product/50/4831001/1.jpg",
      "description": "Apple Iphone 13 Mobile Phone - 6.1 Inches - Single SIM 5G 128GB/4GB - Blue",
      "availability": "Add to cart",
      "extracted_at": "2025-05-21T01:16:56.216578"
    },
    {
      "name": "Apple IPhone 13 Single SIM, 128GB, 4GB RAM, 5G - Midnight Black",
      "url": "https://www.jumia.com.eg/apple-iphone-13-single-sim-128gb-4gb-ram-5g-midnight-black-132062176.html",
      "price": 33566.0,
      "website_source": "jumia.com.eg",
      "search_term": "iphone 13",
      "image": "https://eg.jumia.is/unsafe/fit-in/300x300/filters:fill(white)/product/67/1260231/1.jpg",
      "description": "Apple IPhone 13 Single SIM, 128GB, 4GB RAM, 5G - Midnight Black",
      "availability": "Add to cart",
      "extracted_at": "2025-05-21T01:16:56.210146"
    },
    {
      "name": "Apple IPhone 13 Single SIM, 128GB, 4GB RAM, 5G - Starlight",
      "url": "https://www.jumia.com.eg/apple-iphone-13-single-sim-128gb-4gb-ram-5g-starlight-132062167.html",
      "price": 33766.0,
      "website_source": "jumia.com.eg",
      "search_term": "iphone 13",
      "image": "https://eg.jumia.is/unsafe/fit-in/300x300/filters:fill(white)/product/76/1260231/1.jpg",
      "description": "Apple IPhone 13 Single SIM, 128GB, 4GB RAM, 5G - Starlight",
      "availability": "Add to cart",
      "extracted_at": "2025-05-21T01:16:56.216578"
    }
  ],
  "total_products_found": 8,
  "timestamp": "2025-05-21T01:22:02.533077"
}
```

## How It Works

The BrowserUse Best Deal Finder uses an AI-powered approach to automate product searching and price comparison:

1. **Browser Navigation**: Uses the Browser-Use framework's AI agent to open a browser and navigate to e-commerce websites
2. **Automated Searching**: Enters the user's product query into each website's search function
3. **Content Extraction**: Scrapes product details including names, prices, images and availability
4. **Deal Identification**: Sorts all products by price to find the best deals
5. **Results Processing**: Presents the top 3 products in the console and saves all data to JSON

## Technical Details

### Architecture

- **Browser-Use Framework**: Provides the core functionality for browser automation and AI agent control
- **DeepSeek AI**: Powers the language model behind the agent's understanding and decision-making
- **Pydantic Models**: Define the data structure for products and search results
- **Asyncio**: Enables asynchronous execution for better performance

### Project Structure

```
BrowserUse-Best-Deal-Finder/
├── agent.py          # Main script with search logic and agent configuration
├── models.py         # Pydantic data models for products and results
├── best_prices.json  # Output file with search results
├── requirements.txt  # Package dependencies
└── .env              # Environment variables (API keys)
```

## Troubleshooting

### Common Issues

- **DeepSeek API Key Error**: Ensure you have set the `DEEPSEEK_API_KEY` in your `.env` file
- **Browser Not Found**: Make sure Chrome or Edge is installed on your system
- **Extraction Issues**: Some websites may change their structure, requiring task prompt adjustments

## Contributing

Contributions are welcome! Feel free to:

- Add support for more e-commerce websites
- Improve product data extraction
- Enhance the price comparison logic
- Fix bugs or performance issues

## License

This project is licensed under the MIT License - see the LICENSE file for details.
