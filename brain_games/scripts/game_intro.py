#!/usr/bin/env python3
import prompt
from brain_games.scripts.games import brain_even, brain_calc, brain_gcd


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def what_game():
    game_to_play = prompt.string('What game do you want to play? ')
    return game_to_play


def start_game_loop(number_of_rounds, start_round_func):
    result = 0
    for _ in range(number_of_rounds):
        round_result = start_round_func()
        if round_result == 0:
            break
        print('Correct!')
        result += 1
    return result


def game(game_to_play, number_of_rounds):
    result = 0
    if game_to_play == 'brain-even':
        result = start_game_loop(number_of_rounds, brain_even.start_round)
    elif game_to_play == 'brain-calc':
        result = start_game_loop(number_of_rounds, brain_calc.start_round)
    elif game_to_play == 'brain-gcd':
        result = start_game_loop(number_of_rounds, brain_gcd.start_round)
    return result


def show_game_result(result, points_to_win, name):
    if result == points_to_win:
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")


def main():
    number_of_rounds = 3
    points_to_win = 3
    print('Welcome to the Brain Games!')
    name = welcome_user()
    game_to_play = what_game()
    result = game(game_to_play, number_of_rounds)
    show_game_result(result, points_to_win, name)


if __name__ == '__main__':
    main()
