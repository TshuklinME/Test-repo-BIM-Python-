numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

sum_number = sum(numbers[:4]) + sum(numbers[5:])
len_number = len(numbers)

numbers[4] = sum_number / len_number

print("Измененный список:", numbers)
