#!/usr/bin/env python3
import prompt
from brain_games.scripts.games import brain_even, brain_calc


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name

def what_game():
    game_to_play = prompt.string('What game do you want to play? ')
    return game_to_play


def game(game_to_play):
    result = 0
    if game_to_play == 'brain-even':
        result = brain_even.game_brain_even()
    elif game_to_play == 'brain-calc':
        result = brain_calc.game_brain_calc()
    return result

def game_result(result, name):
    if result == 3:
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")

def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    game_to_play = what_game()
    result = game(game_to_play)
    game_result(result, name)


if __name__ == '__main__':
    main()