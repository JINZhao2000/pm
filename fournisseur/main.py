from fastapi import FastAPI, BackgroundTasks
from .services import *

app = FastAPI()


@app.get("/inner/products")
async def get_products(bgTasks: BackgroundTasks):
    bgTasks.add_task(get_products_serv)
    return {"message": "OK"}


@app.post("/inner/order")
async def recv_order(bgTasks: BackgroundTasks, products: ProductNumList):
    bgTasks.add_task(recv_order_serv, products)
    return {"message": "OK"}


@app.get("/inner/estimate")
async def make_estimate(bgTasks: BackgroundTasks, orderid: int):
    bgTasks.add_task(estimate_serv, orderid)
    return {"message": "OK"}


@app.post("/inner/human")
async def human_intervention(bgTasks: BackgroundTasks):
    bgTasks.add_task(human_intervention_estimation)
    return {"message": "OK"}


@app.post("/inner/confirmOrder")
async def confirm_order(bgTasks: BackgroundTasks, orderid: IntValue):
    bgTasks.add_task(confirm_order_serv, orderid.get_value())
    return {"message": "OK"}


@app.get("/inner/dashboard")
def dashboard():
    return dashboard_serv()