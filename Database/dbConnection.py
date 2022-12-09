#import os
# DATABASE_URL = os.environ.get('DATABASE_URL')
import psycopg2

DATABASE_URL = "postgresql://doadmin:AVNS_NuifHz0JeZ080YiuFfj@db-postgresql-nyc1-91048-do-user-12763043-0.b.db.ondigitalocean.com:25060/defaultdb?sslmode=require"


def getCursor():
    return Singleton.instance(True).cursor()


def commit():
    Singleton.connection.commit()

class Singleton:
    connection = None

    def __init__(self):
        if Singleton.connection is not None:
            print ("Already has a connection")
        else:
            Singleton.connection = psycopg2.connect(DATABASE_URL)

    @staticmethod
    def instance(shouldUpdate):
        if shouldUpdate:
            return psycopg2.connect(DATABASE_URL)

        if Singleton.connection is None:
            Singleton()
        return Singleton.connection

