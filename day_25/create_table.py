from estd_connection import estd_connection

cursor = estd_connection()

# cursor.execute("DROP TABLE STUDENT")

sql = """
CREATE TABLE STUDENT(
    ID CHAR(20),
    NAME CHAR(20),
    AGE INT,
    ADDRESS CHAR(20)
)
"""

cursor.execute(sql)
print("Table Created Successfully !!")
