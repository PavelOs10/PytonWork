# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

# lists = [1, 1, 2, 0, -1, 3, 4, 4]
# unique_numbers = set(lists)  
# count = len(unique_numbers)  
# print(count)


def count_unique_num(numbers):

    unique_numbers = []
    for number in numbers:
        if number not in unique_numbers:
            unique_numbers.append(number)
    return len(unique_numbers)

lists = [1, 1, 2, 0, -1, 3, 4, 4]
output = count_unique_num(lists)
print(output)