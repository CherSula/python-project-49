#!/usr/bin/env python3
import prompt
from random import randint, choice


def start_round():
    # при выигрыше функция вернет 1, при проигрыше 0
    gen_number1 = randint(1, 100)
    gen_number2 = randint(1, 100)
    operator = choice(('+', '-', '*'))
    answer = int(prompt.string(f'Question: '
                               f'{gen_number1} {operator} {gen_number2}\n'
                               f'Your answer: '))  # type: ignore
    if operator == '+':
        sum = gen_number1 + gen_number2
        if answer == sum:
            return 1
        else:
            print(f'"{answer}" is wrong answer ;(.'
                  f'Correct answer was "{sum}".')
            return 0
    if operator == '-':
        difference = gen_number1 - gen_number2
        if answer == difference:
            return 1
        else:
            print(f'"{answer}" is wrong answer ;(.'
                  f'Correct answer was "{difference}".')
            return 0
    if operator == '*':
        multiplyed = gen_number1 * gen_number2
        if answer == multiplyed:
            return 1
        else:
            print(f'"{answer}" is wrong answer ;(.'
                  f'Correct answer was "{multiplyed}".')
            return 0
    return 0
