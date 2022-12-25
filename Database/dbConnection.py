import psycopg2
import os

#DATABASE_URL = os.environ.get('DATABASE_URL')
DATABASE_URL = "postgresql://doadmin:AVNS_NuifHz0JeZ080YiuFfj@db-postgresql-nyc1-91048-do-user-12763043-0.b.db.ondigitalocean.com:25060/defaultdb?sslmode=require"""

class singleton:
    connection = None

    @staticmethod
    def getInstance():
            if singleton.connection is None or singleton.connection.closed:
                singleton()
            print("Server connection is successful")
            return singleton.connection

    def __init__(self):
        singleton.connection = psycopg2.connect(DATABASE_URL,sslmode='require')

def getCursor():

    return singleton.getInstance().cursor()

#To send changes to database
def commit():
    singleton.connection.commit()




def close_database_connection():
    if singleton.connection!=None:
        singleton.connection.close()
        singleton.connection=None


