from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_round():
    gen_number = randint(1, 100)
    question = gen_number
    if is_prime(gen_number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer


def is_prime(number):
    if number == 1:
        return False
    deviders = 0
    for n in range(2, number // 2 + 1):
        if number % n == 0:
            deviders += 1
    if deviders <= 0:
        return True
    else:
        return False
