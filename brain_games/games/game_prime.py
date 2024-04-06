from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_round():
    gen_number = randint(1, 100)
    question = f'Question: {gen_number}'
    if gen_number == 1:
        correct_answer = 'no'
    if gen_number > 1:
        deviders = 0
        for number in range(2, gen_number // 2 + 1):
            if (gen_number % number == 0):
                deviders += 1
        if (deviders <= 0):
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
    return question, str(correct_answer)
