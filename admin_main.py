import json
from Quiz import *
from Question import *


quiz_name = '' #global name for the quiz

#--------------------------------------------------
def take_a_quiz_from_admin():
    quiz_data = {}
    global quiz_name
    quiz_name = input(">> Please Enter the name of the quiz: ").strip().lower()
    num_of_questions = int(input(">> Please Enter the number of questions: ").strip())
    questions = []
    for i in range(num_of_questions):
        question_data = {}
        question_text = input(f">> Please Enter the question{i+1} text: ").strip()
        question_data["question"] = question_text
        options = []
        print('Please Enter 4 Options:')
        for i in range(4):
            option = input(f">> Please Enter the option {i+1}: ").strip().lower()
            options.append(option)
        question_data["options"] = options

        # ask user to enter the index
        while True:
            correct_answer = int(input(">> Please Enter the number of the correct option: ").strip())
            try:
                question_data["answer"] = options[correct_answer - 1]
                break
            except IndexError:
                print(">> The correct answer was not found.")
                continue
        # add the question to the questions list
        questions.append(question_data)
    # add the questions list to the quiz
    quiz_data[quiz_name] = questions
    return quiz_data

#--------------------------------------------------
# function to add to JSON file
def append_the_quiz_to_the_json_file(filename, quiz_data):
    with open(filename,'r+') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside
        file_data[quiz_name] = quiz_data[quiz_name]
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)

#--------------------------------------------------

def start_admin_quiz_app():
    while True:
        print("******* Welcome Admin ********")
        option = input('>> Do you want to add a new quiz? [y: YES/ q: QUIT]')
        if option.lower() == 'y':
            quiz_data = take_a_quiz_from_admin()
            append_the_quiz_to_the_json_file('quiz.json', quiz_data)

        elif option.lower() == 'q':
            print('************Good Luck*************')
            exit(0)
        else:
            print('Invalid option, Please try again')
            continue
















if __name__ == '__main__':
    start_admin_quiz_app()