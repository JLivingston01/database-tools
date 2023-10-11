from pydatabasetools.tools import DBConnector

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

if __name__=='__main__':
    unittest.main()