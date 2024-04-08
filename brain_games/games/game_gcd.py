from random import randint
from math import gcd

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def generate_round():
    gen_number1 = randint(1, 100)
    gen_number2 = randint(1, 100)
    correct_answer = gcd(gen_number1, gen_number2)
    question = f'{gen_number1} {gen_number2}'
    return question, str(correct_answer)
