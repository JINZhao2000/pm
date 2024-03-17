from model.model import *
from utils.utils import fport, fhost, cport, chost


def recv_products_serv(products: list[Product]):
    print("Products received:")
    for product in products:
        print(product)


def recv_order_serv(orderid: int):
    if orderid == -1:
        print("The order is not validated by provider.")
        return
    print(f"The order is received : order id {orderid}.")


def recv_estimate_serv(estimate: float):
    if estimate < 0:
        print("The estimate is not validated by provider.")
        return
    print("The estimate is : ", estimate)


def recv_confirm_order_serv(orderid: int):
    print(f"The order {orderid} is confirmed")
