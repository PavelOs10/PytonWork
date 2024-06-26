# Задача №19. Решение в группах
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

def shift(lst, k):
    n = len(lst) 
    k = k % n  
    return lst[-k+1:] + lst[:-k+1] if k != 0 else lst


input_list = [1, 2, 3, 4, 5]
k = 101
output_list = shift(input_list, k)
print(output_list)
# определяем длинну списка
# если когда k больше длины списка
# возвращем список состоящий из последних К элементов 
# и все остальные элементы до последних К 
# (+1 почему, без него результат [3, 4, 5, 1, 2])