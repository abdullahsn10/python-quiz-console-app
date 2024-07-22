class Question:
    '''
    This is the class for a quiz object, it has many fields:
        - quiz name
        - quiz questions as list of objects
    '''

    def __init__(self, question_text, options, answer):
        self.question_text = question_text
        self.options = options
        self.answer = answer

    def is_correct_answer(self, answer_index):
        if self.options[answer_index] == self.answer:
            return True
        return False

    def __str__(self):
        options_text = ""
        for i in range(len(self.options)):
            options_text += f'{i+1}.  ' + self.options[i] + "\n"
        return f'{self.question_text} \nOptions:\n{options_text}\n-----'
