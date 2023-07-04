from os import system
from random import randint

print(
     "Какую задачу смотрим: введите порядковый номер задачи или введите 0 чтобы посмотреть все"
 )
task_number = int(input("Укажите порядковый номер задачи, которую будем смотреть "))

if task_number == 1 or task_number == 0:
    
    print("Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.\n Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d. \n Каждое число вводится с новой строки. \nВвод: 7 2 5 \nВывод: 7 9 11 13 15")
    
    n_min = int(input("Введите минимальное значение списка: "))
    step = int(input("Шаг элементов в списке: "))
    count_i = int(input("Введите кол-во элементов в списке: "))
    list_1 = []
    for i in range(count_i):
        i = n_min
        n_min += step
        list_1.append(i)
    print(*list_1)
    
    input("Нажмите Enter что бы продолжить ")
    system("cls")
    
def get_list(number, min_value, max_value):
    list_1 = []
    for i in range(number):
        i = int(randint(min_value, max_value))
        list_1.append(i)
    return list_1

if task_number == 2 or task_number == 0:
    
    print("Задача 32: \nОпределить индексы элементов массива (списка),значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума) \nВвод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7] \nВывод: [1, 9, 13, 14, 19]")

    list_32 = get_list(
        int(input("Укажите количество чисел в списке ")),
        int(input("Укажите минимальное значение ")),
        int(input("Укажите максимальное значение ")))
    print(list_32)
    list_32_2 = [i for i in list_32[:] if i >= 0]
    list_32_2.sort()
    print(list_32_2)
    
