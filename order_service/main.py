import os
import requests
from fastapi import FastAPI

app = FastAPI(title="Order Service 02")

STUDENT_N = int(os.getenv("STUDENT_N", 2))
# Звертаємось до першого сервісу за назвою контейнера з docker-compose
INVENTORY_SERVICE_URL = "http://inventory-service-02:8000"


@app.post("/orders/{item_id}")
async def create_order(item_id: int, quantity: int):
    # Перевіряємо наявність через Inventory Service
    response = requests.get(f"{INVENTORY_SERVICE_URL}/stock/{item_id}")
    stock_data = response.json()

    return {
        "order_status": "Created",
        "item_id": item_id,
        "quantity": quantity,
        "inventory_check": stock_data,
        "student_id": STUDENT_N
    }