import pika

from fournisseur import db

parameters = pika.ConnectionParameters('localhost', 5672, '/', pika.PlainCredentials('pm', 'pm'))


def estimation(oid: int):
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.queue_declare(queue='estimation', durable=True)
    channel.basic_publish(exchange='', routing_key='estimation', body=str(oid))
    with db.connection.cursor() as cursor:
        sql = f"insert into sessions(oid, status) value ({oid}, 0)"
        cursor.execute(sql)
    connection.close()


def estimation_consume():
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.queue_declare(queue='estimation', durable=True)
    method_frame, header_frame, body = channel.basic_get(queue='estimation', auto_ack=True)
    if method_frame:
        orderid = body.decode("utf-8")
        price = 0
        with db.connection.cursor() as cursor:
            sql = ("select pnum, pprice from product natural join product_ordercli natural join ordercli "
                   f"where ordercli.oid = {orderid}")
            cursor.execute(sql)
            results = cursor.fetchall()
            for result in results:
                price += result[0] * result[1]
        confirmed = ""
        while confirmed != "y" and confirmed != "n":
            confirmed = input(f"Order {orderid} has price {price}, do you confirm this estimation (y/n)?\n")
            confirmed = confirmed.lower()
        if confirmed == "y":
            with db.connection.cursor() as cursor:
                sql = f"update sessions set status = 1 where oid = {orderid}"
                cursor.execute(sql)
            return orderid, price
        else:
            with db.connection.cursor() as cursor:
                sql = f"update sessions set status = -1 where oid = {orderid}"
                cursor.execute(sql)
            return orderid, -1
    return None, None
