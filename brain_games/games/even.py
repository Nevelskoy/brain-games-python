from brain_games.scripts.utils import get_random_number


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_parity(number):
    return 'no' if number % 2 else 'yes'


def make_question():
    question = get_random_number()
    correct_answer = get_parity(question)
    return question, correct_answer
