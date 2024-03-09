#!/usr/bin/env python3
import prompt
from random import randint


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def game_brain_even():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    result = 0
    for _ in range(3):
        gen_number = randint(1, 100)
        answer = prompt.string(f'Question: {gen_number}\nYour answer: ')
        if answer == 'yes':
            if gen_number%2 == 0:
                print('Correct!')
                result += 1
            else:
                print(f'"{answer}" is wrong answer ;(. Correct answer was "no".')
                break
        elif answer == 'no':
            if gen_number%2 != 0:
                print('Correct!')
                result += 1
            else:
                print(f'"{answer}" is wrong answer ;(. Correct answer was "yes".')
                break
        else:
            print(f"'{answer}' is wrong answer ;(.")
            break
    return result

def game_result(result, name):
    if result == 3:
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")

def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    result = game_brain_even()
    game_result(result, name)


if __name__ == '__main__':
    main()