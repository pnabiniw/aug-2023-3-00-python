from estd_connection import estd_connection

cursor = estd_connection()

id = input("Enter student ID ")

sql = f"""
SELECT * FROM STUDENT WHERE ID='{id}'
"""

cursor.execute(sql)
result = cursor.fetchone()
print(result)
print(type(result))

result = [x.strip() for x in result if type(x) == str]
print(result)
