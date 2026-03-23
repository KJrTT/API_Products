from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/products", tags=["products"])

db: list[dict] = [
    {"id": 1, "name": "iPhone 15",     "price": 99990, "in_stock": True},
    {"id": 2, "name": "MacBook Air",   "price": 139990,"in_stock": True},
    {"id": 3, "name": "AirPods Pro 2", "price": 24990, "in_stock": False},
]
next_id = 4


class ProductIn(BaseModel):
    name: str
    in_stock: bool = True
    price: int
    id: int


@router.get("/")
def get_products(min_price: int = None, max_price: int = None, in_stock: bool = None):
    result = db.copy()

    if min_price is not None and max_price is not None and min_price < max_price:
        raise HTTPException(400, "min_price не может быть больше max_price")
    
    if min_price is not None:
        result = [s for s in result if s["price"] >= min_price]
    if max_price is not None: 
        result = [s for s in result if s["price"] <= max_price]
    if in_stock is not None:
        result = [p for p in result if p["in_stock"] == in_stock]
    
    return result
