'''
    Task 1
    Розробіть скрипт, який відкриває існуючий текстовий файл, зчитує його вміст та виводить його на екран.
'''
print("____________________")
print("Task 1")

def read_and_print_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        print(f"Файл '{filename}' не знайдено.")
    except Exception as e:
        print(f"Виникла помилка: {e}")

filename = 'example.txt'
print(read_and_print_file(filename))

'''
    Task 2
    Створіть програму, яка переіменовує файл з одного імені в інше. rename_file(path_to_file, new_name)
'''
print("____________________")
print("Task 2")

from pathlib import Path

def rename_file(path_to_file, new_name):
    try:
        file_path = Path(path_to_file)
        if not file_path.is_file():
            print(f"Файл '{path_to_file}' не знайдено.")
            return

        new_file_path = file_path.with_name(new_name)
        file_path.rename(new_file_path)
        print(f"Файл переіменовано на '{new_file_path.name}'")
    except Exception as e:
        print(f"Виникла помилка: {e}")

path_to_file = 'old_file.txt'
new_name = 'new_file.txt'
rename_file(path_to_file, new_name)

'''
    Task 3
    Напишіть скрипт для копіювання вмісту одного текстового файлу в інший. copy_to_file(source_file, new_file)
'''
print("____________________")
print("Task 3")
from pathlib import Path

def copy_to_file(source_file, new_file):
    try:
        source_path = Path(source_file)
        new_path = Path(new_file)

        if not source_path.is_file():
            print(f"Файл '{source_file}' не знайдено.")
            return

        content = source_path.read_text(encoding='utf-8')
        new_path.write_text(content, encoding='utf-8')
        print(f"Вміст файлу '{source_file}' успішно скопійовано до '{new_file}'.")
    except Exception as e:
        print(f"Виникла помилка: {e}")

source_file = 'example.txt'
new_file = 'destination.txt'
copy_to_file(source_file, new_file)

'''
    Task 4
    Розробіть програму, яка визначає кількість слів у текстовому файлі. count_words(path_to_file)
'''
print("____________________")
print("Task 4")

from pathlib import Path
import re
import unicodedata

def count_words(path_to_file):
    try:
        file_path = Path(path_to_file)
        if not file_path.is_file():
            print(f"Файл '{path_to_file}' не знайдено.")
            return

        encodings = ['utf-8', 'utf-16', 'utf-32', 'latin-1']
        for encoding in encodings:
            try:
                with open(file_path, 'r', encoding=encoding) as f:
                    text = f.read()
                break
            except UnicodeDecodeError:
                continue
        else:
            print("Не вдалося визначити кодування файлу.")
            return

        word_candidates = re.findall(r'\b\w+\b', text, flags=re.UNICODE)

        words = [
            word for word in word_candidates
            if all(unicodedata.category(char).startswith('L') for char in word)
        ]

        num_words = len(words)
        unique_words = set(words)
        num_unique_words = len(unique_words)

        print(f"Загальна кількість слів у файлі '{path_to_file}': {num_words}")
        print(f"Кількість унікальних слів у файлі '{path_to_file}': {num_unique_words}")

        return num_words, num_unique_words

    except Exception as e:
        print(f"Виникла помилка: {e}")
        return

path_to_file = 'example.txt'
count_words(path_to_file)

'''
    Task 5
    Створіть скрипт, який видаляє текстовий файл. remove_file(path_file). Повертає помилку якщо файла не існує/
'''
print("____________________")
print("Task 5")

from pathlib import Path

def remove_file(path_file):
    file_path = Path(path_file)
    try:
        file_path.unlink()
        print(f"Файл '{path_file}' успішно видалено.")
    except Exception as e:
        print(f"Виникла помилка при видаленні файлу: {e}")
        raise

path_file = Path('delete_me.txt')
if path_file.is_file():
    remove_file(path_file)
else:
    print(f"Файл '{path_file}' не знайдено.")

'''
    Task 6
    Напишіть програму, яка додає новий рядок до існуючого текстового файлу add_data_to_file(path_file , text).
'''
print("____________________")
print("Task 6")

from pathlib import Path

