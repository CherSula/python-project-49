#!/usr/bin/env python3
from brain_games import game_engine
from brain_games.games import game_calc


def main():
    number_of_rounds = 3
    points_to_win = 3
    name = game_engine.welcome_user()
    print('What is the result of the expression?')
    result = game_engine.start_game_loop(
        number_of_rounds,
        game_calc.start_round
    )
    game_engine.show_game_result(result, points_to_win, name)


if __name__ == '__main__':
    main()
