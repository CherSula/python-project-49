import prompt
from random import randint


def start_round():
    gen_number = randint(1, 100)
    answer = prompt.string(f'Question: {gen_number}\nYour answer: ')
    if answer == 'yes':
        if (gen_number != 1
                and gen_number % gen_number == 0
                and gen_number % 1 == gen_number):
            return 1
        else:
            print(f'"{answer}" is wrong answer ;(. Correct answer was "no".')
            return 0
    elif answer == 'no':
        if (gen_number == 1
                or gen_number % gen_number != 0
                or gen_number % 1 != gen_number):
            return 1
        else:
            print(f'"{answer}" is wrong answer ;(. Correct answer was "yes".')
            return 0
    else:
        print(f'"{answer}" is wrong answer ;(.')
    return 0
