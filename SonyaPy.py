import serial
import time

# Настройка соединения с Arduino
arduino = serial.Serial(port='COM12', baudrate=9600, timeout=1)  # Укажите ваш COM порт

time.sleep(2)  # Подождите 2 секунды для установления соединения

# Функция для отправки команды на Arduino
def send_command(command):
    arduino.write(command.encode())
    print(f"Sent command: {command}")
    time.sleep(0.5)


# Основной цикл для управления светодиодом
while True:
    user_input = input("Enter '1' to turn ON the LED, '0' to turn OFF (or 'exit' to quit): ")

    if user_input == '1' or user_input == '0':
        send_command(user_input)
    elif user_input.lower() == 'exit':
        print("Exiting...")
        break
    else:
        print("Invalid input. Please enter '1' or '0'.")

# Закрытие соединения
arduino.close()
