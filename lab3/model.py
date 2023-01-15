from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from abc import abstractmethod
from models import *


class Model:
    def __init__(self, database, user, password, host, port):
        self.database = database
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.dict_foo = {
            1: SelectTable,
            2: InsertData,
            3: UpdateData,
            4: DeleteData,
        }
        self.dict_table = {
            1: Bar,
            2: Goods,
            3: Client,
            4: GoodsClient,
        }

    def get_engine(self):
        return create_engine(url=f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}")

    def connect(self):
        try:
            _engine = self.get_engine()
            Base.metadata.create_all(_engine)
            return sessionmaker(bind=_engine)()
        except Exception as ex:
            print("Connection could not be made due to the following error: \n", ex)

    def execute(self, task, table_name=None, values=None):
        session = self.connect()
        tasks = self.dict_foo[task](session, self.dict_table[table_name], values)
        tasks()


class Task:
    def __init__(self, session, table, values):
        self.session = session
        self.table = table
        self.values = values

    @abstractmethod
    def __call__(self):
        raise NotImplemented


class SelectTable(Task):
    def __call__(self):
        for item in self.session.query(self.table).all():
            for column in item.__table__.columns:
                print(column.name, end='  ')
            print()
            break
        for item in self.session.query(self.table).all():
            for value in tuple(getattr(item, column.name) for column in item.__table__.columns):
                print(value, end='  ')
            print()


class InsertData(Task):
    def __call__(self):
        self.session.add(self.table(*self.values.values()))
        self.session.commit()


class UpdateData(Task):
    def __call__(self):
        column_id_ = list(self.values.keys())[0]
        id_ = self.values[column_id_]
        del self.values[column_id_]
        data = list(self.values.values())
        row = self.session.query(self.table).get(id_)
        columns = [col for col in row.__table__.columns.keys()]
        columns.pop(0)

        for column, d in zip(columns, data):
            if d != '-':
                row.__setattr__(column, d)
        self.session.commit()

class DeleteData(Task):
    def __call__(self):
        row_ = self.session.query(self.table).get(self.values[1])
        if row_:
            self.session.delete(row_)
            self.session.commit()
