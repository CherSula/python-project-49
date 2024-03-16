import prompt
from random import randint


def start_round():
    gen_number = randint(1, 100)
    answer = prompt.string(f'Question: {gen_number}\nYour answer: ')
    if answer == 'yes':
        if gen_number > 1:
            deviders = 0
            for number in range(2, gen_number // 2 + 1):
                if (gen_number % number == 0):
                    deviders += 1
            if (deviders <= 0):
                return 1
            else:
                print(f'"{answer}" is wrong answer ;(. Correct answer was "no".')
                return 0
    elif answer == 'no':
        deviders = 0
        for number in range(2, gen_number // 2 + 1):
            if (gen_number % number == 0):
                deviders += 1
        if (deviders > 0):
                    return 1
        elif gen_number == 1:
            return 1
        else:
            print(f'"{answer}" is wrong answer ;(. Correct answer was "yes".')
            return 0
    else:
        print(f'"{answer}" is wrong answer ;(.')
    return 0
