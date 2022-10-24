from brain_games.cli import greeting_user, get_user_answer


ROUNDS = 3

#TODO: need username?! ask only once?
def run(game=None):
    username = greeting_user()
    if game:
        engine(game, username)

#TODO: improve logic
def engine(game, username):
    print(game.DESCRIPTION)
    completed_round = 0
    while ROUNDS > completed_round:
        question, correct_answer = game.make_question()
        print(f'Question: {question}')
        answer = get_user_answer()
        if answer == correct_answer:
            print('Correct!')
            completed_round += 1
        else:
            print(f'"{answer}" is wrong answer ;(. Correct answer was "{correct_answer}"')
            completed_round = 0
            print(f"Let's try again, {username}!")
    print(f'Congratulations, {username}!')
