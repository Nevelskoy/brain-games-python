#!/usr/bin/env python3
from brain_games.cli import welcome_user
from random import randint
import prompt


def get_random_number():
    return randint(1, 100)


def get_parity(number):
    if number % 2 == 0:
        return 'yes'
    return 'no'


def main():
    print('Answer "yes" if the number is even, otherwise answer "no"')
    correct_answer = 3
    username = welcome_user()
    while correct_answer > 0:
        hidden_number = get_random_number()
        parity = get_parity(hidden_number)
        print(f'Question: {hidden_number}')
        answer = prompt.string('Your answer: ')
        if answer == parity:
            print('Correct!')
            correct_answer -= 1
        else: 
            print(f'"{answer}" is wrong answer ;(. Correct answer was "{parity}"')
            print(f"Let's try again, {username}!")
            correct_answer = 3
    print(f'Congratulations, {username}!')


if __name__ == '__main__':
    main()
