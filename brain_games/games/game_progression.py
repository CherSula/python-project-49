import prompt
from random import randint, choice


def start_round():
    first_number = randint(1, 10)
    increment = randint(1, 10)
    prog_len = randint(5, 10)
    progression_list = progression(first_number, increment, prog_len)
    hidden_number = choice(progression_list)
    answer = int(prompt.string(
        f'Question: {hide_item(progression_list, hidden_number)}\n'
        f'Your answer: '))  # type: ignore
    if answer == hidden_number:
        return 1, answer, hidden_number
    else:
        return 0, answer, hidden_number


def progression(first_number, increment, prog_len):
    current = first_number
    progression_list = [current]
    for _ in range(prog_len - 1):
        current += increment
        progression_list.append(current)
    return progression_list


def hide_item(progression_list, hidden_number):
    hide_symbol = '..'
    final_str = ''
    for number in progression_list:
        if number == hidden_number:
            final_str += hide_symbol + ' '
        else:
            final_str += f'{number} '
    return final_str.strip()


if __name__ == '__main__':
    assert progression(1, 3, 10) == [1, 4, 7, 10, 13, 16, 19, 22, 25, 28]
    assert progression(5, 3, 10) == [5, 8, 11, 14, 17, 20, 23, 26, 29, 32]
    assert progression(1, 5, 10) == [1, 6, 11, 16, 21, 26, 31, 36, 41, 46]
    assert progression(1, 3, 5) == [1, 4, 7, 10, 13]

    assert hide_item(progression(1, 3, 10), 16) == '1 4 7 10 13 .. 19 22 25 28'

    print(start_round())
