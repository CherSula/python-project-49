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
        correct_answer = gen_number1 + gen_number2
        if answer == correct_answer:
            return 1, answer, correct_answer
        else:
            return 0, answer, correct_answer
    if operator == '-':
        correct_answer = gen_number1 - gen_number2
        if answer == correct_answer:
            return 1, answer, correct_answer
        else:
            return 0, answer, correct_answer
    if operator == '*':
        correct_answer = gen_number1 * gen_number2
        if answer == correct_answer:
            return 1, answer, correct_answer
        else:
            return 0, answer, correct_answer
