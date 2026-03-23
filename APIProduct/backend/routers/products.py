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

@router.get("/{product_id}")
def get_product(product_id: int):
    for p in db:
        if p["id"] == product_id:
            return p
    raise HTTPException(404, "Товар не найден")

def checkunique_name(name: str):
    in_unique = True
    for s in db:
       if s["name"].lower() == name.lower():
           in_unique = False
    return in_unique

@router.post("/", status_code=201)
def add_product(body: ProductIn):
    global next_id
    if not body.name.strip():
        raise HTTPException(400, "Название не может быть пустым")
    name_length = len(body.name.strip())
    if name_length < 2 or name_length > 80:
        raise HTTPException(400, "Название должно быть от 2 до 80 символов")
    if not checkunique_name(body.name.strip()):
        raise HTTPException(400, "Название должно быть уникальным")
    if body.price < 0:
        raise HTTPException(400, "Цена не может быть отрицательной")
    
    product = {"id": next_id, "name": body.name.strip(), "price": body.price, "in_stock": body.in_stock}
    db.append(product)
    next_id += 1
    return product


@router.put("/{product_id}")
def update_product(product_id: int , body: ProductIn):
    name_length = len(body.name.strip())
    if name_length < 2 or name_length > 80:
        raise HTTPException(400, "Название должно быть от 2 до 80 символов")
    if body.price < 0:
        raise HTTPException(400, "Цена не может быть отрицательной")
    
    product_index = None
    for s,i in enumerate(db):
        if s["id"] == product_id:
            product_index = i
            break

    if product_index is None:
        raise HTTPException(400, "Товар не найден")
    for s in db:
        if s["id"] != product_id and body.name.strip().lower() == s["name"].lower():
            raise HTTPException(400, "Товар с таким названием уже существует")
    
    db[product_index] = {"id": product_id, "name": body.name.strip(), "price": body.price, "in_stock": body.in_stock}
    return db[product_index]

