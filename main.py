import random
import sys

user_name = input("Введите своё имя: ")

if user_name.isalpha():
    print("Имя указано верно!")
else:
    exit("Не верно указано имя")

random_number = random.randint(1, 5)

user_number = int(input("Угадай число (от 1 до 5): "))

if user_number == random_number:
    print(f"{user_name} вы большой молодец, вы угадали!!!")
    print(f"Число было: {random_number}")

elif user_number != random_number:
    print(f'Увы, {user_name} вы не угадали :(')
    print(f"Число было: {random_number}")


exit("Игра окончена!!!!")
