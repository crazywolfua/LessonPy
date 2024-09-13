'''
    Task 1
    Розробіть скрипт, який відкриває існуючий текстовий файл, зчитує його вміст та виводить його на екран.
'''
# print("____________________")
# print("Task 1")
#
# def read_and_print_file(filename):
#     try:
#         with open(filename, 'r', encoding='utf-8') as file:
#             contents = file.read()
#             print(contents)
#     except FileNotFoundError:
#         print(f"Файл '{filename}' не знайдено.")
#     except Exception as e:
#         print(f"Виникла помилка: {e}")
#
# filename = 'example.txt'
# print(read_and_print_file(filename))


'''
    Task 2
    Створіть програму, яка переіменовує файл з одного імені в інше. rename_file(path_to_file, new_name)
'''
# print("____________________")
# print("Task 2")
#
# from pathlib import Path
#
# def rename_file(path_to_file, new_name):
#     try:
#         file_path = Path(path_to_file)
#         if not file_path.is_file():
#             print(f"Файл '{path_to_file}' не знайдено.")
#             return
#
#         new_file_path = file_path.with_name(new_name)
#         file_path.rename(new_file_path)
#         print(f"Файл переіменовано на '{new_file_path.name}'")
#     except Exception as e:
#         print(f"Виникла помилка: {e}")
#
# path_to_file = 'old_file.txt'
# new_name = 'new_file.txt'
# rename_file(path_to_file, new_name)

# '''
#     Task 3
#     Напишіть скрипт для копіювання вмісту одного текстового файлу в інший. copy_to_file(source_file, new_file)
# '''
# print("____________________")
# print("Task 3")
# from pathlib import Path
#
# def copy_to_file(source_file, new_file):
#     try:
#         source_path = Path(source_file)
#         new_path = Path(new_file)
#
#         if not source_path.is_file():
#             print(f"Файл '{source_file}' не знайдено.")
#             return
#
#         content = source_path.read_text(encoding='utf-8')
#
#         new_path.write_text(content, encoding='utf-8')
#
#         print(f"Вміст файлу '{source_file}' успішно скопійовано до '{new_file}'.")
#     except Exception as e:
#         print(f"Виникла помилка: {e}")
#
# source_file = 'example.txt'
# new_file = 'destination.txt'
# copy_to_file(source_file, new_file)

# '''
#     Task 4
#     Розробіть програму, яка визначає кількість слів у текстовому файлі. count_words(path_to_file)
# '''
# print("____________________")
# print("Task 4")
#
# from pathlib import Path
# import re
# import unicodedata
#
# def count_words(path_to_file):
#     try:
#         file_path = Path(path_to_file)
#         if not file_path.is_file():
#             print(f"Файл '{path_to_file}' не знайдено.")
#             return
#
#         encodings = ['utf-8', 'utf-16', 'utf-32', 'latin-1']
#         for encoding in encodings:
#             try:
#                 with open(file_path, 'r', encoding=encoding) as f:
#                     text = f.read()
#                 break
#             except UnicodeDecodeError:
#                 continue
#         else:
#             print("Не вдалося визначити кодування файлу.")
#             return
#
#         word_candidates = re.findall(r'\b\w+\b', text, flags=re.UNICODE)
#
#         words = [
#             word for word in word_candidates
#             if all(unicodedata.category(char).startswith('L') for char in word)
#         ]
#
#         num_words = len(words)
#         unique_words = set(words)
#         num_unique_words = len(unique_words)
#
#         print(f"Загальна кількість слів у файлі '{path_to_file}': {num_words}")
#         print(f"Кількість унікальних слів у файлі '{path_to_file}': {num_unique_words}")
#
#         return num_words, num_unique_words
#
#     except Exception as e:
#         print(f"Виникла помилка: {e}")
#         return
#
# path_to_file = 'example.txt'
# count_words(path_to_file)

