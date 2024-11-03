import tkinter as tk
from tkinter import ttk
import random
import time
import threading

import tkinter as tk
from tkinter import ttk


class ProgressBarApp:
    def __init__(self, root, max_length):
        self.root = root
        self.max_length = max_length
        self.current_length = 0

        # Настраиваем интерфейс
        self.root.title("Прогресс Бар")
        self.progress_bar = ttk.Progressbar(self.root, maximum=self.max_length)
        self.progress_bar.pack(pady=20)

        self.button = tk.Button(self.root, text="Добавить 1", command=self.update_progress)
        self.button.pack(pady=10)

        self.label = tk.Label(self.root, text=f"Прогресс: {self.current_length}/{self.max_length}")
        self.label.pack(pady=10)

    def update_progress(self):
        if self.current_length < self.max_length:
            self.current_length += 1
            self.progress_bar['value'] = self.current_length
            self.label['text'] = f"Прогресс: {self.current_length}/{self.max_length}"

        if self.current_length >= self.max_length:
            self.button.config(state=tk.DISABLED)  # Отключаем кнопку



max_length = 100  # Максимальная длина прогресса
root = tk.Tk()
app = ProgressBarApp(root, max_length)
root.mainloop()

# class ProgressBar:
#     def __init__(self, root, array_length):
#         self.root = root
#         self.array_length = array_length
#         self.current_value = 0  # Начальное значение прогресса
#
#         # Создаем виджет Progressbar
#         self.progress_bar = ttk.Progressbar(root, orient='horizontal', length=300, mode='determinate')
#         self.progress_bar.pack(pady=20)
#
#     def update_progress(self, value):
#         """Обновляет прогресс-бар, добавляя к текущему значению новое значение"""
#         if self.current_value < self.array_length:
#             self.current_value += value
#             self.current_value = min(self.current_value, self.array_length)  # Ограничиваем текущее значение
#             self.progress_bar['value'] = (self.current_value / self.array_length) * 100
#             self.root.update_idletasks()  # Обновляем интерфейс
#
# class ExternalClass:
#     def __init__(self, progress_bar):
#         self.progress_bar = progress_bar
#
#     def start_sending_numbers(self):
#         """Имитация отправки чисел в прогресс-бар"""
#         for _ in range(10):  # Планируем отправку 10 значений
#             time.sleep(1)  # Задержка между отправками
#             self.send_number(random.randint(1, 10))  # Отправляем случайное число от 1 до 10
#
#     def send_number(self, value):
#         """Отправляет новое число в прогресс-бар"""
#         print(f"Отправлено число: {value}")
#         self.progress_bar.update_progress(value)
#
#
# root = tk.Tk()
# array_length = 100  # Максимальная длина прогресс-бара
# progress_bar = ProgressBar(root, array_length)
#
# # Запускаем внешний класс в отдельном потоке, чтобы не блокировать GUI
# external_class = ExternalClass(progress_bar)
# threading.Thread(target=external_class.start_sending_numbers).start()
#
# root.mainloop()

# import os
# import datetime, time
#
# import tkinter as tk
# from tkinter import ttk
# import time
#
# class ProgressBar:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Полоса загрузки")
#
#         # Создаем виджет Progressbar
#         self.progress_bar = ttk.Progressbar(root, orient='horizontal', length=300, mode='determinate')
#         self.progress_bar.pack(pady=20)
#
#         # Создаем кнопку для запуска загрузки
#         start_button = tk.Button(root, text="Начать загрузку", command=self.start_loading)
#         start_button.pack(pady=10)
#
#     def start_loading(self):
#         # Запускаем процесс обновления полосы загрузки в отдельном потоке
#         threading.Thread(target=self.loading).start()
#
#     def loading(self):
#         # Запускаем процесс обновления полосы загрузки
#         self.progress_bar['value'] = 0  # Сбрасываем полосу загрузки
#         for i in range(1001):  # Итерируем от 0 до 1000
#             time.sleep(0.01)  # Задержка для имитации обработки
#             self.progress_bar['value'] = i  # Обновляем значение полосы загрузки
#             self.root.update_idletasks()  # Обновляем интерфейс
#
#
# root = tk.Tk()
# progress_bar = ProgressBar(root)
# root.mainloop()

# # Укажите путь к вашему файлу
# DIRECTORY = '/Users/vladislavlipkin/Documents/work_path/'
#
# for file in os.listdir(DIRECTORY):
#     if file.endswith(".xlsx"):
#         print(f'{DIRECTORY}{file}')
#         # book = openpyxl.open(f"{self.DIRECTORY}{file}", read_only=True)
#         # sheet = book.active
#         timestamp = os.path.getmtime(f'{DIRECTORY}{file}')
#         print(timestamp)
#         time = datetime.datetime.fromtimestamp(timestamp)
#         print(time)
# def get_last_modified_time(file_path):
#     # Получаем время последнего изменения файла
#     return os.path.getmtime(file_path)
#
# # Сохраняем время последнего изменения файла
# last_modified_time = get_last_modified_time(DIRECTORY)

# Ваша логика проверки файла
# while True:
#     time.sleep(10)  # Например, проверяем каждые 10 секунд
#
#     current_modified_time = get_last_modified_time(DIRECTORY)
#
#     if current_modified_time != last_modified_time:
#         print("Файл изменился, выполняем нужные действия...")
#         # Здесь добавьте вашу логику, например, скачать файл заново
#         last_modified_time = current_modified_time  # Обновляем время последнего изменения
#     else:
#         print("Файл не изменился, ничего не делаем.")

import openpyxl
import re
import os
#
# directory = "/Users/vladislavlipkin/Desktop/data/"
# for file in os.listdir(directory):
#     if file.endswith(".xlsx"):
#         print(file)
#         book = openpyxl.open(f"/Users/vladislavlipkin/Desktop/data/{file}", read_only=True)
#         sheet = book.active
#
#         search_number = re.sub("[^0-9]", "", input("Введите номер: "))
#         for row in sheet:
#             if row[0].value == "$":
#                 equipment_name = str(row[1].value)
#             number = re.sub("[^0-9]", "",  str(row[1].value))
#             if number == search_number:
#                 print(f"оборудование {equipment_name}, номер телефона {str(row[1].value)}, номер бокса {str(row[0].value)}, "
#                       f"адрес кросс. параллели {str(row[3].value)}")
#

# book = openpyxl.open("table.xlsx", read_only=True)


# phone = input("Введите номер телефона:")
# convert = ''
# flag = True
# for num in phone:
#     if flag:
#         convert += num
#         convert += "-"
#         flag = False
#     else:
#         convert += num
#         flag = True
#
# convert = convert.rstrip("-")
# for row in range(1, 708):
#     if sheet[row][1].value == convert:
#         print(f"Строка: {row}")
#
# for row in sheet:
#     if row[0].value == "$":
#         print(row[1].value)