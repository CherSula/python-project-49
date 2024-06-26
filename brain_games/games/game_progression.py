from random import randint, choice

DESCRIPTION = 'What number is missing in the progression?'


def generate_round():
    first_number = randint(1, 10)
    increment = randint(1, 10)
    prog_len = randint(5, 10)
    progression_list = progression(first_number, increment, prog_len)
    correct_answer = choice(progression_list)
    question = hide_item(progression_list, correct_answer)
    return question, str(correct_answer)


def progression(first_number, increment, prog_len):
    current = first_number
    progression_list = [current]
    for _ in range(prog_len - 1):
        current += increment
        progression_list.append(current)
    return progression_list


def hide_item(progression_list, hidden_number):
    hide_symbol = '..'
    symbols = []
    for number in progression_list:
        if number == hidden_number:
            symbols.append(hide_symbol)
        else:
            symbols.append(str(number))
    return ' '.join(symbols)
