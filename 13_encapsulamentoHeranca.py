class DatabaseConn:

    def __init__(self) -> None:
        self.__database = 'Postgres'
        self._conn = '//conection_string'
        self.user = 'Lhama'
    
    def get_database(self) -> None:
        print(self.__database)
    
    def _testing_connection(self) -> None:
        print('Connection Ok!')
    
class Repository(DatabaseConn):

    def __init__(self) -> None:
        super().__init__()

    def select(self) -> None:
        self._testing_connection()
        print(f'Connecting to {self._conn}')
        print('Select * from table')
        print(self.user)

repo = Repository()
repo.select()