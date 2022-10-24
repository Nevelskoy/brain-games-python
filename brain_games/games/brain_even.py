#!/usr/bin/env python3
from brain_games.scripts.utils import get_random_number


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no"'


def get_parity(number):
    if number % 2 == 0:
        return 'yes'
    return 'no'


def make_question():
    number = get_random_number()
    correct_answer = get_parity(number)
    return number, correct_answer
