#!/usr/bin/env python3
from brain_games.cli import greeting
from brain_games.scripts.unils import get_random_number
import prompt


def get_operator():
    operators = ["+", "-", "*"]
    sign = get_random_number(0,2)
    return operators[sign]


def calculating(first, second, operator):
    if operator == '+':
        return first + second
    elif operator == '-':
        return first - second
    else: return first * second


def main():
    username = greeting()
    print('Answer "yes" if the number is even, otherwise answer "no"')
    count_correct = 3
    while count_correct > 0:
        first = get_random_number()
        second = get_random_number()
        operator = get_operator()
        answer = calculating(first, second, operator)
        print(f'Question: {first} {operator} {second}')
        user_answer = int(prompt.string('Your answer: '))
        if answer == user_answer:
            print('Correct!')
            count_correct -= 1
        else:
            print(f'"{answer}" is wrong answer ;(. Correct answer was "{answer}"')
            print(f"Let's try again, {username}!")
            count_correct = 3
    print(f'Congratulations, {username}!')


if __name__ == '__main__':
    main()