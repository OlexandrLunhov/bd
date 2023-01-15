from controller import Controller

def main():
    dict_table = {
        'Bar': ['bar_id', 'name', 'address'],
        'Goods_Client': ['goods_id', 'name', 'client_id'],
        'Goods': ['goods_id', 'name', 'price', 'bar_id'],
        'Client': ['client_id', 'name']
    }
    dbname = 'Bar'
    user = 'postgres'
    password = '1234'
    host = 'localhost'
    port = '5432'
    control = Controller(dict_table, dbname, user, password, host, port)
    control.menu()

if __name__ == '__main__':
    main()
