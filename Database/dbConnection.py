#import os
# DATABASE_URL = os.environ.get('DATABASE_URL')
import psycopg2

DATABASE_URL = "postgresql://doadmin:AVNS_NuifHz0JeZ080YiuFfj@db-postgresql-nyc1-91048-do-user-12763043-0.b.db.ondigitalocean.com:25060/defaultdb?sslmode=require"

connection = psycopg2.connect(DATABASE_URL)

def getCursor():
    return connection.cursor()

def commit():
    connection.commit()

