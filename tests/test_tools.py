from pydatabasetools.tools import DBConnector

from sqlalchemy import (
    text
)

import os

import unittest

class TestSimple(unittest.TestCase):

    def test_str_sqlite(self):

        client = DBConnector(
            dialect='sqlite',
            driver='',
            username='',
            password='',
            host='',
            port='',
            database='sqlite.db'
        )

        url = client._create_url()

        self.assertEqual(url,'sqlite:///sqlite.db')

        
    def test_str_postgres(self):

        client = DBConnector(
            dialect='postgresql',
            driver='psycopg2',
            username='user',
            password='pass123',
            host='localhost',
            port='5151',
            database='database'
        )

        url = client._create_url()

        self.assertEqual(url,'postgresql+psycopg2://user:pass123@localhost:5151/database')

                
    def test_str_postgres_noport(self):

        client = DBConnector(
            dialect='postgresql',
            driver='psycopg2',
            username='user',
            password='pass123',
            host='localhost',
            port='',
            database='database'
        )

        url = client._create_url()

        self.assertEqual(url,'postgresql+psycopg2://user:pass123@localhost/database')

    def test_connect_sqlite(self):

        tmp_path = f".unittest_data"
        os.makedirs(tmp_path,exist_ok=True)

        client = DBConnector(
            dialect='sqlite',
            driver='',
            username='',
            password='',
            host='',
            port='',
            database=f'{tmp_path}/sqlite.db'
        )
        engine = client._make_db_engine()
        with engine.connect() as conn:
            result = conn.execute(text("select 'hello world';")).fetchall()
            print(result)
            conn.close()
        
        engine.dispose()

        files = os.listdir(f"{tmp_path}")
        if len(files)>0:
            dbname = files[0]
        else:
            dbname = 'nodb'

        os.system(f"rm -rf {tmp_path}")

        self.assertEqual(dbname,'sqlite.db')

if __name__=='__main__':
    unittest.main()