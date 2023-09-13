from estd_connection import estd_connection

cursor = estd_connection()

id = input("Enter student ID ")
name = input("Student name ")
age = int(input("Enter student's age "))
address = input("Enter student's address ")

sql = f"""
INSERT INTO STUDENT (ID, NAME, AGE, ADDRESS) VALUES ('{id}', '{name}', {age}, '{address}')
"""

cursor.execute(sql)
print("Student added successfully !!")
