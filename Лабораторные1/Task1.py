numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
summ = 0
length = len(numbers)
for i in numbers:
    if i is not None:
        summ += i
for i in range(length):
    if numbers[i] is None:
        numbers[i] = summ / length
print("Измененный список:", numbers)
