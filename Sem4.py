# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()

# def track_characters(input_string):
#     # Разделяем входную строку на символы
#     characters = input_string.split()
    
#     # Создаем словарь для отслеживания количества появлений каждого символа
#     occurrences = {}
    
#     # Создаем список для хранения результатов
#     result = []
    
#     for char in characters:
#         if char in occurrences:
#             occurrences[char] += 1
#             result.append(f"{char}_{occurrences[char]}")
#         else:
#             occurrences[char] = 0
#             result.append(char)
    
#     return " ".join(result)

# input_string = "a a a b c a a d c d d"
# output_string = track_characters(input_string)
# print(output_string)


# Задача №27. Решение в группах
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13

def count_unique_words(text):
    # Разделяем текст на слова, используя метод split(), который по умолчанию разбивает по пробелам
    words = text.split()
    
    # Используем множество для хранения уникальных слов
    unique_words = set(words)
    
    # Возвращаем количество уникальных слов
    return len(unique_words)

# Пример использования
input_text = """She sells sea shells on the sea shore The shells
that she sells are sea shells I'm sure.So if she sells sea
shells on the sea shore I'm sure that the shells are sea
shore shells"""

output_count = count_unique_words(input_text)
print(output_count)

# Задача №29. Решение в группах
# Ваня и Петя поспорили, кто быстрее решит
# следующую задачу: “Задана последовательность
# неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в
# последовательность)”. Однако 2 друга оказались не
# такими смышлеными. Никто из ребят не смог до
# конца сделать это задание. Они решили так: у кого
# будет меньше ошибок в коде, тот и выиграл спор. За
# помощью товарищи обратились к Вам, студентам.
# Примечание: Программные коды на следующих
# слайдах
# 30 минут
# Семинар 4. Словари, множества и профилирование
# Задача №29. Решение в группах
# Ваня:
# n = int(input())
# max_number = 1000
# while n != 0:
# n = int(input())
# if max_number > n:
# max_number = n
# print(max_number)
# Петя:
# n = int(input())
# max_number = -1
# while n < 0:
# n = int(input())
# if max_number < n:
# n = max_number
# print(n)


# Код Вани
# Ошибки:

# Переменная max_number инициализируется значением 1000, что не имеет смысла, так как последовательность может содержать числа меньше 1000.
# Внутри цикла условие if max_number > n: перепутано. Нужно искать максимальное значение, а не минимальное.
# Исправленный код Вани:

n = int(input("Введите число: "))
max_number = -1  # Инициализируем переменную значением, которое меньше любого неотрицательного числа

while n != 0:
    if n > max_number:
        max_number = n
    n = int(input("Введите число: "))

print("Наибольший элемент последовательности:", max_number)

# Код Пети
# Ошибки:

# Цикл while n < 0 никогда не выполнится, так как вводится неотрицательное число.
# Внутри цикла переменная max_number должна обновляться значением n, а не наоборот.
# Необходимо обновлять значение n внутри цикла.
# Исправленный код Пети:


n = int(input("Введите число: "))
max_number = -1  # Инициализируем переменную значением, которое меньше любого неотрицательного числа

while n != 0:
    if n > max_number:
        max_number = n
    n = int(input("Введите число: "))

print("Наибольший элемент последовательности:", max_number)