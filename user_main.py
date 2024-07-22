import json
from Quiz import *
from Question import *

quizzes = []

#--------------------------------------------------
def load_data_from_json_file(filename):
    json_file = open(filename)
    data = json.load(json_file)
    json_file.close()
    return data
#--------------------------------------------------
def is_valid_question(question):
    # (Simple Validation) : check number of fields
    if len(question) != 3:
        return False
    return True
#--------------------------------------------------

def extract_quizzes(data):
    for quiz, questions in data.items():
        quiz_questions = []
        for question in questions:
            if is_valid_question(question):
                question_instance = Question(question["question"],
                                             question["options"], question["answer"])
                quiz_questions.append(question_instance)

        quiz_instance = Quiz(quiz, quiz_questions)
        quizzes.append(quiz_instance)
#--------------------------------------------------
def display_quizzes_options():
    print('*******Welcome to Quiz App *********')
    print('Which quiz do you want to start?')
    for i in range(len(quizzes)):
        print(f'{i+1}. {quizzes[i].name} Quiz')
#--------------------------------------------------
def start_quiz(quiz_index):
    quiz = quizzes[quiz_index]
    print('*'*10)
    print(f'Welcome to Quiz {quiz.name}')
    questions_count = 0
    for question in quiz.questions:
        questions_count += 1
        print(f'Question {questions_count}: {question}')
        answer = int(input('>> Please Enter the number of the correct answer: '))
        if question.is_correct_answer(answer - 1):
            quiz.score += 1
#--------------------------------------------------
def clear_quizzes_data():
    for quiz in quizzes:
        quiz.score = 0

#--------------------------------------------------
def start_user_quiz_app():

    # load data from the json file
    quizzes_data = load_data_from_json_file('quiz.json')

    # add quizzes to quizzes list
    extract_quizzes(quizzes_data)

    while True:
        # clear quizzes prev data
        clear_quizzes_data()

        # show quizzes choices
        display_quizzes_options()

        # get the choice from the user
        option = int(input('>> Please Select an option or press -1 to exit: '))
            # check if the option is not valid
        if option > len(quizzes):
            print(f'>> ERROR: Please select a valid option')
            continue
        elif option == -1:
            print('Good Luck, See You next time')
            exit(1)

        # start the quiz
        start_quiz(option - 1)

        # display the score
        print("*"*15)
        print(f'>> YOUR SCORE = {quizzes[option - 1].score} out of {len(quizzes[option - 1].questions)}')
        print("*"*15)


if __name__ == '__main__':
    start_user_quiz_app()