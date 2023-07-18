""" Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке """
# def check_rhythm(poem):
#     lines = poem.split()  # Разделяем стихотворение на строки по пробелам
#     syllables_count = None  # Число слогов в предыдущей фразе

#     for line in lines:
#       words = line.split('-')  # Разделяем строку на слова по дефисам
#       syllables = sum(count_syllables(word) for word in words)  # Считаем число слогов во фразе
#       if syllables_count is None:
#         syllables_count = syllables
#       elif syllables != syllables_count:
#         return "Пам парам"
#     return "Парам пам-пам"


# def count_syllables(word):
#   vowels = "аеёиоуыэюя"  # Список гласных букв
#   count = 0
  
#   for letter in word:
#     if letter.lower() in vowels:
#       count += 1
#   return count

# poem = input("Введите стихотворение Винни-Пуха: ")
# result = check_rhythm(poem)
# print(result)

""" Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.

*Пример:*

**Ввод:** `print_operation_table(lambda x, y: x * y) ` 
**Вывод:**
1 2 3 4 5 6

2 4 6 8 10 12
3 6 9 12 15 18
4 8 12 16 20 24
5 10 15 20 25 30
6 12 18 24 30 36 """

# def print_operation_table(func, num_rows, num_columns):
#   for i in range(1 , num_rows + 1):
#     list = []
#     for j in range(1, num_columns + 1):
#       list.append(i * j)
#     print(*list)    

# print_operation_table(lambda x, y: x * y, int(input('row: ')), int(input('column: '))) 