def add_data_to_file(path_file, text):
    file_path = Path(path_file)
    if not file_path.is_file():
        raise FileNotFoundError(f"Файл '{path_file}' не знайдено.")

    try:
        with file_path.open('a', encoding='utf-8') as file:
            file.write(text + '\n')
        print(f"Текст успішно додано до файлу '{path_file}'.")
    except Exception as e:
        print(f"Виникла помилка при додаванні тексту до файлу: {e}")
        raise

path_file = 'example.txt'
text = 'Новий рядок тексту'
add_data_to_file(path_file, text)

'''
    Task 7
    Розробіть скрипт, який перевіряє наявність файлу за заданим ім'ям та повідомляє
    користувача про результат. функція має повертати True/False
'''
print("____________________")
print("Task 7")

from pathlib import Path

def check_file_exists(file_name):
    file_path = Path(file_name)
    if file_path.is_file():
        print(f"Файл '{file_name}' існує.")
        return True
    else:
        print(f"Файл '{file_name}' не знайдено.")
        return False

file_name = 'example.txt'
print(check_file_exists(file_name))

'''
    Task 8
    Створіть програму, яка шукає вказаний текст у файлі та виводить номери рядків,
    де цей текст знаходиться find_text(path_file, search_text )
'''
print("____________________")
print("Task 8")

from pathlib import Path

def find_text(path_file, search_text):
    try:
        file_path = Path(path_file)
        if not file_path.is_file():
            raise FileNotFoundError(f"Файл '{path_file}' не знайдено.")

        with file_path.open('r', encoding='utf-8') as file:
            lines = file.readlines()

        found = False
        for line_number, line in enumerate(lines, start=1):
            if search_text in line:
                print(f"Текст '{search_text}' знайдено в рядку {line_number}:")
                found = True

        if not found:
            print(f"Текст '{search_text}' не знайдено у файлі '{path_file}'.")

    except Exception as e:
        print(f"Виникла помилка: {e}")
        raise

path_file = 'example.txt'
search_text = 'скрипт'
find_text(path_file, search_text)

'''
    Task 9
    Напишіть скрипт, який сортує вміст текстового файлу за алфавітом і зберігає відсортований результат
    у новому файлі. sort_data_in_file(file_path). Резульаттом має бути новий файл з наступною
    назвою {file_path}_sorted
'''
print("____________________")
print("Task 9")

from pathlib import Path

def sort_data_in_file(file_path):
    try:
        original_file = Path(file_path)

        if not original_file.is_file():
            raise FileNotFoundError(f"Файл '{file_path}' не знайдено.")

        with original_file.open('r', encoding='utf-8') as f:
            lines = f.readlines()

        sorted_lines = sorted(lines)
        sorted_file_name = f"{original_file.stem}_sorted.txt"
        sorted_file_path = original_file.parent / sorted_file_name

        with sorted_file_path.open('w', encoding='utf-8') as f:
            f.writelines(sorted_lines)

        print(f"Відсортований вміст збережено у файлі '{sorted_file_path}'.")

    except Exception as e:
        print(f"Виникла помилка: {e}")
        raise

file_path = 'example.txt'
sort_data_in_file(file_path)

'''
    Task 10
    Розробіть функцію, яка перевіряє розмір файлу і повідомляє користувача, чи він
    перевищує заданий ліміт. is_greater_size(file_path, limit)
'''
print("____________________")
print("Task 10")

from pathlib import Path

def is_greater_size(file_path, limit):
    try:
        path = Path(file_path)
        if not path.is_file():
            raise FileNotFoundError(f"Файл '{file_path}' не знайдено.")

        file_size = path.stat().st_size

        if file_size > limit:
            print(f"Розмір файлу '{file_path}' ({file_size} байт) перевищує ліміт {limit} байт.")
            return True
        else:
            print(f"Розмір файлу '{file_path}' ({file_size} байт) не перевищує ліміт {limit} байт.")
            return False

    except Exception as e:
        print(f"Виникла помилка: {e}")
        raise

file_path = 'example.txt'
limit = 1024
is_greater_size(file_path, limit)

