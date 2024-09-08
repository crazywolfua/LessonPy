def count_sum(count, param):
    result = 0
    if param == "even":
        for i in range(0, count + 1, 2):
            result += i
    if param == "odd":
        for i in range(1, count + 1, 2):
            result += i
    print(result)

count = int(input("Введите число: "))
param = input("Введите значение: ")

count_sum(count, param)
