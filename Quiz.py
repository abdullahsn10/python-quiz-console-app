class Quiz:
    """
    This is the class for a Quiz object
    instance variables:
        name - the name of the Quiz
        questions - the list of questions in the quiz
    """

    def __init__(self, name, questions):
        self.name = name
        self.questions = questions
        self.score = 0

    def get_name(self):
        return self.name

    def get_questions(self):
        return self.questions

    def get_score(self):
        return self.score

    def set_score(self, score):
        self.score = score

    def __str__(self):
        return f'{self.name}: {self.score}'