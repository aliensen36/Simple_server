import socket

# Создаем клиентский сокет
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Подключаемся к серверу
try:
    s.connect(('localhost', 3030))
    print("Успешно подключено к серверу.")
    s.sendall(b'Привет, сервер!')  # Отправляем сообщение
    data = s.recv(1024)  # Получаем ответ от сервера
    print(f"Ответ от сервера: {data.decode('utf-8')}")
finally:
    s.close()  # Закрываем сокет
