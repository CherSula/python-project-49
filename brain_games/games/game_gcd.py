#!/usr/bin/env python3
import prompt
from random import randint
from math import gcd


def start_round():
    gen_number1 = randint(1, 100)
    gen_number2 = randint(1, 100)
    correct_answer = gcd(gen_number1, gen_number2)
    answer = int(prompt.string(
        f'Question: {gen_number1}, {gen_number2}\n'
        f'Your answer: '))  # type: ignore
    if answer == correct_answer:
        return 1, answer, correct_answer
    else:
        return 0, answer, correct_answer
