import time

from model.model import *
from .mq import *
import pymysql

connection = pymysql.connect(host='rm-4xo63l909kdrexz8kio.mysql.germany.rds.aliyuncs.com', port=3306, user='pm',
                             password='PMpm2024', db='pm')


# get the list of products from database
async def get_products_from_db():
    with connection.cursor() as cursor:
        sql = "select pid, pname, pprice from product"
        cursor.execute(sql)
        results = cursor.fetchall()
        results = [row for row in results]
    return [Product(pid=row[0], pname=row[1], pprice=row[2]) for row in results]


# check the validation of order and create the order
async def check_order(products: ProductNumList):
    # human intervention in console
    confirm = ""
    print("The products in this order are the followings:")
    for product in products:
        print(product)
    print()
    while confirm != "y" and confirm != "n":
        confirm = input("Do you confirm this order? (y/n) ")
        confirm = confirm.lower()

    if confirm == "n":
        return Ordercli(oid=-1, otime=-1, oconfirmed=-1)

    # create valid order
    with connection.cursor() as cursor:
        sql = "select count(*) from ordercli"
        cursor.execute(sql)
        result = cursor.fetchone()
    oid = result[0] + 1
    ord = Ordercli(oid=oid, otime=time.time_ns(), oconfirmed=0)
    with connection.cursor() as cursor:
        sql = f"insert into ordercli (oid, otime, oconfirmed) value ({ord.oid}, {ord.otime}, {ord.oconfirmed})"
        cursor.execute(sql)
        for product in products.products:
            sql = f"insert into product_ordercli(pid, pnum, oid) value ({product.pid}, {product.pnum}, {oid})"
            cursor.execute(sql)
        sql = f"insert into sessions(oid, status) value ({oid}, {0})"
        cursor.execute(sql)
        connection.commit()
    return ord


# calculate the total price estimation
async def calculate_estimate(orderid: int):
    estimation(orderid)


async def human_intervention_estimation():
    orderid, result = estimation_consume()
    return orderid, result


# confirm the order
async def confirm_order_dao(orderid: int):
    with connection.cursor() as cursor:
        sql = f"update ordercli set oconfirmed = 1 where oid = {orderid}"
        cursor.execute(sql)
        sql = f"update sessions set status = 3 where oid = {orderid}"
        cursor.execute(sql)
        connection.commit()


def dashboard_dao():
    with connection.cursor() as cursor:
        sql = f"select sid, oid, status from sessions"
        cursor.execute(sql)
        results = cursor.fetchall()
        results = [row for row in results]
    return [Session(sid=row[0], oid=row[1], status=int(row[2])) for row in results]
