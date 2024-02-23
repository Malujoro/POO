class PostgresDB:

    def __init__(self) -> None:
        self.__conexao = 'Postgres'
    
    def conectar(self) -> str:
        print('Conectando ao banco Postgres')
        return self.__conexao

    def desconectar(self) -> None:
        print('Desconectando do banco Postgres')


class MysqlDB:

    def __init__(self) -> None:
        self.__conexao = 'Mysql'
    
    def conectar(self) -> str:
        print('Conectando ao banco Mysql')
        return self.__conexao

    def desconectar(self) -> None:
        print('Desconectando do banco Mysql')

class Repositorio:

    def select(self, db_connection: any) -> None:
        conection = db_connection.conectar()
        print(f'Conectei ao banco {conection}')
        print('Fazendo um SELECT * FROM...')
        db_connection.desconectar()

    def insert(self, db_connection: any) -> None:
        conection = db_connection.conectar()
        print(f'Conectei ao banco {conection}')
        print('Fazendo um insert Values...')
        db_connection.desconectar()

    
db_conn_postgres = PostgresDB()
db_conn_mysql = MysqlDB()
repo = Repositorio()

repo.insert(db_conn_postgres)
print()
repo.insert(db_conn_mysql)