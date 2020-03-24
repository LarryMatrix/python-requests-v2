import requests
import psycopg2

# https://api.myjson.com/bins/mkcs2


def insert():
    username = 'username'
    password = 'password'
    host = 'host'
    port = 'port'
    db = 'db'

    try:
        connection = psycopg2.connect(
            uri=uri,
            user=username,
            password=password,
            port=port,
            database=db)

        cursor = connection.cursor()
        # Print PostgreSQL Connection properties
        print(connection.get_dsn_parameters(), "\n")

        # Print PostgreSQL version
        cursor.execute("SELECT version();")

        # req = requests.get('https://api.myjson.com/bins/mkcs2')

        # print(req.json())

        record = cursor.fetchone()
        print("You are connected to - ", record, "\n")

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL::", error)
    finally:
        # closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

    # req = requests.get('https://api.myjson.com/bins/mkcs2')

    # print(req.json())


if __name__ == "__main__":
    insert()
