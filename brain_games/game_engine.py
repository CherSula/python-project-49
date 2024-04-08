import prompt

ROUNDS = 3


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def run(game):
    name = welcome_user()
    print(game.DESCRIPTION)

    for _ in range(ROUNDS):
        question, correct_answer = game.generate_round()
        print(f'Question: {question}')
        user_answer = input('Your answer: ')
        if user_answer != correct_answer:
            print(
                f'"{user_answer}" is wrong answer ;(.'
                f'Correct answer was "{correct_answer}".\n'
                f"Let's try again, {name}!"
            )
            break
        print('Correct!')
    else:
        print(f'Congratulations, {name}!')
