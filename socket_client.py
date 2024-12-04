import socket

# Создаем клиентский сокет
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Подключаемся к серверу
try:
    s.connect(('localhost', 3030))
    print("Успешно подключено к серверу.")
    message = 'Привет, сервер!'  # Сообщение на русском
    s.sendall(message.encode('utf-8'))  # Кодируем сообщение в байты UTF-8
    data = s.recv(1024)  # Получаем ответ от сервера
    print(f"Ответ от сервера: {data.decode('utf-8')}")  # Декодируем байты обратно в строку
finally:
    s.close()  # Закрываем сокет
