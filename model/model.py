from typing import List

from pydantic import BaseModel


class Product(BaseModel):
    pid: int
    pname: str
    pprice: float

    def __repr__(self):
        return f"<Product : id={self.pid}, name={self.pname}, price={self.pprice}"


class Ordercli(BaseModel):
    oid: int
    otime: int
    oconfirmed: int


class ProductNum(BaseModel):
    pid: int
    pnum: int

    def __repr__(self):
        return f"<ProductNum: id={self.pid}, name={self.pnum}"


class ProductNumList(BaseModel):
    products: List[ProductNum]

    def __repr__(self):
        return f"<ProductNumList: products={self.products}>"


class IntValue(BaseModel):
    value: int

    def get_value(self):
        return self.value

    def __repr__(self):
        return self.value


class FloatValue(BaseModel):
    value: float

    def get_value(self):
        return self.value

    def __repr__(self):
        return self.value


class ProductOrdercli(BaseModel):
    poid: int = -1
    pid: int
    pnum: int
    oid: int = -1

    def __repr__(self):
        return f"<ProductOrdercli poid={self.poid}, pid={self.pid}, pnum={self.pnum}, oid={self.oid}>"


class Session:
    sid: int = -1
    oid: int = -1
    status: str = ""

    def __init__(self, sid: int, oid: int, status: int):
        self.sid = sid
        self.oid = oid
        if status == 0:
            self.status = "WAIT HUMAN INTERVENTION"
        elif status == 1:
            self.status = "ACCEPTED ESTIMATION"
        elif status == -1:
            self.status = "REFUSED ESTIMATION"
        else:
            self.status = "UNKNOWN"

    def __repr__(self):
        return "{'Session id': " + str(self.sid) + ", 'Order id'= " + str(self.oid) + ", 'Status'= '" + self.status + "'}"
