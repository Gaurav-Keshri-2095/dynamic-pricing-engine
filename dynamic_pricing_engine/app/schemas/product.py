# for validation
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# -----------------------------
# Common Fields
# -----------------------------
class ProductBase(BaseModel):
    name: str
    sku: str
    base_price: float
    current_price: float
    min_price: float
    max_price: float 
    stock_level: int

# -----------------------------
# Create Product
# -----------------------------
class ProductCreate(ProductBase):
    pass


# -----------------------------
# Update Product (Pricing Engine)
# Optional fields
# -----------------------------
class ProductUpdate(BaseModel):
    current_price: Optional[float]= None
    min_price: Optional[float]= None
    max_price: Optional[float]= None
    stock_level: Optional[int]= None


# -----------------------------
# Response Schema
# -----------------------------

class ProductResponse(ProductBase):
    id: int
    updated_at: datetime
    
    class Config:
        from_attributes = True
