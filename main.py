#fastAPI with body and multiple methods within 1 fastAPI
from typing import Optional
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
from pydantic import BaseSettings

from fastapi import Body, FastAPI, status
from fastapi.responses import JSONResponse

class Order_info(BaseSettings):
    #app_name: str = "Awesome API"
    order_id: int = 0

#uvicorn fastAPI1:app --reload
class orders(BaseModel):
    id: Optional[str] = None
    crust: str
    toppings: List[str]
    # EXAMPLE Body
    """
    {
    "crust": "thin",
    "toppings": ["cheese","jalapenos"]
    }
    """

orders_list = []
last_order_id = 0
order_item = {
    "crust": "Thick",
    "toppings": ["cheese","jalapenos"]
    }

#orders_list.append(order_item)   
order_info = Order_info() 
app = FastAPI()

@app.post("/orders/")
async def create_item(order: orders):
    #print(order)
    #print(orders_list)
    #print(order_info.order_id)
    order_info.order_id = order_info.order_id + 1
    order_id = order_info.order_id
    order.id = order_id
    orders_list.append(order)
    return orders_list

@app.get("/orders/")
async def get_all_orders():
    return {"Order List" : orders_list}

@app.get("/orders/{option}")
async def get_orders(option : int):
    for i in orders_list:
        if i.id == option:
            print(i)
            return i

    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content="")
