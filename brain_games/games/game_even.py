from random import randint

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_round():
    gen_number = randint(1, 100)
    question = gen_number

    if gen_number % 2 == 0:
        correct_answer = "yes"
    else:
        correct_answer = "no"
    return question, str(correct_answer)
