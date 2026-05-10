import os
from fastapi import FastAPI

app = FastAPI(title="Inventory Service 02")

# Персоналізація згідно з Етапом 2 та 3
STUDENT_N = int(os.getenv("STUDENT_N", 2))

# Початкові ID починаються з 100 * 2 = 200
inventory_db = {
    201: {"name": "Espresso Machine", "stock": 10},
    202: {"name": "Coffee Beans 1kg", "stock": 50}
}

@app.get("/stock/{item_id}")
async def get_stock(item_id: int):
    item = inventory_db.get(item_id)
    return {
        "item_id": item_id,
        "data": item if item else "Not Found",
        "student_id": STUDENT_N  # Обов'язкове поле
    }

@app.get("/health")
async def health():
    return {"status": "ok", "student_id": STUDENT_N}