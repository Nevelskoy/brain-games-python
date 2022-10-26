from brain_games.scripts.utils import get_random_number


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_gcd(first, second):
    if second == 0: return first
    return get_gcd(second, first % second) 


def make_question():
    first = get_random_number()
    second = get_random_number()
    question = f'{first} {second}'
    correct_answer = str(get_gcd(first, second))
    return question, correct_answer