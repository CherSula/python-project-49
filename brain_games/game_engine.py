#!/usr/bin/env python3
import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def start_game_loop(number_of_rounds, start_round_func):
    result = 0
    for _ in range(number_of_rounds):
        round_result, answer, correct_answer = start_round_func()
        if round_result == 0:
            print(
                f'"{answer}" is wrong answer ;(.'
                f'Correct answer was "{correct_answer}".'
            )
            break
        print('Correct!')
        result += 1
    return result


def show_game_result(result, points_to_win, name):
    if result == points_to_win:
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")
