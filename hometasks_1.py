'''
    Task 1
    Дані два цілих числа. Виведіть значення найменшого.
'''
print("____________________")
number1 = int(input("Введите первое целое число: "))
number2 = int(input("Введите второе целое число: "))
print("Task 1.1")
print(f"Наименьшее число: {min(number1, number2)}")

print("Task 1.2")
if number1 < number2:
    print(f"Наименьшее число: {number1}")
elif number1 > number2:
    print(f"Наименьшее число: {number2}")
else:
    print("Оба числа равны.")

'''
    Task 2
    Задано дві клітинки шахівниці. Якщо вони пофарбовані в один колір, 
    виведіть слово YES, а якщо в різні кольори - то NO. 
    Програма отримує на вхід чотири числа від 1 до 8 кожне, 
    що задають номер стовпця та номер рядка спочатку для першої клітини, 
    потім для другої клітини.
'''
print("____________________")
print("Task 2")
x1 = int(input("Введите номер столбца первой клетки (1-8): "))
y1 = int(input("Введите номер ряда первой клетки (1-8): "))
x2 = int(input("Введите номер столбца второй клетки (1-8): "))
y2 = int(input("Введите номер ряда второй клетки (1-8): "))

if (x1 + y1) % 2 == (x2 + y2) % 2:
    print("YES")
else:
    print("NO")

'''
    Task 3
    Якщо вводиться температура в градусах за шкалою Цельсія, 
    вона переводиться в температуру за шкалою Фаренгейта. 
    Або навпаки: температура за Фаренгейтом переводиться в температуру за Цельсієм.
'''
print("____________________")
print("Task 3")
temp = float(input("Введите температуру: "))
scale = input("Введите шкалу ('C' для Цельсия или 'F' для Фаренгейта): ").upper()

if scale == 'C':
    fahrenheit = (temp * 9/5) + 32
    print(f"Температура в Фаренгейтах: {fahrenheit:.2f}°F")
elif scale == 'F':
    celsius = (temp - 32) * 5/9
    print(f"Температура в Цельсиях: {celsius:.2f}°C")
else:
    print("Некорректный ввод шкалы. Пожалуйста, введите 'C' или 'F'.")

'''
    Task 4
    Зі списку випадкових чисел, визначити та вивести на екран непарні числа.
'''
print("____________________")
print("Task 4")
random_numbers = [12, 5, 23, 8, 19, 42, 33, 14, 7, 9]

print("Нечётные числа из списка:")
for number in random_numbers:
    if number % 2 != 0:
        print(number)

'''
    Task 5
    Вводиться ціле число, що означає код символу за таблицею ASCII. 
    Визначити, це код англійської літери або будь-який інший символ.
'''
print("____________________")
print("Task 5.1")
UPPERCASE_START = 65   # Код символа 'A'
UPPERCASE_END = 90     # Код символа 'Z'
LOWERCASE_START = 97   # Код символа 'a'
LOWERCASE_END = 122    # Код символа 'z'

ascii_code = int(input("Введите код символа по таблице ASCII: "))
symbol = chr(ascii_code)

if (UPPERCASE_START <= ascii_code <= UPPERCASE_END) or (LOWERCASE_START <= ascii_code <= LOWERCASE_END):
    print(f"Символ с кодом {ascii_code} - это английская буква: '{symbol}'")
else:
    print(f"Символ с кодом {ascii_code} - это не английская буква, а символ: '{symbol}'")

print("Task 5.1")
UPPERCASE_A = ord('A')
UPPERCASE_Z = ord('Z')
LOWERCASE_A = ord('a')
LOWERCASE_Z = ord('z')

if (UPPERCASE_A <= ascii_code <= UPPERCASE_Z) or (LOWERCASE_A <= ascii_code <= LOWERCASE_Z):
    print(f"Символ с кодом {ascii_code} - это английская буква: '{symbol}'")
else:
    print(f"Символ с кодом {ascii_code} - это не английская буква, а символ: '{symbol}'")

print("Task 5.2")

if (ord('A') <= ascii_code <= ord('Z')) or (ord('a') <= ascii_code <= ord('z')):
    print(f"Символ с кодом {ascii_code} - это английская буква: '{symbol}'")
else:
    print(f"Символ с кодом {ascii_code} - это не английская буква, а символ: '{symbol}'")

'''
    Task 6
    Вводяться два цілих числа. Перевірити чи ділиться перше на друге. 
    Вивести на екран повідомлення про це, а також залишок (якщо він є) 
    та приватне (у будь-якому випадку).
'''
print("____________________")
print("Task 6")
num1 = int(input("Введите первое число (делимое): "))
num2 = int(input("Введите второе число (делитель): "))

if num2 == 0:
    print("Деление на ноль невозможно.")
else:
    quotient = num1 // num2
    remainder = num1 % num2

    if remainder == 0:
        print(f"{num1} делится на {num2} без остатка. Частное: {quotient}")
    else:
        print(f"{num1} не делится на {num2} без остатка. Частное: {quotient}, Остаток: {remainder}")

'''
    Task 7
    По черзі вводиться 5 цифр, вивести їхню суму (скориставшись for)
'''
print("____________________")
print("Task 7")
total_sum = 0

