#!/usr/bin/env python3
import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def run(game):
    number_of_rounds = 3

    name = welcome_user()
    print(game.DESCRIPTION)

    for _ in range(number_of_rounds):
        question, correct_answer = game.generate_round()
        print(question)
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
