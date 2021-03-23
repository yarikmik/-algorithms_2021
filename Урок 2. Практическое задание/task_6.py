import random

"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Подсказка:
Базовый случай здесь - угадали число или закончились попытки
"""


def quiz(num, r_count):
    user_answer = int(input('Введите свой вариант: '))
    if user_answer == num:
        return print('Игра закончена, игрок угадал!!!')
    elif r_count == 1:
        return print(f'Попытки закончились, игрок проиграл(((, правильный ответ - {num}')
    elif user_answer > num:
        print(f'Число меньше чем {user_answer}')
        return quiz(num, r_count - 1)
    elif user_answer < num:
        print(f'Число больше чем {user_answer}')
        return quiz(num, r_count - 1)


num = random.randint(1, 100)  # Генерация случайного числа
r_count = 5  # Колличество попыток
quiz(num, r_count)
