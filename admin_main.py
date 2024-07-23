import json
from Quiz import *
from Question import *


def take_a_quiz_from_admin() -> tuple[str, dict]:
    """
    This function used to take a quiz from admin and store it in a python dictionary.
    Args:
        No args
    Return:
        returns a tuple of (quiz_name: the name of the quiz which taken from user
        , quiz_data: the quiz's data as a python dictionary)
    """
    quiz_data = {}

    # take quiz name from the admin, validate it
    while True:
        quiz_name = input(">> Please Enter the name of the quiz: ").strip().lower()
        if quiz_name == '':
            print(">> Please enter a valid name.")
            continue
        break

    while True:
        try:
            num_of_questions = int(input(">> Please Enter the number of questions: ").strip())
        except ValueError:
            print(">> Please enter a valid number.")
            continue
        if num_of_questions <= 0:
            print(">> There should be at least one question.")
            continue
        break

    questions = []  # list of questions of the quiz
    for i in range(num_of_questions):
        question_data = {}
        while True:
            try:
                question_text = input(f">> Please Enter the question{i + 1} text: ").strip()
            except Exception:
                print(">> Please enter a valid text.")
                continue
            if question_text == '':
                print(">> Please enter a valid text.")
                continue
            break

        question_data["question"] = question_text
        options = []
        print('Please Enter 4 Options:')
        for j in range(4):
            while True:
                option = input(f">> Please Enter the option {j + 1}: ").strip().lower()
                if option == '':
                    print(">> Please enter a valid option.")
                    continue
                break
            options.append(option)
        question_data["options"] = options

        # ask user to enter the index
        while True:
            try:
                correct_answer = int(input(">> Please Enter the number of the correct option: ").strip())
                question_data["answer"] = options[correct_answer - 1]
                break
            except Exception:
                print(">> Please enter a valid number of option.")

        # add the question to the questions list
        questions.append(question_data)

    # add the questions list to the quiz
    quiz_data[quiz_name] = questions
    return quiz_name, quiz_data


# function to add to JSON file
def append_the_quiz_to_the_json_file(filename: str, quiz_data: dict, quiz_name: str) -> None:
    """
    This function used to append the quiz to the json file of quizzes
    Args:
        filename: the name of the json file contains the quizzes
        quiz_data: the quiz's data as a python dictionary
        quiz_name: the name of the quiz

    Return:
        returns a tuple of (quiz_name: the name of the quiz which taken from user
        , quiz_data: the quiz's data as a python dictionary)
    """
    with open(filename, 'r+') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside
        file_data[quiz_name] = quiz_data[quiz_name]
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent=4)


def start_admin_quiz_app() -> None:
    """
    This function used to start the quiz app for the admin, it takes a quiz from the admin
    and stores it in a json file
    Args:
        No Args
    Return:
        does not return anything, it is the main method to trigger all other methods of the app
    """
    while True:
        print("******* Welcome Admin ********")
        option = input('>> Do you want to add a new quiz? [y: YES/ q: QUIT]')
        if option.lower() == 'y':
            quiz_name, quiz_data = take_a_quiz_from_admin()
            append_the_quiz_to_the_json_file(filename='quiz.json', quiz_data=quiz_data, quiz_name=quiz_name)
            print(">> Your Quiz Saved Successfully!!")
        elif option.lower() == 'q':
            print('************Good Luck*************')
            exit(0)
        else:
            print('Invalid option, Please try again')
            continue


if __name__ == '__main__':
    start_admin_quiz_app()