for i in range(5):
    number = int(input(f"Введите цифру {i + 1}: "))
    total_sum += number

print(f"Сумма введённых цифр: {total_sum}")

'''
    Task 8
    Дано два цілих числа A і B. Виведіть усі числа від A до B включно, 
    в порядку зростання, якщо A < B, або в порядку убування інакше.
'''
print("____________________")
print("Task 8")
a = int(input("Введите число A: "))
b = int(input("Введите число B: "))

if a < b:
    for i in range(a, b + 1):
        print(i, end=' ')
else:
    for i in range(a, b - 1, -1):
        print(i, end=' ')
print()

'''
    Task 9
    Циклом for вивести ромб
'''
print("____________________")
print("Task 9")
height = int(input("Введите высоту ромба (половина): "))

for i in range(1, height + 1):
    print(" " * (height - i), end="")
    print("* " * i)

for i in range(height - 1, 0, -1):
    print(" " * (height - i), end="")
    print("* " * i)

'''
    Task 10.1
    Порахувати суму числового ряду від 0 до 14 включно. Наприклад, 0+1+2+3+…+14;
'''
print("____________________")
print("Task 10.1")
total_sum = 0

for i in range(0, 15):
    total_sum += i

print(f"Сумма чисел от 0 до 14: {total_sum}")

print("Task 10.2")
total_sum = sum(range(15))
print(f"Сумма чисел от 0 до 14: {total_sum}")

'''
    Task 11
    Перемножити всі парні значення в діапазоні від 0 до 436
'''
print("____________________")
print("Task 11")
product = 1

for i in range(0, 437, 2):
    if i != 0:
        product *= i

print(f"Произведение всех чётных чисел от 0 до 436: {product}")

'''
    Task 12
    Задається випадкове речове число. Визначте максимальну цифру цього числа. 
    Приклад виконання: 56.457 -> 7
'''
print("____________________")
print("Task 12")
number = input("Введите вещественное число: ")

clean_number = number.replace('.', '').replace(',', '')

max_digit = max(clean_number)

print(f"Максимальная цифра в числе: {max_digit}")

'''
    Task 13
    Факторіалом числа n називається число 𝑛! = 1∙2∙3∙…∙𝑛. 
    Створіть програму, яка обчислює фактор введеного користувачем числа. (Цикл!)
'''
print("____________________")
print("Task 13")
n = int(input("Введите число для вычисления факториала: "))
factorial = 1

for i in range(1, n + 1):
    factorial *= i

print(f"Факториал числа {n} равен: {factorial}")

'''
    Task 14
    Використовуючи вкладені цикли та функції print('*', end=''), print(' ', end='') та print() 
    виведіть на екран прямокутний трикутник.
'''
print("____________________")
print("Task 14")
height = int(input("Введите высоту треугольника: "))
for i in range(1, height + 1):
    for j in range(i):
        print('*', end='')
    print()

'''
    Task 15
    Користувач робить внесок у розмірі N $ строком на роки під 11.5% 
    річних (кожний рік розмір його вкладу збільшується на 11,5%. 
    Ці гроші додаються до суми вкладу, і на них наступного року також будуть відсотки). 
    Написати програму , де користувач вводить аргументи a та years, і порахувати суму, 
    яка буде на рахунку користувача через роки.
'''
print("____________________")
print("Task 15")
a = float(input("Введите начальную сумму вклада (в $): "))
years = int(input("Введите количество лет: "))
rate = 11.5
for year in range(1, years + 1):
    a += a * (rate / 100)
    print(f"После {year}-го года сумма на счёте: {a:.2f} $")

print(f"Итоговая сумма на счёте через {years} лет: {a:.2f} $")

