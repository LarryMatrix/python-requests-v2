import requests
import psycopg2

# https://api.myjson.com/bins/mkcs2


def insert():
    username = 'wkxqxgtqutdjwx'
    password = '778097e7a0247e14d9ff7917095199709637870daca6d21bd8b9d28c03f5b4ca'
    host = '127.0.0.1'
    port = 5432
    db = 'd7h4pekdeo0957'
    uri = 'postgres://wkxqxgtqutdjwx:778097e7a0247e14d9ff7917095199709637870daca6d21bd8b9d28c03f5b4ca@ec2-174-129-254-231.compute-1.amazonaws.com:5432/d7h4pekdeo0957'

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