'''
    Task 11
    Напишіть скрипт для копіювання усіх файлів з одного каталогу в інший. copy_folder(from_folder , to_folder)
'''
print("____________________")
print("Task 11")

from pathlib import Path
import shutil

def copy_folder(from_folder, to_folder):
    try:
        src_path = Path(from_folder)
        dest_path = Path(to_folder)

        if not src_path.is_dir():
            raise NotADirectoryError(f"Каталог '{from_folder}' не знайдено або це не директорія.")

        dest_path.mkdir(parents=True, exist_ok=True)

        for item in src_path.iterdir():
            if item.is_file():
                shutil.copy2(item, dest_path / item.name)

        print(f"Усі файли з '{from_folder}' успішно скопійовано до '{to_folder}'.")

    except Exception as e:
        print(f"Виникла помилка: {e}")
        raise

from_folder = 'source_folder'
to_folder = 'destination_folder'
copy_folder(from_folder, to_folder)

'''
    Task 12
    Створіть функцію, яка читає CSV-файл і виводить на екран лише певні стовпці.
'''
print("____________________")
print("Task 12")

import csv

def print_csv_columns(file_path, columns):
    try:
        with open(file_path, mode='r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            if not reader.fieldnames:
                print("CSV-файл не містить заголовків стовпців.")
                return

            if isinstance(columns[0], int):
                headers = reader.fieldnames
                columns_to_print = [headers[i] for i in columns]
            else:
                columns_to_print = columns

            for row in reader:
                selected_data = [row[col] for col in columns_to_print if col in row]
                print(selected_data) # Варіант 1 виводу

                selected_data_1 = [row[col] for col in columns_to_print if col in row]
                print(', '.join(selected_data_1)) # Варіант 2 виводу

    except FileNotFoundError:
        print(f"Файл '{file_path}' не знайдено.")
    except Exception as e:
        print(f"Виникла помилка: {e}")

file_path = 'data.csv'
columns = ['Name', 'Age']
print_csv_columns(file_path, columns)

'''
    Task 13
    Напишіть скрипт, який створює архів з кількох файлів та розпаковує його. має бути дві функції
    create_archive (*files)
    unpacking_archive(path_to_archive)
'''
print("____________________")
print("Task 13")

import zipfile
from pathlib import Path

def create_archive(*files):
    archive_name = 'archive.zip'
    try:
        with zipfile.ZipFile(archive_name, 'w') as archive:
            for file in files:
                file_path = Path(file)
                if file_path.is_file():
                    archive.write(file_path, arcname=file_path.name)
                    print(f"Файл '{file}' додано до архіву.")
                else:
                    print(f"Файл '{file}' не знайдено і не буде додано.")
        print(f"Архів '{archive_name}' успішно створено.")
    except Exception as e:
        print(f"Виникла помилка при створенні архіву: {e}")
        raise

def unpacking_archive(path_to_archive):
    try:
        with zipfile.ZipFile(path_to_archive, 'r') as archive:
            archive.extractall()
            print(f"Архів '{path_to_archive}' успішно розпаковано.")
    except FileNotFoundError:
        print(f"Архів '{path_to_archive}' не знайдено.")
    except zipfile.BadZipFile:
        print(f"Файл '{path_to_archive}' не є дійсним ZIP-архівом.")
    except Exception as e:
        print(f"Виникла помилка при розпакуванні архіву: {e}")
        raise


create_archive('source_folder/test.txt', 'source_folder/Test_1.txt', 'source_folder/Test_3.txt')
unpacking_archive('archive.zip')

'''
    Task 14
    Розробіть функцію, яка змінює права доступу до файлу
    (наприклад, робить його доступним лише для читання або запису).
'''
print("____________________")
print("Task 14")

import os
import stat
from pathlib import Path

def change_file_permissions(file_path, mode):
    try:
        path = Path(file_path)
        if not path.is_file():
            raise FileNotFoundError(f"Файл '{file_path}' не знайдено.")

        if mode == 'read_only':
            path.chmod(stat.S_IREAD | stat.S_IRGRP | stat.S_IROTH)
            print(f"Права доступу до файлу '{file_path}' змінено на 'лише читання'.")
        elif mode == 'write_only':
            path.chmod(stat.S_IWRITE | stat.S_IWGRP | stat.S_IWOTH)
            print(f"Права доступу до файлу '{file_path}' змінено на 'лише запис'.")
        elif mode == 'read_write':
            path.chmod(stat.S_IREAD | stat.S_IWRITE | stat.S_IRGRP | stat.S_IWGRP | stat.S_IROTH | stat.S_IWOTH)
            print(f"Права доступу до файлу '{file_path}' змінено на 'читання та запис'.")
        else:
            print(f"Невідомий режим доступу: '{mode}'. Використайте 'read_only', 'write_only' або 'read_write'.")
    except Exception as e:
        print(f"Виникла помилка: {e}")
        raise

file_path = 'example.txt'
mode = 'read_only'
change_file_permissions(file_path, mode)

'''
    Task 15
    Створіть функцію, яка виводить список всіх файлів у заданому каталозі та його підкаталогах.
'''
print("____________________")
print("Task 15")

from pathlib import Path

def list_all_files(directory):
    try:
        path = Path(directory)
        if not path.is_dir():
            raise NotADirectoryError(f"'{directory}' не є каталогом або не існує.")

        for file_path in path.rglob('*'):
            if file_path.is_file():
                print(file_path.resolve()) # Виведення повного шляху файлу
                print(file_path.name) # Виведення лише імені файлу
    except Exception as e:
        print(f"Виникла помилка: {e}")
        raise

directory = '../hometasks_3'
list_all_files(directory)

'''
    Task 16
    Напишіть функцію, яка масово перейменовує файли у заданому каталозі за певним шаблоном.
    Додайте до кожної назви файла префікс "rename_"
'''
print("____________________")
print("Task 16")

from pathlib import Path

def mass_rename_files(directory):
    try:
        path = Path(directory)
        if not path.is_dir():
            raise NotADirectoryError(f"'{directory}' не є каталогом або не існує.")

        for file_path in path.iterdir():
            if file_path.is_file():
                new_name = "rename_" + file_path.name
                new_file_path = file_path.with_name(new_name)

                if new_file_path.exists():
                    print(f"Файл з ім'ям '{new_name}' вже існує. Пропускаємо файл '{file_path.name}'.")
                    continue

                file_path.rename(new_file_path)
                print(f"Файл '{file_path.name}' перейменовано у '{new_name}'")
    except Exception as e:
        print(f"Виникла помилка: {e}")
        raise

directory = 'source_folder'
mass_rename_files(directory)

'''
    Task 17
    Створіть скрипт, який зчитує XML-файл та витягує з нього певну інформацію.
'''
print("____________________")
print("Task 17")

import xml.etree.ElementTree as ET

def extract_information(xml_file, tag_name):
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()

        elements = root.findall(f".//{tag_name}")

        extracted_data = [elem.text for elem in elements if elem.text is not None]

        return extracted_data

    except ET.ParseError as e:
        print(f"Помилка розбору XML-файлу: {e}")
    except FileNotFoundError:
        print(f"Файл '{xml_file}' не знайдено.")
    except Exception as e:
        print(f"Виникла помилка: {e}")

xml_file = 'example.xml'
tag_name = 'item'

data = extract_information(xml_file, tag_name)
if data:
    for idx, text in enumerate(data, start=1):
        print(f"{idx}. {text}")
else:
    print(f"Тег '{tag_name}' не знайдено у файлі '{xml_file}'.")

'''
    Task 18
    Розробіть скрипт, який переформатовує CSV-файл, видаляючи дублікати рядків
    та зберігаючи результат у новому файлі.
'''
print("____________________")
print("Task 18")

import csv

def remove_duplicates(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            reader = csv.reader(infile)
            data = list(reader)

        unique_data = []
        seen = set()
        for row in data:
            row_tuple = tuple(row)
            if row_tuple not in seen:
                seen.add(row_tuple)
                unique_data.append(row)

        with open(output_file, 'w', encoding='utf-8', newline='') as outfile:
            writer = csv.writer(outfile)
            writer.writerows(unique_data)

        print(f"Результат збережено у файлі '{output_file}'.")
    except FileNotFoundError:
        print(f"Файл '{input_file}' не знайдено.")
    except Exception as e:
        print(f"Виникла помилка: {e}")

input_file = 'input.csv'
output_file = 'output.csv'
remove_duplicates(input_file, output_file)

'''
    Task 19
    Створіть функцію для пошуку файлів з певним розширенням у вказаному каталозі та всіх його підкаталогах..
'''
print("____________________")
print("Task 19")

from pathlib import Path

def find_files_with_extension(directory, extension):
    try:
        path = Path(directory)
        if not path.is_dir():
            raise NotADirectoryError(f"'{directory}' не є каталогом або не існує.")

        files = list(path.rglob(f'*{extension}'))

        return files

    except Exception as e:
        print(f"Виникла помилка: {e}")
        raise

directory = '../hometasks_3'
extension = '.txt'
files = find_files_with_extension(directory, extension)
if files:
    print(f"Знайдено {len(files)} файл(ів) з розширенням '{extension}':")
    for file in files:
        print(file.resolve())
else:
    print(f"Файлів з розширенням '{extension}' не знайдено у каталозі '{directory}'.")

'''
    Task 20
    Створіть функцію для створення текстового файлу, в якому кожний рядок містить назву файлу,
    його розмір та дату створення, для всіх файлів у вказаному каталозі.
'''
print("____________________")
print("Task 20")

from pathlib import Path
from datetime import datetime

def create_file_report(directory, output_file):
    try:
        path = Path(directory)
        if not path.is_dir():
            raise NotADirectoryError(f"'{directory}' не є каталогом або не існує.")

        with open(output_file, 'w', encoding='utf-8') as outfile:
            for file_path in path.iterdir():
                if file_path.is_file():
                    file_name = file_path.name
                    file_size = file_path.stat().st_size  # Розмір файлу в байтах
                    creation_time = datetime.fromtimestamp(file_path.stat().st_ctime)
                    creation_time_str = creation_time.strftime('%Y-%m-%d %H:%M:%S')

                    outfile.write(f"{file_name}, {file_size} байт, створено: {creation_time_str}\n")

        print(f"Інформацію про файли записано у файл '{output_file}'.")
    except Exception as e:
        print(f"Виникла помилка: {e}")
        raise

directory = '../hometasks_3'
output_file = 'file_report.txt'
create_file_report(directory, output_file)

'''
    Task 21
    Розробіть функцію для знаходження найбільшого та найменшого файлів у вказаному каталозі.
'''
print("____________________")
print("Task 21")

from pathlib import Path

def find_largest_and_smallest_files(directory):
    try:
        path = Path(directory)
        if not path.is_dir():
            raise NotADirectoryError(f"'{directory}' не є каталогом або не існує.")

        files = [file for file in path.iterdir() if file.is_file()]

        if not files:
            print(f"У каталозі '{directory}' немає файлів.")
            return None, None

        files_sorted_by_size = sorted(files, key=lambda x: x.stat().st_size)

        smallest_file = files_sorted_by_size[0]
        largest_file = files_sorted_by_size[-1]

        print(f"Найменший файл: '{smallest_file.name}', розмір: {smallest_file.stat().st_size} байт")
        print(f"Найбільший файл: '{largest_file.name}', розмір: {largest_file.stat().st_size} байт")

        return smallest_file, largest_file

    except Exception as e:
        print(f"Виникла помилка: {e}")
        raise

directory = '../hometasks_3'
find_largest_and_smallest_files(directory)

'''
    Task 22
    Створіть функцію для об'єднання вмісту декількох текстових файлів у один файл.
'''
print("____________________")
print("Task 22")

from pathlib import Path

def merge_text_files(output_file, *input_files):
    try:
        with open(output_file, 'w', encoding='utf-8') as outfile:
            for input_file in input_files:
                input_path = Path(input_file)
                if input_path.is_file():
                    with open(input_file, 'r', encoding='utf-8') as infile:
                        content = infile.read()
                        outfile.write(content + '\n')
                        print(f"Вміст файлу '{input_file}' додано до '{output_file}'.")
                else:
                    print(f"Файл '{input_file}' не знайдено або це не файл. Пропуск.")

        print(f"Всі файли успішно об'єднано у '{output_file}'.")
    except Exception as e:
        print(f"Виникла помилка: {e}")
        raise

output_file = 'merged_output.txt'
input_files = ['example.txt', 'example_1.txt', 'example_2.txt']
merge_text_files(output_file, *input_files)

'''
    Task 23
    Створіть функцію, яка перевіряє, чи усі файли у вказаному каталозі мають однаковий розмір.
'''
print("____________________")
print("Task 23")

from pathlib import Path

def are_files_same_size(directory):
    try:
        path = Path(directory)
        if not path.is_dir():
            raise NotADirectoryError(f"'{directory}' не є каталогом або не існує.")

        file_sizes = set()

        for file_path in path.iterdir():
            if file_path.is_file():
                file_size = file_path.stat().st_size
                file_sizes.add(file_size)

        if len(file_sizes) == 1:
            print("Всі файли мають однаковий розмір.")
            return True
        else:
            print("Файли мають різний розмір.")
            return False

    except Exception as e:
        print(f"Виникла помилка: {e}")
        raise

directory = '../hometasks_3'
are_files_same_size(directory)
directory = 'for_size'
are_files_same_size(directory)

'''
    Task 24
    Розробіть скрипт для вилучення всіх коментарів з файлу програмного коду на мові Python.
'''
print("____________________")
print("Task 24")

import re

def remove_comments_from_python_file(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            code = infile.read()

        code_without_single_comments = re.sub(r'#.*', '', code)
        code_without_multiline_comments = re.sub(r'\'\'\'(.*?)\'\'\'', '', code_without_single_comments, flags=re.DOTALL)
        code_cleaned = re.sub(r'\"\"\"(.*?)\"\"\"', '', code_without_multiline_comments, flags=re.DOTALL)

        with open(output_file, 'w', encoding='utf-8') as outfile:
            outfile.write(code_cleaned)

        print(f"Коментарі успішно вилучено. Результат збережено у '{output_file}'.")

    except FileNotFoundError:
        print(f"Файл '{input_file}' не знайдено.")
    except Exception as e:
        print(f"Виникла помилка: {e}")
        raise

input_file = 'example.py'
output_file = 'cleaned_code.py'
remove_comments_from_python_file(input_file, output_file)

'''
    Task 25
    Створіть скрипт, який автоматично видаляє файли, які не змінювалися протягом останнього
    місяця, з вказаного каталогу
'''
print("____________________")
print("Task 25")

from pathlib import Path
import time

def delete_old_files(directory):

    try:
        path = Path(directory)
        if not path.is_dir():
            raise NotADirectoryError(f"'{directory}' не є каталогом або не існує.")

        current_time = time.time()
        one_month_ago = current_time - 30 * 24 * 60 * 60

        for file_path in path.iterdir():
            if file_path.is_file():
                file_mod_time = file_path.stat().st_mtime

                if file_mod_time < one_month_ago:
                    print(f"Видаляємо файл: {file_path} (Остання модифікація: {time.ctime(file_mod_time)})")
                    file_path.unlink()

        print(f"Очищення каталогу '{directory}' завершено.")

    except Exception as e:
        print(f"Виникла помилка: {e}")
        raise

directory = '../hometasks_3'
delete_old_files(directory)

'''
    Task 26
    Напишіть функцію для розділу списку на два підсписки, використовуючи певний елемент як роздільник.
    Врахуйте можливі помилки, такі як відсутність роздільника чи невірний тип даних у списку.
'''
print("____________________")
print("Task 26")

def split_list_by_element(lst, delimiter):
    try:
        if not isinstance(lst, list):
            raise TypeError("Перший аргумент має бути списком.")

        if delimiter not in lst:
            raise ValueError(f"Роздільник '{delimiter}' не знайдено у списку.")

        delimiter_index = lst.index(delimiter)

        left_sublist = lst[:delimiter_index]
        right_sublist = lst[delimiter_index + 1:]

        return left_sublist, right_sublist

    except TypeError as te:
        print(f"Помилка типу: {te}")
    except ValueError as ve:
        print(f"Помилка значення: {ve}")
    except Exception as e:
        print(f"Виникла непередбачена помилка: {e}")
        raise

lst = [1, 2, 3, "роздільник", 4, 5, 6]
delimiter = "роздільник"

result = split_list_by_element(lst, delimiter)

if result:
    left, right = result
    print("Ліва частина:", left)
    print("Права частина:", right)

'''
    Task 27
    Розробіть функцію для обчислення податку на прибуток за різними ставками.
    Використовуйте try-except, щоб обробити можливі помилки введення користувача або некоректні дані.
'''
print("____________________")
print("Task 27")

def calculate_income_tax(income, tax_rate):
    try:
        if not isinstance(income, (int, float)):
            raise TypeError("Прибуток повинен бути числом.")

        if not isinstance(tax_rate, (int, float)):
            raise TypeError("Ставка податку повинна бути числом.")

        if income < 0:
            raise ValueError("Прибуток не може бути від'ємним.")

        if tax_rate < 0:
            raise ValueError("Ставка податку не може бути від'ємною.")

        tax_amount = income * (tax_rate / 100)
        return tax_amount

    except TypeError as te:
        print(f"Помилка типу даних: {te}")
    except ValueError as ve:
        print(f"Помилка значення: {ve}")
    except Exception as e:
        print(f"Виникла непередбачена помилка: {e}")
        raise

try:
    income_input = input("Введіть ваш прибуток: ")
    tax_rate_input = input("Введіть ставку податку (%): ")

    income = float(income_input)
    tax_rate = float(tax_rate_input)

    tax = calculate_income_tax(income, tax_rate)

    if tax is not None:
        print(f"Сума податку: {tax:.2f}")

except ValueError:
    print("Введені дані не є числом. Будь ласка, спробуйте ще раз.")
except Exception as e:
    print(f"Виникла непередбачена помилка: {e}")

'''
    Task 28
    Створіть програму для валідації електронної адреси користувача.
    Використовуйте try-except, щоб обробити помилки формату або відсутності необхідних компонентів (наприклад, "@").
'''
print("____________________")
print("Task 28")

import re

def validate_email(email):
    try:
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        if not isinstance(email, str):
            raise TypeError("Електронна адреса повинна бути рядком.")

        if not re.match(email_regex, email):
            raise ValueError("Електронна адреса має неправильний формат.")

        return True

    except TypeError as te:
        print(f"Помилка типу: {te}")
    except ValueError as ve:
        print(f"Помилка значення: {ve}")
    except Exception as e:
        print(f"Виникла непередбачена помилка: {e}")
        raise
try:
    email_input = input("Введіть електронну адресу: ")
    if validate_email(email_input):
        print("Електронна адреса є дійсною.")
    else:
        print("Електронна адреса є недійсною.")

except Exception as e:
    print(f"Виникла непередбачена помилка: {e}")

'''
    Task 29
    Напишіть код, який зчитує вміст HTML-файлу та виводить список всіх URL-адрес у файлі.
'''
print("____________________")
print("Task 29")

import re

def extract_urls_from_html_1(file_path):
    try:
        url_regex = r'href=["\'](.*?)["\']'

        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        urls = re.findall(url_regex, content)

        return urls

    except FileNotFoundError:
        print(f"Файл '{file_path}' не знайдено.")
    except Exception as e:
        print(f"Виникла помилка: {e}")
        raise

file_path = 'example.html'
urls = extract_urls_from_html_1(file_path)

if urls:
    print("Знайдені URL-адреси:")
    for url in urls:
        print(url)
else:
    print("URL-адрес не знайдено або файл порожній.")

print("Task 29.1")
from bs4 import BeautifulSoup

def extract_urls_from_html(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        soup = BeautifulSoup(content, 'html.parser')
        urls = [a['href'] for a in soup.find_all('a', href=True)]

        return urls
    except Exception as e:
        print(f"Виникла помилка: {e}")
        raise

file_path = 'example.html'
urls = extract_urls_from_html(file_path)

if urls:
    print("Знайдені URL-адреси:")
    for url in urls:
        print(url)
else:
    print("URL-адрес не знайдено або файл порожній.")