# '''
#     Task 5
#     Створіть скрипт, який видаляє текстовий файл. remove_file(path_file). Повертає помилку якщо файла не існує/
# '''
# print("____________________")
# print("Task 5")
#
# from pathlib import Path
#
# def remove_file(path_file):
#     file_path = Path(path_file)
#     try:
#         file_path.unlink()
#         print(f"Файл '{path_file}' успішно видалено.")
#     except Exception as e:
#         print(f"Виникла помилка при видаленні файлу: {e}")
#         raise
#
# path_file = Path('delete_me.txt')
# if path_file.is_file():
#     remove_file(path_file)
# else:
#     print(f"Файл '{path_file}' не знайдено.")

# '''
#     Task 6
#     Напишіть програму, яка додає новий рядок до існуючого текстового файлу add_data_to_file(path_file , text).
# '''
# print("____________________")
# print("Task 6")
#
# from pathlib import Path
#
# def add_data_to_file(path_file, text):
#     file_path = Path(path_file)
#     if not file_path.is_file():
#         raise FileNotFoundError(f"Файл '{path_file}' не знайдено.")
#
#     try:
#         with file_path.open('a', encoding='utf-8') as file:
#             file.write(text + '\n')
#         print(f"Текст успішно додано до файлу '{path_file}'.")
#     except Exception as e:
#         print(f"Виникла помилка при додаванні тексту до файлу: {e}")
#         raise
#
# path_file = 'example.txt'
# text = 'Новий рядок тексту'
# add_data_to_file(path_file, text)

# '''
#     Task 7
#     Розробіть скрипт, який перевіряє наявність файлу за заданим ім'ям та повідомляє
#     користувача про результат. функція має повертати True/False
# '''
# print("____________________")
# print("Task 7")
#
# from pathlib import Path
#
# def check_file_exists(file_name):
#     file_path = Path(file_name)
#     if file_path.is_file():
#         print(f"Файл '{file_name}' існує.")
#         return True
#     else:
#         print(f"Файл '{file_name}' не знайдено.")
#         return False
#
# file_name = 'example.txt'
# print(check_file_exists(file_name))

# '''
#     Task 8
#     Створіть програму, яка шукає вказаний текст у файлі та виводить номери рядків,
#     де цей текст знаходиться find_text(path_file, search_text )
# '''
# print("____________________")
# print("Task 8")
#
# from pathlib import Path
#
# def find_text(path_file, search_text):
#     try:
#         file_path = Path(path_file)
#         if not file_path.is_file():
#             raise FileNotFoundError(f"Файл '{path_file}' не знайдено.")
#
#         with file_path.open('r', encoding='utf-8') as file:
#             lines = file.readlines()
#
#         found = False
#         for line_number, line in enumerate(lines, start=1):
#             if search_text in line:
#                 print(f"Текст '{search_text}' знайдено в рядку {line_number}:")
#                 found = True
#
#         if not found:
#             print(f"Текст '{search_text}' не знайдено у файлі '{path_file}'.")
#
#     except Exception as e:
#         print(f"Виникла помилка: {e}")
#         raise
#
# path_file = 'example.txt'
# search_text = 'скрипт'
# find_text(path_file, search_text)

# '''
#     Task 9
#     Напишіть скрипт, який сортує вміст текстового файлу за алфавітом і зберігає відсортований результат
#     у новому файлі. sort_data_in_file(file_path). Резульаттом має бути новий файл з наступною
#     назвою {file_path}_sorted
# '''
# print("____________________")
# print("Task 9")
#
# from pathlib import Path
#
# def sort_data_in_file(file_path):
#     try:
#         original_file = Path(file_path)
#
#         if not original_file.is_file():
#             raise FileNotFoundError(f"Файл '{file_path}' не знайдено.")
#
#         with original_file.open('r', encoding='utf-8') as f:
#             lines = f.readlines()
#
#         sorted_lines = sorted(lines)
#         sorted_file_name = f"{original_file.stem}_sorted.txt"
#         sorted_file_path = original_file.parent / sorted_file_name
#
#         with sorted_file_path.open('w', encoding='utf-8') as f:
#             f.writelines(sorted_lines)
#
#         print(f"Відсортований вміст збережено у файлі '{sorted_file_path}'.")
#
#     except Exception as e:
#         print(f"Виникла помилка: {e}")
#         raise
#
# file_path = 'example.txt'
# sort_data_in_file(file_path)

