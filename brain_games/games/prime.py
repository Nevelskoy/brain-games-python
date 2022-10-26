from brain_games.scripts.utils import get_random_number


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_Prime(number):
    if number <= 1: return False
    for i in range(2, number - 1):
        if number % i == 0:
            return False
    return True


def make_question():
    question = get_random_number()
    correct_answer = 'yes' if is_Prime(question) else 'no'
    return question, correct_answer
