numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

before = numbers[0:4]
after = numbers[5:]
new_numbers = before + after
count_of_new_numbers = sum(new_numbers)
length = len(numbers)
average_of_numbers = count_of_new_numbers / length
numbers[4] = average_of_numbers
print("Измененный список:", numbers)
