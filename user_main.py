import json
from Quiz import *
from Question import *


def load_data_from_json_file(filename: str) -> dict:
    """
    This function used to load the data from a json file
    Args:
        filename (string): the name of the json file
    Return:
        returns the loaded json file as python dictionary
    """

    json_file = open(filename)
    data = json.load(json_file)
    json_file.close()
    return data


def is_valid_question(question: Question) -> bool:
    """
    This function used to apply simple validation on a given question
    Args:
        question: the question to be validated
    Return:
        returns True if the question is valid, otherwise False
    """

    if len(question) != 3:
        return False
    return True


def extract_quizzes(data: dict) -> list:
    """
    This function used to extract quizzes from a dictionary
    Args:
        data (dict): the dictionary to extract quizzes from
    Return:
        returns a list of extracted quizzes
    """

    quizzes = []  # list of quizzes to be returned
    for quiz, questions in data.items():
        quiz_questions = []
        for question in questions:
            if is_valid_question(question):
                question_instance = Question(question["question"],
                                             question["options"],
                                             question["answer"])
                quiz_questions.append(question_instance)

        quiz_instance = Quiz(quiz, quiz_questions)
        quizzes.append(quiz_instance)
    return quizzes


def display_quizzes_options(quizzes: list) -> None:
    """
    This function used to display options of quizzes to the user
    Args:
        quizzes (list): list of quizzes objects in the system
    Return:
        does not return anything, only display quizzes options
    """
    print('*******Welcome to Quiz App *********')
    print('Which quiz do you want to start?')
    for i in range(len(quizzes)):
        print(f'{i + 1}. {quizzes[i].name} Quiz')


def start_quiz(quiz_index: int, quizzes: list) -> None:
    """
    This function used to start the required quiz given its index in
    the quizzes list in the system
    Args:
        quiz_index (int): the index of the quiz to start
        quizzes (list): list of quizzes objects in the system
    Return:
        does not return anything, only start thq quiz
    """

    quiz = quizzes[quiz_index]
    print('*' * 10)
    print(f'Welcome to Quiz {quiz.name}')
    questions_count = 0
    for question in quiz.questions:
        questions_count += 1
        print(f'Question {questions_count}: {question}')
        while True:
            try:
                answer = int(input('>> Please Enter the number of the correct answer: '))
            except ValueError:
                print('ERROR: Invalid option!')
                continue
            if answer > 4 or answer < 1:
                print('ERROR: Invalid option!')
                continue
            break

        if question.is_correct_answer(answer - 1):
            quiz.score += 1


def clear_quizzes_data(quizzes: list) -> None:
    """
    This function used to clear the previous data from a quizzes list, by setting score =0
    Args:
        quizzes (list): list of quizzes objects in the system
    Return:
        does not return anything, only change on quizzes inside the list
    """
    for quiz in quizzes:
        quiz.score = 0


def start_user_quiz_app():
    """
    This function used to start a user quiz app
    """

    # list of quizzes
    quizzes = []

    # load data from the json file
    quizzes_data = load_data_from_json_file(filename='quiz.json')

    # add quizzes to quizzes list
    quizzes = extract_quizzes(data=quizzes_data)

    while True:
        # clear quizzes prev data
        clear_quizzes_data(quizzes=quizzes)

        # show quizzes choices
        display_quizzes_options(quizzes=quizzes)

        # get the choice from the user
        try:
            option = int(input('>> Please Select an option or press -1 to exit: '))
        except ValueError:
            print('>> Invalid option!')
            continue

        # check if the option is not valid
        if option == -1:
            print('>> Good Luck, See You next time')
            exit(1)
        elif option > len(quizzes) or option <= 0:
            print(f'>> ERROR: Please select a valid option')
            continue

        # start the quiz
        start_quiz(quiz_index=option - 1, quizzes=quizzes)

        # display the score
        print("*" * 15)
        print(f'>> YOUR SCORE = {quizzes[option - 1].score} out of {len(quizzes[option - 1].questions)}')
        print("*" * 15)


if __name__ == '__main__':
    start_user_quiz_app()
