import openpyxl
import re
import os
from pathlib import Path
import tkinter as tk

import app

class Search_number:
    # initialization
    def __init__(self, search_number):
        self.search_number = search_number
        self.data = []

        # the root folder
        #self.DIRECTORY = r"C:/Users/Incognitus/PycharmProjects/project_for_anton/data/"
        self.DIRECTORY = "/Users/vladislavlipkin/PycharmProjects/project_for_anton/data/"


        # COUNT FILES
        self.path = Path(self.DIRECTORY)
        self.file_count = len(list(self.path.glob('*')))

    def read_path_file(self):
        root = tk.Tk()
        root.withdraw()
        UP = app.ProgressBarApp(root, self.file_count)

        print(f'len PROGRESS {self.file_count}')
        for file in os.listdir(self.DIRECTORY):
            if file.endswith(".xlsx"):
                book = openpyxl.open(f"{self.DIRECTORY}{file}", read_only=True)
                sheet = book.active
                print(f'READ FILE - {file}')
                # work
                # UP.update_progress()
                # UP.root.update()
                UP.update_progress()
                UP.progress_window.update()

                for row in sheet:
                    if row[0].value == "$":
                        key_name = row[1].value
                    left_number = re.sub("[^0-9]", "", str(row[1].value))
                    right_number = re.sub("[^0-9]", "", str(row[6].value))

                    if left_number == self.search_number:
                        self.data.append(str(
                            f"номер телефона {str(row[1].value)} - "  #номер 
                            f"расположение {key_name} - "  # расположение
                            f"пара {str(row[0].value)} - "  # пара 
                            f"адрес кросс.параллели {str(row[2].value)} - "  # адресс кросс 
                            f"помещение {str(row[3].value)} - "  # помещение 
                            f"( файла {file} )"))  # имя файла
                        self.data.append(str(""))

                    if right_number == self.search_number:
                        self.data.append(str(
                            f"номер телефона {str(row[6].value)} - "  # номер
                            f"расположение {key_name} - "  # расположение
                            f"пара {str(row[5].value)} - "  # пара
                            f"адрес кросс.параллели {str(row[7].value)} - "  # адресс кросс
                            f"помещение {str(row[8].value)} - "  # помещение 
                            f"( файл {file} )"))  # имя файла
                        self.data.append(str(""))

        UP.close()

    def output(self):
        if len(self.data) == 0:
            self.data.append(f"по запросу {self.search_number} ничего не найдено!")
            self.data.append(str(""))
        return self.data
