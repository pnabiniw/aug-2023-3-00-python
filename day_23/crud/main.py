from create import create_student
from read import read_student
from update import update_student
from delete import delete_student


def inquiry():
    selection = input("Enter your choice c/r/u/d/e ")
    selection = selection.lower()

    def exit_message():
        print("Thank You. See You Again !!")
    if selection == "c":
        program_continue = create_student()
        inquiry() if program_continue else exit_message()
    elif selection == "r":
        read_student()
    elif selection == "u":
        update_student()
    elif selection == "d":
        delete_student()
    else:
        exit_message()


if __name__ == "__main__":
    inquiry()
