from estd_connection import estd_connection

def delete_student():
    cursor = estd_connection()
    student_id = input("Enter the student id ")
    sql = f"""
    DELETE FROM STUDENT WHERE ID='{student_id}'
    """
    try:
        cursor.execute(sql)
    except:
        print("Invalid Student Id")
    else:
        print("Student Deleted Successfully !!")
    choice = input("Do you want to continue? (y/n) ")
    return choice.lower() == "y"
