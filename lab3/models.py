import sqlalchemy
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Bar(Base):
    __tablename__ = 'Bar'
    bar_id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)

    def __init__(self, name, address):
        self.name = name
        self.address = address
        super(Bar, self).__init__()


class Goods(Base):
    __tablename__ = 'Goods'
    goods_id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    bar_id = Column(Integer, ForeignKey('Bar.bar_id'))

    plant = relationship('Bar', foreign_keys=[bar_id])

    def __init__(self, name, price, bar_id):
        self.name = name
        self.price = price
        self.bar_id = bar_id
        super(Goods, self).__init__()


class Client(Base):
    __tablename__ = 'Client'
    client_id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name
        super(Client, self).__init__()


class GoodsClient(Base):
    __tablename__ = 'Goods_Client'
    goods_id = Column(Integer, ForeignKey('Goods.goods_id'), primary_key=True)
    client_id = Column(Integer, ForeignKey('Client.client_id'), primary_key=True)

    goods = relationship("Goods", foreign_keys=[goods_id])
    client = relationship("Client", foreign_keys=[client_id])

    def __init__(self, goods_id, client_id):
        self.goods_id = goods_id
        self.client_id = client_id
        super(GoodsClient, self).__init__()