#!/usr/bin/env python3
import prompt
import random
from random import randint


def game_brain_calc():
    result = 0
    for _ in range(3):
        round_result = start_round()
        if round_result == 0:
            break
        print('Correct!')
        result += 1
    return result


def start_round():
    '''при выигрыше функция вернет 1, при проигрыше 0'''
    gen_number1 = randint(1, 100)
    gen_number2 = randint(1, 100)
    operator = random.choice(('+', '-', '*'))
    answer = int(prompt.string(f'Question: {gen_number1} {operator} {gen_number2}\nYour answer: '))  # type: ignore (это игрушка дьявола!)
    if operator == '+':
        sum = gen_number1 + gen_number2
        if answer == sum:
            return 1
        else:
            print(f'"{answer}" is wrong answer ;(. Correct answer was "{sum}".')
            return 0
    if operator == '-':
        difference = gen_number1 - gen_number2
        if answer == difference:
            return 1
        else:
            print(f'"{answer}" is wrong answer ;(. Correct answer was "{difference}".')
            return 0
    if operator == '*':
        multiplyed = gen_number1 * gen_number2
        if answer == multiplyed:
            return 1
        else:
            print(f'"{answer}" is wrong answer ;(. Correct answer was "{multiplyed}".')
            return 0
    return 0

def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def game_result(result, name):
    if result == 3:
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    result = game_brain_calc()
    game_result(result, name)


if __name__ == '__main__':

    main()
