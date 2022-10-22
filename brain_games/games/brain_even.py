#!/usr/bin/env python3
from brain_games.cli import greeting
from brain_games.scripts.unils import get_random_number
import prompt


def get_parity(number):
    if number % 2 == 0:
        return 'yes'
    return 'no'


def main():
    username = greeting()
    print('Answer "yes" if the number is even, otherwise answer "no"')
    count_correct = 3
    while count_correct > 0:
        hidden_number = get_random_number()
        answer = get_parity(hidden_number)
        print(f'Question: {hidden_number}')
        user_answer = prompt.string('Your answer: ')
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
