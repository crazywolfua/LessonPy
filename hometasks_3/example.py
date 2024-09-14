'''
    Task 1
    Розробіть скрипт, який відкриває існуючий текстовий файл, зчитує його вміст та виводить його на екран.
'''
print("____________________")
print("Task 1")

def read_and_print_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            contents = file.read() # comments
            print(contents)
    except FileNotFoundError:
        print(f"Файл '{filename}' не знайдено.")
    except Exception as e:
        print(f"Виникла помилка: {e}")

filename = 'example.txt'
print(read_and_print_file(filename))