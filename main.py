import random
import time

def arithmetic_question():
    """Генерация арифметической задачи"""
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*'])
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2
    question = f"Решите: {num1} {operator} {num2} = "
    return question, answer

def validate_input(user_input):
    """Проверка ввода пользователя"""
    try:
        int(user_input)
        return True
    except ValueError:
        return False

def play_game():
    """Игра"""
    current_room = 1
    time_limit = 600  # 10 минут в секундах
    start_time = time.time()

    while current_room <= 3:
        if time.time() - start_time > time_limit:
            print("Время вышло! Вы проиграли.")
            return

        print(f"Вы находитесь в комнате №{current_room}")
        door = int(input("Выберите дверь (1, 2 или 3): "))

        if door not in [1, 2, 3]:
            print("Некорректный выбор двери.")
            continue

        question, answer = arithmetic_question()
        attempts = 3

        while attempts > 0:
            print(question)
            user_answer = input("Введите ответ: ")

            if not validate_input(user_answer):
                print("Некорректный ввод.")
                continue

            if int(user_answer) == answer:
                print("Правильно!")
                break
            else:
                attempts -= 1
                if attempts > 0:
                    print(f"Неправильно. У вас осталось {attempts} попыток.")
                else:
                    print("У вас закончились попытки. Вы проиграли.")
                    return

        if random.choice([True, False]):
            if current_room == 3:
                print(f"Вы успешно завершили игру за {time_limit // 60} минут {time_limit % 60} секунд.")
                return
            else:
                print(f"Вы успешно перешли в комнату №{current_room + 1}")
                current_room += 1
        else:
            if current_room == 3:
                print("Вы неудачно выбрали дверь и остались в комнате №3.")
            else:
                print("Вы неудачно выбрали дверь и вернулись в комнату №1.")
                current_room = 1
                start_time -= 60  # Уменьшаем время на 1 минуту

        if current_room == 3:
            print("Вы на последнем этапе. У вас осталось:")
        else:
            remaining_time = time_limit - (time.time() - start_time)
            print(f"Осталось времени: {int(remaining_time) // 60} минут {int(remaining_time) % 60} секунд.")

play_game()