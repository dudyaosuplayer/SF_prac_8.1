"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def custon_predict(number: int = 1) -> int:
    """Функция для угадывания числа менее чем за 20 попыток в среднем.
    Результат: в среднем угадывает числа за 7 попытко.

    Args:
        number (int, optional): число, которое нужно угадать. Defaults to 1.

    Returns:
        int: кол-во попыток затраченное на угадывание числа
    """
    np.random.seed(2)
    count = 0

    predict_number = 50

    while number != predict_number:
        count += 1

        if number > predict_number:
            predict_number += 25
            while number != predict_number:
                count += 1
                if number > predict_number:
                    predict_number += 1

                elif number < predict_number:
                    predict_number -= 1

        elif number < predict_number:
            count += 1
            predict_number -= 25
            while number != predict_number:
                if number > predict_number:
                    predict_number += 1

                elif number < predict_number:
                    predict_number -= 1

    return count


def score_game(custon_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(custon_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(custon_predict)
