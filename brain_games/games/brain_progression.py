#!/usr/bin/env python3
from brain_games.scripts.utils import get_random_number


DESCRIPTION = 'What number is missing in the progression?'


def get_progression():
    '''
    l = []
    start = 1
    step = 5
    while len(l) < 10:
        start += step
        l.append(start)
    res = ''
    for num in l:
        res += f' {str(num)}'
    print(l)
    print(res)
    '''


def make_question():
    start = get_random_number()
    step = get_random_number(1, 10)
    question = get_progression()
    correct_answer = get_progression()
    return question, correct_answer