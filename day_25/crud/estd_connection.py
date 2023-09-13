# If we want to connect database from a program (Python, javaScript) then
# we need a database connector
# Database connector connects your program with Database
# mysqlclient, psycopg2 etc. are the db connectors


def estd_connection():
    import psycopg2
    conn = psycopg2.connect(
        database="studenttestdb",
        user="postgres",
        password="password",
        host="127.0.0.1",
        port=5432
    )
    conn.autocommit = True
    print("Connection established successfully !!")
    cursor = conn.cursor()
    return cursor


if __name__ == "__main__":
    estd_connection()