# '''
#     Task 10
#     Розробіть функцію, яка перевіряє розмір файлу і повідомляє користувача, чи він
#     перевищує заданий ліміт. is_greater_size(file_path, limit)
# '''
# print("____________________")
# print("Task 10")
#
# from pathlib import Path
#
# def is_greater_size(file_path, limit):
#     try:
#         path = Path(file_path)
#         if not path.is_file():
#             raise FileNotFoundError(f"Файл '{file_path}' не знайдено.")
#
#         file_size = path.stat().st_size  # Розмір файлу в байтах
#
#         if file_size > limit:
#             print(f"Розмір файлу '{file_path}' ({file_size} байт) перевищує ліміт {limit} байт.")
#             return True
#         else:
#             print(f"Розмір файлу '{file_path}' ({file_size} байт) не перевищує ліміт {limit} байт.")
#             return False
#
#     except Exception as e:
#         print(f"Виникла помилка: {e}")
#         raise
#
# file_path = 'example.txt'
# limit = 1024
# is_greater_size(file_path, limit)
#
# '''
#     Task 11
#     Напишіть скрипт для копіювання усіх файлів з одного каталогу в інший. copy_folder(from_folder , to_folder)
# '''
# print("____________________")
# print("Task 11")
#
# from pathlib import Path
# import shutil
#
# def copy_folder(from_folder, to_folder):
#     try:
#         src_path = Path(from_folder)
#         dest_path = Path(to_folder)
#
#         if not src_path.is_dir():
#             raise NotADirectoryError(f"Каталог '{from_folder}' не знайдено або це не директорія.")
#
#         dest_path.mkdir(parents=True, exist_ok=True)
#
#         for item in src_path.iterdir():
#             if item.is_file():
#                 shutil.copy2(item, dest_path / item.name)
#
#         print(f"Усі файли з '{from_folder}' успішно скопійовано до '{to_folder}'.")
#
#     except Exception as e:
#         print(f"Виникла помилка: {e}")
#         raise
#
# from_folder = 'source_folder'
# to_folder = 'destination_folder'
# copy_folder(from_folder, to_folder)

# '''
#     Task 12
#     Створіть функцію, яка читає CSV-файл і виводить на екран лише певні стовпці.
# '''
# print("____________________")
# print("Task 12")
#
# import csv
#
# def print_csv_columns(file_path, columns):
#     try:
#         with open(file_path, mode='r', encoding='utf-8') as csvfile:
#             reader = csv.DictReader(csvfile)
#             if not reader.fieldnames:
#                 print("CSV-файл не містить заголовків стовпців.")
#                 return
#
#             if isinstance(columns[0], int):
#                 headers = reader.fieldnames
#                 columns_to_print = [headers[i] for i in columns]
#             else:
#                 columns_to_print = columns
#
#             for row in reader:
#                 selected_data = [row[col] for col in columns_to_print if col in row]
#                 print(selected_data) # Варіант 1 виводу
#                 selected_data_1 = [row[col] for col in columns_to_print if col in row]
#                 print(', '.join(selected_data_1)) # Варіант 2 виводу
#
#     except FileNotFoundError:
#         print(f"Файл '{file_path}' не знайдено.")
#     except Exception as e:
#         print(f"Виникла помилка: {e}")
#
# file_path = 'data.csv'
# columns = ['Name', 'Age']
# print_csv_columns(file_path, columns)

'''
    Task 13
    Створіть функцію, яка читає CSV-файл і виводить на екран лише певні стовпці.
'''
print("____________________")
print("Task 13")

