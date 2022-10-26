from brain_games.scripts.utils import get_random_number


DESCRIPTION = 'What number is missing in the progression?'
LENGTH_PROGRESSION = 10


def get_progression_crux(progression):
    progression_crux = ''
    hidden_index = get_random_number(1, LENGTH_PROGRESSION - 1)
    hidden_num = str(progression[hidden_index])
    progression[hidden_index] = '..'
    for item in progression:
        progression_crux += f' {str(item)}'
    return progression_crux, hidden_num


def get_progression(start, step):
    progression = []
    while len(progression) < LENGTH_PROGRESSION:
        start += step
        progression.append(start)
    return progression


def make_question():
    start = get_random_number()
    step = get_random_number(1, LENGTH_PROGRESSION)
    question, correct_answer = get_progression_crux(get_progression(start, step))
    return question, correct_answer