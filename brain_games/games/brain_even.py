#!/usr/bin/env python3
from brain_games.cli import greeting_user
from brain_games.scripts.utils import get_random_number


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no"'

hidden_number = get_random_number()

def get_parity(number):
    if number % 2 == 0:
        return 'yes'
    return 'no'

def make_question():
    return hidden_number

def correct_answer(number):
    return get_parity(number)
