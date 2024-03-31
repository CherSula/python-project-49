#!/usr/bin/env python3
import prompt
from random import randint


def start_round():
    gen_number = randint(1, 100)
    answer = prompt.string(f'Question: {gen_number}\nYour answer: ')
    if answer == 'yes':
        if gen_number % 2 == 0:
            correct_answer = "yes"
            return 1, answer, correct_answer
        else:
            correct_answer = "no"
            return 0, answer, correct_answer
    elif answer == 'no':
        if gen_number % 2 != 0:
            correct_answer = "no"
            return 1, answer, correct_answer
        else:
            correct_answer = "yes"
            return 0, answer, correct_answer
