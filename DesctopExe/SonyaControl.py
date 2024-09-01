import customtkinter as ctk
import serial
import time
from tkinter import messagebox
import random
from tkinter import PhotoImage


class CustomApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.current_theme = "dark"
        ctk.set_appearance_mode(self.current_theme)
        self.title("LED Control App")
        self.geometry("1000x550")
        self.iconbitmap("C:\\Users\\micha\\OneDrive\\Рабочий стол\\Sonya\\home.ico")
        self.configure(bg='#f0f0f0')
        self.resizable(False, False)
        # Подключение к Arduino
        try:
            self.arduino = serial.Serial(port='COM12', baudrate=9600, timeout=1)  # Укажите свой COM порт
            time.sleep(2)  # Подождите немного для установления соединения
        except Exception as e:
            messagebox.showerror("Connection Error", f"Could not connect to Arduino: {e}")
            self.destroy()  # Закрываем приложение, если не удается подключиться
        # Создаем кнопку для включения светодиода
        self.grid_rowconfigure(1, weight=0)
        self.grid_columnconfigure(1, weight=0)
        self.frame = ctk.CTkFrame(
            self,
            width=500,
            height=1000,
            fg_color="#A5A5A5",  # Цвет фона фрейма
            corner_radius=5  # Скругление углов фрейма
        )

        # Размещаем Frame в окне
        self.frame.grid(padx=0, pady=0, row=0, column=0, sticky="n")

        # Добавляем виджеты внутрь Frame
        self.label = ctk.CTkLabel(master=self.frame, text="Это CTkLabel", text_color="white")
        self.label.grid(pady=10, padx=20, row=0, column=0, sticky="n")
        self.optionmenu = ctk.CTkOptionMenu(
        self.frame,
        values=["Глазки","Радость", "Грусть", "Левый глаз", "Правый глаз"],
        command=self.optionmenu_callback,  # Функция, вызываемая при изменении выбора
        font = ("Arial", 14),
        fg_color = '#000000',  # Красный цвет для выключения
        button_hover_color="#171717",  # Цвет кнопки при наведении
        button_color = '#000000'
        )
        # Задаем начальное значение
        self.optionmenu.set("Эмоции")
        self.optionmenu.grid(pady=10, padx=10, row=1, column=0)
        self.button_settings = ctk.CTkButton(
            self.frame,
            text="Settings",
            command=self.settings,
            font=("Arial", 14),
            fg_color='#000000',  # Красный цвет для выключения
            hover_color='#171717'
        )
        self.button_settings.grid(pady=10, padx=10, row=2, column=0)
        self.button_off = ctk.CTkButton(
            self,
            text="RGB ON",
            command=self.rgb,
            font=("Arial", 14),
            fg_color='#000000',  # Красный цвет для выключения
            hover_color='#171717'
        )
        self.button_off.grid(pady=0, padx=0, row=1, column=6)

        self.button_off = ctk.CTkButton(
            self,
            text="RGB OFF",
            command=self.rgb_off,
            font=("Arial", 14),
            fg_color='#000000',  # Красный цвет для выключения
            hover_color='#171717'
        )
        self.button_off.grid(pady=0, padx=0, row=1, column=7)

        self.button_off = ctk.CTkButton(
            self,
            text="Exit",
            command=self.on_closing,
            font=("Arial", 14),
            fg_color='#000000',  # Красный цвет для выключения
            hover_color='#171717'
        )
        self.button_off.grid(pady=490, padx=0, row=4, column=7)

        self.theme_switch = ctk.CTkSwitch(self, text="Light Mode", command=self.toggle_theme)
        self.theme_switch.grid(pady=460, padx=0, row=4, column=6)
    def settings(self):
        for widget in self.winfo_children():
            widget.destroy()
    def optionmenu_callback(self, choice):
        if choice == "Радость":
            self.send_command('2')
        elif choice == "Грусть":
            self.send_command('3')
        elif choice == "Левый глаз":
            self.send_command('0')
        elif choice == "Правый глаз":
            self.send_command('1')
        elif choice == "Глазки":
            self.send_command('6')
    def toggle_theme(self):
        if self.current_theme == "dark":
            self.current_theme = "light"
            ctk.set_appearance_mode("light")
            self.theme_switch.configure(text="Dark Mode")
        else:
            self.current_theme = "dark"
            ctk.set_appearance_mode("dark")
            self.theme_switch.configure(text="Light Mode")

    def random(self):
        random_number = random.randint(0, 3)
        # Отправка сгенерированного числа в функцию send_command
        for i in range(3):
            self.send_command(random_number)
    def rgb(self):
        self.send_command('4')

    def rgb_off(self):
        self.label = ctk.CTkLabel(self, text="Подождите 15 секунд")
        self.label.grid(pady=0, padx=0, row=1, column=7)
        self.send_command('5')
        self.button_off.grid(pady=462, padx=0, row=4, column=7)

    def send_command(self, command):
        try:
            self.arduino.write(f"{command}\n".encode())
            time.sleep(0.1)  # Небольшая задержка для обработки команды
        except Exception as e:
            messagebox.showerror("Communication Error", f"Error sending command to Arduino: {e}")

    def on_closing(self):
        try:
            self.arduino.close()
        except Exception as e:
            print(f"Error closing serial connection: {e}")
        self.destroy()

if __name__ == "__main__":
    app = CustomApp()
    app.protocol("WM_DELETE_WINDOW", app.on_closing)
    app.mainloop()
