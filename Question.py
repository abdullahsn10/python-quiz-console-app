class Question:
    """
    This is the class for a Question object
    instance variables:
        question_text - the text of the question
        options - a list of options for the question
        answer - the answer to the question
    """

    def __init__(self, question_text: str, options: list, answer: str):
        self.question_text = question_text
        self.options = options
        self.answer = answer

    def is_correct_answer(self, answer_index: int) -> bool:
        """
        This function used to check if a given answer index equals the correct answer index
        in the options list
        Args:
            answer_index (int): the index of the answer to be checked
        Return:
            bool: True if the answer is correct, False otherwise
        """
        if self.options[answer_index] == self.answer:
            return True
        return False

    def __str__(self):
        options_text = ""
        for i in range(len(self.options)):
            options_text += f'{i+1}.  ' + self.options[i] + "\n"
        return f'{self.question_text} \nOptions:\n{options_text}\n-----'
