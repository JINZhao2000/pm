from fastapi import FastAPI, BackgroundTasks
from .services import *

app = FastAPI()


@app.post("/cli/products")
async def recv_products(bgTasks: BackgroundTasks, products: list[Product]):
    bgTasks.add_task(recv_products_serv, products)
    return {"message": "OK"}


@app.post("/cli/checkOrderMsg")
async def recv_order_msg(bgTasks: BackgroundTasks, ordercli: Ordercli):
    bgTasks.add_task(recv_order_serv, ordercli.oid)
    return {"message": "OK"}


@app.post("/cli/estimate")
async def recv_estimate(bgTasks: BackgroundTasks, estimate: FloatValue):
    bgTasks.add_task(recv_estimate_serv, estimate.get_value())
    return {"message": "OK"}


@app.post("/cli/confirmOrderMsg")
async def recv_confirm_order_msg(bgTasks: BackgroundTasks, orderid: IntValue):
    bgTasks.add_task(recv_confirm_order_serv, orderid.get_value())
    return {"message": "OK"}
