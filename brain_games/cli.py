import prompt


def greeting_user():
    print('Welcome to the Brain Games!')
    username = prompt.string('May I have your name? ')
    print(f'Hello, {username}!')
    return username


def get_user_answer():
    return prompt.string('Your answer: ')
