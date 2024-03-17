from fournisseur.db import *
from utils.utils import get, post, fhost, fport, cport, chost
from model.model import *


async def get_products_serv():
    results = await get_products_from_db()
    await post(f"http://{chost}:{cport}/cli/products", data=results)


async def recv_order_serv(products: ProductNumList):
    result = await check_order(products)
    await post(f"http://{chost}:{cport}/cli/checkOrderMsg", data=result)


async def estimate_serv(order_id: int):
    await calculate_estimate(order_id)


async def human_intervention_serv():
    orderid, result = await human_intervention_estimation()
    if orderid is not None:
        await post(f"http://{chost}:{cport}/cli/estimate", data=FloatValue(value=result))


async def confirm_order_serv(order_id: int):
    await confirm_order_dao(order_id)
    await post(f"http://{chost}:{cport}/cli/confirmOrderMsg", data=IntValue(value=order_id))


def dashboard_serv():
    return dashboard_dao()