from controller import Controller

def main():
    dict_table = {
        1 : ['bar_id', 'name', 'address'],
        2 : ['goods_id', 'client_id'],
        3 : ['goods_id', 'name', 'price', 'bar_id'],
        4 : ['goods_id', 'client_id'],
    }
    dbname = 'Bar'
    user = 'postgres'
    password = '1234'
    host = 'localhost'
    port = 5432
    control = Controller(dict_table, dbname, user, password, host, port)
    control.menu()

if __name__ == '__main__':
    main()
