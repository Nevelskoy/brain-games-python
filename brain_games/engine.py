from brain_games.cli import greeting_user, get_user_answer


ROUNDS = 3


def run(game=None):
    username = greeting_user()
    if game:
        print(game.DESCRIPTION)
        engine(game, username)


def engine(game, username):
    completed_round = 0
    while ROUNDS > completed_round:
        question, correct_answer = game.make_question()
        print(f'Question: {question}')
        answer = get_user_answer()
        if answer == correct_answer:
            print('Correct!')
            completed_round += 1
        else:
            print(f'"{answer}" is wrong answer ;(. \
                 Correct answer was "{correct_answer}"')
            return print(f"Let's try again, {username}!")
    return print(f'Congratulations, {username}!')
