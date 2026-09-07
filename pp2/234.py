import random

print("🎮 Игра: Угадай число!")
print("Я загадал число от 1 до 100.")

secret = random.randint(1, 100)
attempts = 0

while True:
    try:
        number = int(input("Твоя попытка: "))
        attempts += 1

        if number < secret:
            print("📈 Загаданное число больше!")
        elif number > secret:
            print("📉 Загаданное число меньше!")
        else:
            print(f"🎉 Ты угадал!")
            print(f"Число: {secret}")
            print(f"Попыток: {attempts}")
            break

    except ValueError:
        print("❌ Введи целое число!")

print("Спасибо за игру! 👋")
