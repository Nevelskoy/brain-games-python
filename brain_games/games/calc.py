#!/usr/bin/env python3
from brain_games.scripts.utils import get_random_number


DESCRIPTION = 'What is the result of the expression?'


def get_operator():
    operators = ["+", "-", "*"]
    sign = get_random_number(0, 2)
    return operators[sign]


def calculating(first, second, operator):
    if operator == '+':
        return first + second
    elif operator == '-':
        return first - second
    else:
        return first * second


def make_question():
    first = get_random_number()
    second = get_random_number()
    operator = get_operator()
    question = f'{first} {operator} {second}'
    correct_answer = str(calculating(first, second, operator))
    return question, correct_answer
