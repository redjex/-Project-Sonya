import customtkinter as ctk
from tkinter import messagebox
import os

class RegistrationApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Registration and Login App")
        self.geometry("400x350")

        # Устанавливаем начальную тему
        self.current_theme = "dark"
        ctk.set_appearance_mode(self.current_theme)

        self.frame = ctk.CTkFrame(self)
        self.frame.pack(pady=20, padx=20, fill="both", expand=True)
        # Создаем заголовок
        self.label = ctk.CTkLabel(self.frame, text="Registration and Login", font=("Arial", 20))
        self.label.pack(pady=20)

        # Поле для ввода логина
        self.entry_login = ctk.CTkEntry(self.frame, placeholder_text="Login", width=250)
        self.entry_login.pack(pady=10)

        # Поле для ввода пароля
        self.entry_password = ctk.CTkEntry(self.frame, placeholder_text="Password", show="*", width=250)
        self.entry_password.pack(pady=10)

        # Кнопка для регистрации
        self.register_button = ctk.CTkButton(self.frame, text="Register", command=self.register)
        self.register_button.pack(pady=10)

        # Кнопка для входа
        self.login_button = ctk.CTkButton(self.frame, text="Login", command=self.login)
        self.login_button.pack(pady=10)

        # Переключатель темы
        self.theme_switch = ctk.CTkSwitch(self.frame, text="Dark Mode", command=self.toggle_theme)
        self.theme_switch.pack(pady=10)

    def register(self):
        login = self.entry_login.get()
        password = self.entry_password.get()

        if login and password:
            with open("login.txt", "a") as file:
                file.write(f"Login: {login} Password: {password}\n")
            messagebox.showinfo("Registration Successful", "Your data has been saved.")
            self.entry_login.delete(0, 'end')
            self.entry_password.delete(0, 'end')
        else:
            messagebox.showwarning("Input Error", "Please enter both login and password.")

    def login(self):
        login = self.entry_login.get()
        password = self.entry_password.get()

        if login and password:
            with open("login.txt", "r") as file:
                users = file.readlines()
                for user in users:
                    if f"Login: {login} Password: {password}" in user:
                        messagebox.showinfo("Login Successful", "Login successful! Opening main.py...")
                        self.open_main()
                        return

            messagebox.showerror("Login Failed", "Incorrect login or password.")
        else:
            messagebox.showwarning("Input Error", "Please enter both login and password.")

    def open_main(self):
        try:
            os.system("python main.py")  # Открываем файл main.py
            self.destroy()  # Закрываем текущее окно после открытия main.py
        except Exception as e:
            messagebox.showerror("Error", f"Could not open main.py: {e}")

    def toggle_theme(self):
        if self.current_theme == "light":
            self.current_theme = "dark"
            ctk.set_appearance_mode("dark")
            self.theme_switch.configure(text="Light Mode")
        else:
            self.current_theme = "light"
            ctk.set_appearance_mode("light")
            self.theme_switch.configure(text="Dark Mode")

if __name__ == "__main__":
    app = RegistrationApp()
    app.mainloop()
