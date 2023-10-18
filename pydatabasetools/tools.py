from sqlalchemy import create_engine
import os

class DBConnector:

    def __init__(self,
                 dialect: str = 'sqlite',
                 driver: str = '',
                 username: str = '',
                 password: str = '',
                 host: str = '',
                 port: str = '',
                 database: str = 'sqlite.db'
                 ):
        self.dialect = dialect
        self.driver = driver
        self.username = username
        self.password = password
        self.host = host
        self.port = port
        self.database = database

    def _create_prefix_if_provided(self,s,p):

        if s != '':
            s = p+s
        
        return s

    def _create_url(self):

        driver = self._create_prefix_if_provided(self.driver,'+')
        port = self._create_prefix_if_provided(self.port,':')
        host = self._create_prefix_if_provided(self.host,'@')
        password = self._create_prefix_if_provided(self.password,':')
            
        connect_info = f"{self.username}{password}{host}{port}"

        url = f"{self.dialect}{driver}://{connect_info}/{self.database}"
        self.url = url

        return url

    def _make_db_engine(self,echo:bool = False):

        url = self._create_url()
        engine = create_engine(url,echo=echo)

        return engine
    
    def _make_db_connection(self,echo:bool = False):

        engine = self._make_db_engine(echo=echo)
        
        connection = engine.connect()

        return connection