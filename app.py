from search_file import Search_number
from tkinter import ttk
import tkinter as tk
from tkinter import scrolledtext, ttk
from tkinter import Label
from tkinter import StringVar
from tkinter import Entry
from tkinter import Button
from tkinter import messagebox
from functools import partial

import re


class Window_login_pass:

    def __init__(self):
        # Window
        
        tkWindow = tk.Tk()
        self.dest = tkWindow
        w = tkWindow.winfo_screenwidth()
        h = tkWindow.winfo_screenheight()
        w = w // 2  # середина экрана
        h = h // 2
        w = w - 300  # смещение от середины
        h = h - 200
        tkWindow.geometry(f'400x150+{w}+{h}')
        tkWindow.title('- Введите логин и пароль учетной записи -')

        # Username label and text entry box
        self.usernameLabel = Label(tkWindow, text="Логин").grid(row=0, column=0)
        self.username = StringVar()
        self.usernameEntry = Entry(tkWindow, textvariable=self.username).grid(row=0, column=1)

        # Password label and password entry box
        self.passwordLabel = Label(tkWindow, text="Пароль").grid(row=1, column=0)
        self.password = StringVar()
        self.passwordEntry = Entry(tkWindow, textvariable=self.password, show='*').grid(row=1, column=1)

        # pass arguments from button
        self.validateLogin = partial(self.validateLogin)

        # Login button
        self.loginButton = Button(tkWindow, text="Login", command=self.validateLogin).grid(row=4, column=0)

        # NEW
        tkWindow.bind('<Return>', self.on_enter)

        tkWindow.mainloop()


    # NEW
    def on_enter(self, event):
        print('OKAY')
        self.validateLogin()

    def validateLogin(self):
        login = self.username.get()
        passw = self.password.get()
        print('SUCCEFUL CONECTION')
        #conn = smbconnect.SMBConnect(login, passw)
        #print(conn.connect())
        # if conn.connect():
        #     conn.download()
        #     self.showMsg_succefull()
        #     self.dest.destroy()
        #     Window_search_file()

        # else:
        #     self.showMsg_error()
        self.showMsg_succefull()
        self.dest.destroy()
        Window_search_file()

    def showMsg_error(self):
        messagebox.showinfo('ошибка!','Неправильный логин или пароль!')
        
        
    
    def showMsg_succefull(self):
        messagebox.showinfo('успешно','вход произведен!')


