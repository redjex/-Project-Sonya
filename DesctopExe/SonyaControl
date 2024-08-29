import customtkinter as ctk
import serial
import time
from tkinter import messagebox


class CustomApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("dark")
        self.title("LED Control App")
        self.geometry("1000x550")
        self.configure(bg='#f0f0f0')

        # Подключение к Arduino
        try:
            self.arduino = serial.Serial(port='COM12', baudrate=9600, timeout=1)  # Укажите свой COM порт
            time.sleep(2)  # Подождите немного для установления соединения
        except Exception as e:
            messagebox.showerror("Connection Error", f"Could not connect to Arduino: {e}")
            self.destroy()  # Закрываем приложение, если не удается подключиться
        # Создаем кнопку для включения светодиода
        self.button_on = ctk.CTkButton(
            self,
            text="Left eye",
            command=self.turn_led_on,
            font=("Arial", 14),
            fg_color='#28a745',  # Зеленый цвет для включения
            hover_color='#218838'
        )
        self.button_on.pack(pady=20, anchor="nw")

        # Создаем кнопку для выключения светодиода
        self.button_off = ctk.CTkButton(
            self,
            text="Right eye",
            command=self.turn_led_off,
            font=("Arial", 14),
            fg_color='#dc3545',  # Красный цвет для выключения
            hover_color='#c82333'
        )
        self.button_off.pack(pady=20, anchor="nw")

        self.button_off = ctk.CTkButton(
            self,
            text="Blink",
            command=self.blink_led,
            font=("Arial", 14),
            fg_color='#000000',  # Красный цвет для выключения
            hover_color='#171717'
        )
        self.button_off.pack(pady=20, anchor="nw")

        self.button_off = ctk.CTkButton(
            self,
            text="Exit",
            command=self.on_closing,
            font=("Arial", 14),
            fg_color='#000000',  # Красный цвет для выключения
            hover_color='#171717'
        )
        self.button_off.pack(pady=150, anchor="se")

    def turn_led_on(self):
        self.send_command('1')

    def turn_led_off(self):
        self.send_command('0')

    def blink_led(self):
        self.send_command('2')

    def send_command(self, command):
        try:
            self.arduino.write(command.encode())
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
