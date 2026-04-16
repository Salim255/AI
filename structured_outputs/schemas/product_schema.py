from pydantic import BaseModel
from typing import List

class ProductFeature(BaseModel):
    name: str
    value: str

class Product(BaseModel):
    id: str
    name: str
    price: float
    features: List[ProductFeature]