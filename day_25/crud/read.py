from estd_connection import estd_connection


def read_student():
    cursor = estd_connection()
    student_id = input("Enter the student id ")
    sql = f"""
    SELECT * FROM STUDENT WHERE ID='{student_id}'
    """
    cursor.execute(sql)
    choice = input("Do you want to continue? (y/n) ")
    return choice.lower() == "y"
