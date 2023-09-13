from estd_connection import estd_connection

cursor = estd_connection()

id = input("Enter student ID ")

sql = f"""
DELETE FROM STUDENT WHERE ID='{id}'
"""

cursor.execute(sql)
print("Student Deleted Successfully")