'''
    Task 16
    Користувач вводить рік. Визначити він високосний чи ні.
'''
print("____________________")
print("Task 16")
year = int(input("Введите год: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} год является високосным.")
else:
    print(f"{year} год не является високосным.")

'''
    Task 17
    Напишіть програму, яка запитує три цілі числа a, b і x і виводить True, 
    якщо x лежить між a і b, інакше - False.
'''
print("____________________")
print("Task 17")
a = int(input("Введите первое число (a): "))
b = int(input("Введите второе число (b): "))
x = int(input("Введите число для проверки (x): "))

if min(a, b) <= x <= max(a, b):
    print(True)
else:
    print(False)

'''
    Task 18
    Дано чотири дійсні числа: x1, y1, x2, y2. обчисліть відстань між точкою 
    (x1, y1) та (x2, y2). Вважайте чотири дійсні числа та виведіть результат роботи цієї функції.
'''
import math
print("____________________")
print("Task 18")
x1 = float(input("Введите координату x1: "))
y1 = float(input("Введите координату y1: "))
x2 = float(input("Введите координату x2: "))
y2 = float(input("Введите координату y2: "))

distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print(f"Расстояние между точками ({x1}, {y1}) и ({x2}, {y2}) равно: {distance:.4f}")

'''
    Task 19
    Запитайте користувача про число n. Знайдіть суму всіх чисел від 1 до n.
'''
print("____________________")
print("Task 19")
n = int(input("Введите число n: "))

sum_n = sum(range(1, n + 1))

print(f"Сумма всех чисел от 1 до {n}: {sum_n}")

'''
    Task 20
    Виведіть таблицю множення для числа, яке вводить користувач (наприклад, таблицю множення для 5).
'''
print("____________________")
print("Task 20")
n = int(input("Введите число для вывода таблицы умножения: "))

print(f"Таблица умножения для {n}:")
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

'''
    Task 21
    Перевірте, чи є введене число простим. Виведіть повідомлення про результат.
'''
print("____________________")
print("Task 21")
n = int(input("Введите число для проверки на простоту: "))

if n > 1:
    is_prime = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{n} является простым числом.")
    else:
        print(f"{n} не является простым числом.")
else:
    print(f"{n} не является простым числом.")

'''
    Task 22
    Згенеруйте випадкове число в заданому діапазоні. 
    Дайте користувачу спробу вгадати це число. Виведіть повідомлення про результат.
'''
import random
print("____________________")
print("Task 22")
lower_bound = int(input("Введите нижнюю границу диапазона: "))
upper_bound = int(input("Введите верхнюю границу диапазона: "))

random_number = random.randint(lower_bound, upper_bound)

user_guess = int(input(f"Угадайте число между {lower_bound} и {upper_bound}: "))

if user_guess == random_number:
    print("Поздравляем! Вы угадали число!")
else:
    print(f"К сожалению, вы не угадали. Загаданное число было: {random_number}")

'''
    Task 23
    Перевірте, чи є це слово паліндромом (читається однаково зліва направо і справа наліво).
'''
print("____________________")
print("Task 23")
phrase = input("Введите слово или фразу для проверки на палиндром: ")

normalized_phrase = ''.join(char.lower() for char in phrase if char.isalnum())

if normalized_phrase == normalized_phrase[::-1]:
    print("Это палиндром.")
else:
    print("Это не палиндром.")

'''
    Task 24
    Відсортуйте цей список за допомогою алгоритму сортування бульбашкою.
'''
print("____________________")
print("Task 24")

numbers = [74, 24, 35, 2, 28, 13, 97]

n = len(numbers)

for i in range(n):
    for j in range(0, n - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print(f"Отсортированный список: {numbers}")

'''
    Task 25
    Створіть список чисел в діапазоні від 1 до n, пропустивши одне число. 
    Знайдіть та виведіть пропущене число. наприклад some_list =[1,2,3,5,6,7] , 
    пропущене число - 4.
'''
import random
print("____________________")
print("Task 25")
n = int(input("Введите значение n: "))

some_list = list(range(1, n + 1))

missing_number = random.choice(some_list)

some_list.remove(missing_number)

print(f"Список чисел: {some_list}")

expected_sum = n * (n + 1) // 2

actual_sum = sum(some_list)

found_missing_number = expected_sum - actual_sum

print(f"Пропущенное число: {found_missing_number}")

'''
    Task 26
    Сіракузська послідовність Запитайте користувача про початкове число. 
    Виведіть послідовність чисел за правилом: якщо число парне, поділіть його на 2, 
    інакше помножте на 3 і додайте 1. Повторюйте цей процес, поки не досягнете числа 1.
'''
print("____________________")
print("Task 26")
n = int(input("Введите начальное число: "))
print(f"Сиракузская последовательность для числа {n}:")

while n != 1:
    print(n, end=' ')
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1

print(n)

'''
    Task 27 - 28
    Запитайте користувача про верхню межу діапазону. 
    Знайдіть всі прості числа у заданому діапазоні і виведіть їх.
'''
print("____________________")
print("Task 27 - 28")
upper_limit = int(input("Введите верхнюю границу диапазона: "))
print(f"Простые числа в диапазоне от 2 до {upper_limit}:")

for num in range(2, upper_limit + 1):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=' ')
print()
'''
    Task 29
    Переведення числа в текст Запитайте користувача про ціле число від 1 до 999. 
    Виведіть це число прописом (наприклад, 123 → "сто двадцять три").
'''
print("____________________")
print("Task 29")

ones = ["", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
teens = ["десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать",
         "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]
tens = ["", "", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
hundreds = ["", "сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот"]

n = int(input("Введите число от 1 до 999: "))

if 1 <= n <= 999:
    result = ""
    result += hundreds[n // 100] + " "

    if 10 <= n % 100 <= 19:
        result += teens[n % 10]
    else:
        result += tens[(n % 100) // 10] + " "
        result += ones[n % 10]

    print(result.strip())
else:
    print("Введите корректное число от 1 до 999.")

'''
    Task 30
    Створіть функцію для знаходження найменшого спільного кратного двох чисел.
'''
print("____________________")
print("Task 30")

def greatest_common_divisor(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def least_common_multiple(a, b):
    return abs(a * b) // greatest_common_divisor(a, b)

first_number = int(input("Введите первое число: "))
second_number = int(input("Введите второе число: "))

result = least_common_multiple(first_number, second_number)
print(f"Наименьшее общее кратное для чисел {first_number} и {second_number}: {result}")
