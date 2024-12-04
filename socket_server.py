import socket

# Создаем серверный сокет
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Привязываем серверный сокет к localhost и порту 3030
server_socket.bind(('localhost', 3030))
server_socket.listen(1)  # Начинаем прослушивать входящие соединения
print("Сервер слушает порт 3030...")

# Принимаем входящее соединение
conn, addr = server_socket.accept()
print(f"Подключение установлено с {addr}")

while True:
    # Получаем данные от клиента
    data = conn.recv(1024)
    if not data:  # Если данных нет, завершаем цикл
        break
    conn.sendall(data)  # Отправляем данные обратно клиенту
    print(data.decode('utf-8'))  # Выводим информацию в консоль

conn.close()  # Закрываем соединение