class Window_search_file:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Система вывода информации абонента")

        # Получаем размеры экрана и располагаем окно по центру
        w = self.root.winfo_screenwidth()
        h = self.root.winfo_screenheight()
        w = w // 2  # середина экрана
        h = h // 2
        w = w - 300  # смещение от середины
        h = h - 200
        self.root.geometry(f'600x400+{w}+{h}')

        # Настройки стиля ttk
        self.style = ttk.Style()
        self.style.configure('TLabel', font=('Arial', 12), padding=5)  # Уменьшили отступы
        self.style.configure('TButton', font=('Arial', 12), padding=10)

        # Создаем метку для ввода номера
        self.input_label = ttk.Label(self.root, text="Введите искомый номер:")
        self.input_label.pack(pady=20)

        # Создаем поле ввода
        self.input_entry = ttk.Entry(self.root, font=('Arial', 12), width=40)
        self.input_entry.pack(pady=10)

        # Создаем кнопку поиска
        self.submit_button = ttk.Button(self.root, text="Поиск", command=self.show_output)
        self.submit_button.pack(pady=10)

        # Создаем фрейм с прокруткой для вывода результатов
        self.output_frame = ttk.Frame(self.root)
        self.output_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Добавляем Canvas для создания прокручиваемой области
        self.canvas = tk.Canvas(self.output_frame)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Добавляем Scrollbar и привязываем его к Canvas
        self.scrollbar = ttk.Scrollbar(self.output_frame, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Внутренний фрейм, который будет размещаться внутри Canvas
        self.inner_frame = ttk.Frame(self.canvas)

        # Создаем окно внутри Canvas для размещения виджетов
        self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw")

        # Обновляем размеры Canvas при изменении размера содержимого
        self.inner_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        # Привязываем событие прокрутки колесиком мыши для Windows и Linux
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

        # Привязываем событие прокрутки для macOS
        self.canvas.bind_all("<Button-4>", self._on_mousewheel)
        self.canvas.bind_all("<Button-5>", self._on_mousewheel)

        # Привязываем нажатие Enter к функции поиска
        self.root.bind('<Return>', self.on_enter)

        self.root.mainloop()

    def _on_mousewheel(self, event):
        # Для Windows и Linux
        if event.num == 4 or event.delta > 0:
            self.canvas.yview_scroll(-1, "units")  # прокрутка вверх
        elif event.num == 5 or event.delta < 0:
            self.canvas.yview_scroll(1, "units")  # прокрутка вниз

    def on_enter(self, event):
        self.show_output()

    def show_output(self):
        # Получаем введенный текст и очищаем его от символов, кроме цифр
        input_text = self.input_entry.get()
        search_number = re.sub("[^0-9]", "", input_text)

        # Имитируем результат поиска через ваш класс Search_number
        enemy = Search_number(search_number)  # ваш класс для поиска номера
        enemy.read_path_file()  # вызов метода для чтения данных из файла
        result = enemy.output()  # получаем результат поиска

        # Очищаем старые метки с результатами
        for widget in self.inner_frame.winfo_children():
            widget.destroy()

        # Построчно добавляем результат
        if result:
            for row in result:
                row_label = ttk.Label(self.inner_frame, text=row, wraplength=500, justify=tk.LEFT)
                row_label.pack(anchor='w', pady=2)  # Уменьшили отступы между строками
        else:
            error_label = ttk.Label(self.inner_frame, text="Номер не найден", wraplength=500, justify=tk.LEFT)
            error_label.pack(anchor='w', pady=2)  # Уменьшили отступы между строками

# class Window_search_file:
#     def __init__(self):
#         root = tk.Tk()
#         w = root.winfo_screenwidth()
#         h = root.winfo_screenheight()
#         w = w // 2  # середина экрана
#         h = h // 2
#         w = w - 300  # смещение от середины
#         h = h - 200
#         root.geometry(f'600x400+{w}+{h}')
#
#
#         self.root = root
#         self.root.title("Система вывода информации абонента")
#
#         self.input_label = tk.Label(self.root, text="Введите искомый номер:")
#         self.input_label.pack()
#
#         self.input_entry = tk.Entry(self.root)
#         self.input_entry.pack()
#
#         self.submit_button = tk.Button(self.root, text="поиск", command=self.show_output)
#         self.submit_button.pack()
#         self.output_text = scrolledtext.ScrolledText(self.root, wrap=tk.WORD)
#
#         # NEW
#         root.bind('<Return>', self.on_enter)
#
#         root.mainloop()
#
#     # NEW
#     def on_enter(self, event):
#         self.show_output()
#
    # def show_output(self):
    #     input_text = self.input_entry.get()
    #     search_number = re.sub("[^0-9]", "", input_text)
    #     enemy = Search_number(search_number)
    #     enemy.read_path_file()
    #     result = enemy.output()
    #
    #
    #     for row in result:
    #         self.output_text.insert(tk.END, f"{row}\n")
    #         self.output_text.pack()

class ProgressBarApp:
    def __init__(self, root, max_length):
        # Создаем дочернее окно для прогресс-бара
        self.progress_window = tk.Toplevel(root)
        self.max_length = max_length
        self.current_length = 0

        w = self.progress_window.winfo_screenwidth()
        h = self.progress_window.winfo_screenheight()
        w = w // 2  # середина экрана
        h = h // 2
        w = w - 300  # смещение от середины
        h = h - 200
        self.progress_window.geometry(f'250x100+{w}+{h}')

        # Настраиваем интерфейс
        self.progress_window.title("Прогресс Бар")
        self.progress_bar = ttk.Progressbar(self.progress_window, maximum=self.max_length)
        self.progress_bar.pack(pady=20)

        self.label = tk.Label(self.progress_window, text=f"Прогресс: {self.current_length}/{self.max_length}")
        self.label.pack(pady=10)

    def update_progress(self):
        if self.current_length < self.max_length:
            self.current_length += 1
            self.progress_bar['value'] = self.current_length
            self.label['text'] = f"Прогресс: {self.current_length}/{self.max_length}"

    def close(self):
        self.progress_window.destroy()  # Закрыть только окно прогресс-бара

