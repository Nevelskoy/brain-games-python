from brain_games.cli import greeting_user, get_user_answer


ROUNDS = 3

def get_question(game):
    return game.make_question()

# def check_answer(game, question):
#     return game.correct_answer(question)

def run(game=None):
    username = greeting_user()
    print(game.DESCRIPTION)
    if game:
        completed_round = 0
        while ROUNDS > completed_round:
            question = get_question(game)
            print(f'Question {question}')

            answer = get_user_answer()
            correct_answer = game.correct_answer(question)
            if answer == correct_answer:
                print('Correct!')
                completed_round += 1
            else:
                print(f'"{answer}" is wrong answer ;(. Correct answer was "{correct_answer}"')
                completed_round = 0
                print(f"Let's try again, {username}!")
        print(f'Congratulations, {username}!')


#TODO:
# 1. Сформировать в make_qustion возврат вопроса и верного ответа
# 2. Разделить логику run - выполнение основной логики игрового процесса, engine - обработка данных каждой игры
