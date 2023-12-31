import os
os.system("cls")

def Task16():
    
    print("Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X\n\t*Пример:* \n\t5 \n\t1 2 3 4 5\n\t3\n\t-> 1")
    
    n = int(input("Введите кол-во элементов в массиве: "))
    import random
    list_1 = [random.randint(1, 5) for i in range(n)]
    print("Массив: ", list_1)
    count = 0
    x = int(input("цифра в массиве: "))
    for i in range(0, len(list_1)):
            if x == list_1[i]:
                count += 1
    print("Сколько раз встречается цифра {} в массиве list_1: {} раз(а)" .format(x, count))
    
#Task16()


def Task18():
    print("Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X\t\n*Пример:*\t\n5\t\n1 2 3 4 5\t\n6\t\n5")

    n = int(input("Введите кол-во элементов в массиве: "))
    import random
    list_1 = [random.randint(1, 20) for i in range(n)]
    list_1.sort()
    print("Массив: ", list_1)
    x = int(input("Задать число для поиска ближайшего в списке по значению: "))
    min = abs(x - list_1[0])
    index = 0
    for i in range(1, n):
        count = abs(x - list_1[i])
        if count < min:
            min = count
            index = i
    print(f'Число {list_1[index]} близкое по значению числу {x}')
    
#Task18()    
    

def Task20():
    print("Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. \nВ случае с английским алфавитом очки распределяются так:\nA, E, I, O, U, L, N, S, T, R – 1 очко; \nD, G – 2 очка; \nB, C, M, P – 3 очка; \nF, H, V, W, Y – 4 очка; \nK – 5 очков; \nJ, X – 8 очков; \nQ, Z – 10 очков. \nА русские буквы оцениваются так: \nА, В, Е, И, Н, О, Р, С, Т – 1 очко; \nД, К, Л, М, П, У – 2 очка; \nБ, Г, Ё, Ь, Я – 3 очка; \nЙ, Ы – 4 очка;\nЖ, З, Х, Ц, Ч – 5 очков; \nШ, Э, Ю – 8 очков; \nФ, Щ, Ъ – 10 очков. \n\tНапишите программу, которая вычисляет стоимость введенного пользователем слова. Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.\n\t*Пример: \n\tноутбук = 12")

    eng = 'qwertyuiopasdfghjklzxcvbnm'
    rus = 'йцукенгшщзхъфывапролджэячсмитьбюё'

    scrabble_eng = {
        1: 'AEIOULNSTR',
        2: 'DG',
        3: 'BCMP',
        4: 'FHVWY',
        5: 'K',
        8: 'JX',
        10: 'QZ'    
    }
    scrabble_rus = {
        1: 'АВЕИНОРСТ',
        2: 'ДКЛМПУ',
        3: 'БГЁЬЯ',
        4: 'ЙЫ',
        5: 'ЖЗХЦЧ',
        8: 'ШЭЮ',
        10: 'ФЩЪ'  
    }
    word = input('Введите слово на русском или английском языке: ')

    if word[0].lower() in eng:
        summa = 0
        for text in word:
            for k, v in scrabble_eng.items():
                if text.upper() in v:
                    summa += k
        print(f"Количество очков во введенном английском слове = {summa}")
    else: 
        if word[0].lower() in rus:
            summa = 0
            for text in word:
                for k, v in scrabble_rus.items():
                    if text.upper() in v:
                        summa += k
        print(f"Количество очков во введенном русском слове = {summa}")
        
#Task20()                            