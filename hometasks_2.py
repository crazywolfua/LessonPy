'''
    Task 1
    Напишіть функцію для визначення парності числа: is_even(7) - повертає false
'''
print("____________________")
print("Task 1")

def is_even(number):
    return number % 2 == 0

print(is_even(int(input("Введите число: "))))

'''
    Task 2
    Напишіть функцію для обчислення факторіалу числа: factorial(4) - повертає 24
'''
print("____________________")
print("Task 2")

def factorial(number):
    result = 1
    for i in range(1, number+1):
        result *= i
    return result

some_result = factorial(int(input("Введите число, факториал которого хотите узнать: ")))
print(f"Факториал числа равен: {some_result}")

'''
    Task 3
    Напишіть функцію для виведення всіх парних чисел від 1 до n: print_even_numbers(10)
'''
print("____________________")
print("Task 3")

def print_even_numbers(number):
    result = ""
    for i in range(0, number+1, 2):
        if i != 0:
            result += f"{i} "
    print(f"Четные числа в указанном диапазоне: {result}")

def print_even_numbers_1(number):
    result = ""
    for i in range(1, number+1):
        if i % 2 == 0:
            if i != 0:
                result += f"{i} "
    return result

print_even = int(input("Введите конец диапазона чисел: "))
print(f"Четные числа в указанном диапазоне: {print_even_numbers_1(print_even)}")

'''
    Task 4
    Напишіть функцію для переведення градусів Цельсія у градуси Фаренгейта celsius_to_fahrenheit(10)
'''
print("____________________")
print("Task 4")

def celsius_to_fahrenheit(temp: float):
    result = temp * 9 / 5 + 32
    return result

celsius_temp = input("Введите температуру в °C: ")
print(f"Температура по Фаренгейту: {celsius_to_fahrenheit(float(celsius_temp))}°F")

'''
    Task 5
    Напишіть функцію для обчислення площі прямокутника
'''
print("____________________")
print("Task 5")

def rectangle_area(width, height):
    return width * height

width = float(input("Введите ширину прямоугольника: "))
height = float(input("Введите высоту прямоугольника: "))

print(f"Площадь прямоугольника: {rectangle_area(width, height)}")

'''
    Task 6
    Напишіть функцію для обчислення кількості голів та ніг у стаді худоби та курей count_animals(heads, legs)
'''
print("____________________")
print("Task 6")

def count_animals(heads, legs):
    for cows in range(heads + 1):
        chickens = heads - cows
        if cows * 4 + chickens * 2 == legs:
            return chickens, cows
    return None

heads = int(input("Введите количество голов: "))
legs = int(input("Введите количество ног: "))

result = count_animals(heads, legs)

if result:
    print(f"Количество кур: {result[0]}, Количество коров: {result[1]}")
else:
    print("Невозможно вычислить количество животных с такими данными.")

'''
    Task 7
    Напишіть функцію для перевірки простоти числа: is_prime(10)
'''
print("____________________")
print("Task 7")

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(int(input("Введите число для проверки на простоту: "))))

'''
    Task 8
    Функція для перевірки паліндрому: is_palindrome('hello world')
'''
print("____________________")
print("Task 8")

def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

print(is_palindrome(input("Введите слово или фразу для проверки на палиндром: ")))

'''
    Task 9
    Функція для генерації списку простих чисел: generate_primes(30) (використайте фун-цію is_prime)
'''
print("____________________")
print("Task 9")

def generate_primes(limit):
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes

some_list = generate_primes(int(input("Введите числовое значение: ")))
print(f"Список простых чисел входящих в указанное числовое значение: {some_list}")

'''
    Task 10
    Функція для конвертації числа у римський запис: int_to_roman(100)
'''
print("____________________")
print("Task 10")

def int_to_roman(number):
    roman_numerals = {
        1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
        100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
        10: 'X', 9: 'IX', 5: 'V', 4: 'IV',
        1: 'I'
    }

    result = ""
    for value in roman_numerals:
        while number >= value:
            result += roman_numerals[value]
            number -= value
    return result

print(int_to_roman(int(input("Введите число, которое вы хотите перевести в римскую систему счисления: "))))

'''
    Task 11
    Функція для обчислення коренів квадратного рівняння
'''
import math

print("____________________")
print("Task 11")

def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return x1, x2
    elif discriminant == 0:
        x = -b / (2 * a)
        return x,
    else:
        return None

a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))

result = solve_quadratic(a, b, c)

if result is None:
    print("Уравнение не имеет действительных корней.")
elif len(result) == 1:
    print(f"Уравнение имеет один корень: {result[0]}")
else:
    print(f"Уравнение имеет два корня: {result[0]} и {result[1]}")

'''
    Task 12
    Написати функцію яка перетворює рядок на наступний формат. функція повинна ПОВЕРТАТИ рядок
            rebuild_string('test') = > tEsT
            rebuild_string('some string') = > sOmE sTrIng
'''
print("____________________")
print("Task 12")

def rebuild_string(s):
    result = []
    for i, char in enumerate(s):
        if i % 2 == 0:
            result.append(char.lower())
        else:
            result.append(char.upper())
    return ''.join(result)

print(rebuild_string(input("Введите строку, которую необходимо преобразовать: ")))

'''
    Task 13
    Написати функцію, яка змінює цифри на літери за принципом 0-А 1-B 2-C ... etc 
    і ПОВЕРТАЄ строку proccess_str('231') => CDB
'''
print("____________________")
print("Task 13")

def process_str(s):
    result = []
    for char in s:
        if char.isdigit():
            result.append(chr(ord('A') + int(char)))
        else:
            result.append(char)
    return ''.join(result)

print(process_str(input("Введите числовое значение, которое необходимо преобразовать: ")))

'''
    Task 14
    Написати функцію з розрахунку скільки витрачається грошей на кип'ятіння води в чайнику. 
    На вхід подається початкова температура води та маса води. 
    Функція повинна повернути кількість гривень.
        Q = C*m*(t2-t1), де:
        C - питома теплоємність, тобто. енергія, необхідна нагрівання в-ва на 1 градус. 
            Для води за нормального тиску (101.325 кПа) це 4200 джоулів.
        m – маса, 1 літр води за звичайних умов має масу 1 кг.
        t2 – верхня температура нагріву, для нормального тиску температура кипіння води 100 градусів.
        t1 – початкова температура = кімнатна температура = у моєму випадку 25,6 гр.
        Q вимірюється у джоулях. 1Дж = 2.7778e-7 Кват/год. Необхідно перевести з Джуолей в кіловатий годинник.
        Вартість електроенергії можна взяти як 2,64 грн за 1кват/год.
'''
print("____________________")
print("Task 14")

def calculate_boiling_cost(mass, initial_temp):
    # Константы
    C = 4200
    BOILING_TEMP = 100
    ELECTRICITY_RATE = 4.32 # Новый тариф на электричество за 1 кВт/час (грн)
    JOULE_TO_KWH = 2.7778e-7

    Q = C * mass * (BOILING_TEMP - initial_temp)

    energy_kwh = Q * JOULE_TO_KWH

    cost = energy_kwh * ELECTRICITY_RATE

    return cost

mass = float(input("Введите массу воды (в кг): "))
initial_temp = float(input("Введите начальную температуру воды (в градусах Цельсия): "))

cost = calculate_boiling_cost(mass, initial_temp)
print(f"Стоимость кипячения воды: {cost:.2f} грн")