#!/usr/bin/env python3
import prompt
from random import randint
from math import gcd


def start_round():
    gen_number1 = randint(1, 100)
    gen_number2 = randint(1, 100)
    nod = gcd(gen_number1, gen_number2)
    print('Find the greatest common divisor of given numbers.')
    answer = int(prompt.string(
        f'Question: {gen_number1}, {gen_number2}\n'
        f'Your answer: '))  # type: ignore
    if answer == nod:
        return 1
    else:
        print(f'"{answer}" is wrong answer ;(. Correct answer was "{nod}".')
        return 0
