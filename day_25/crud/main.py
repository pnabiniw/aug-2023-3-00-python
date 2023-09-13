from create import create_student
from read import read_student
from update import update_student
from delete import delete_student


def inquiry():
    selection = input("Enter your choice c/r/u/d/e ")
    selection = selection.lower()
    program_continue = None

    def exit_message():
        print("Thank You. See You Again !!")
    if selection == "c":
        program_continue = create_student()
    elif selection == "r":
        program_continue = read_student()
    elif selection == "u":
        program_continue = update_student()
    elif selection == "d":
        program_continue = delete_student()
    inquiry() if program_continue else exit_message()


if __name__ == "__main__":
    inquiry()
