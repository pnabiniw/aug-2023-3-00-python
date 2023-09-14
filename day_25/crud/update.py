from estd_connection import estd_connection

def update_student():
    cursor = estd_connection()
    student_id = input("Enter the student id ")
    key = input("Enter the info you want to update ")  # name
    value = input(f"Enter the new {key}")  # Ram  (Jon)
    sql = f"""
    UPDATE STUDENT SET {key}='{value}' WHERE ID='{student_id}'
    """
    cursor.execute(sql)
    print("Information Updated Successfully !!")
    choice = input("Do you want to continue? (y/n) ")
    return choice.lower() == "y"
