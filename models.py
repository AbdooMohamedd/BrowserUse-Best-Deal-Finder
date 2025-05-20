from pydantic import BaseModel, HttpUrl, Field
from typing import Optional, List
from datetime import datetime

class Product(BaseModel):
    name: str
    url: HttpUrl
    price: float
    website_source: str
    search_term: str
    image: Optional[HttpUrl] = None
    description: Optional[str] = None
    availability: Optional[str] = None
    extracted_at: datetime = Field(default_factory=datetime.now)
    
class ProductSearchResult(BaseModel):
    search_term: str
    products: List[Product]
    
class BestDealsResult(BaseModel):
    original_query: str
    search_terms: List[str]
    best_products: List[Product]
    total_products_found: int
    timestamp: datetime = Field(default_factory=datetime.now)
