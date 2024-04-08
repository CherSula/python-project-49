from random import randint, choice

DESCRIPTION = 'What is the result of the expression?'


def generate_round():
    gen_number1 = randint(1, 100)
    gen_number2 = randint(1, 100)
    operator = choice(('+', '-', '*'))

    question = f'{gen_number1} {operator} {gen_number2}'

    if operator == '+':
        correct_answer = gen_number1 + gen_number2
    if operator == '-':
        correct_answer = gen_number1 - gen_number2
    if operator == '*':
        correct_answer = gen_number1 * gen_number2

    return question, str(correct_answer)
