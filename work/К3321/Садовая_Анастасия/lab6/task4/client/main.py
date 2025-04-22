import socket
import threading

# Настройки подключения
HOST = '127.0.0.1'
PORT = 1234

# Получение сообщений от сервера
def receive_messages(sock):
    while True:
        try:
            message = sock.recv(1024).decode('utf-8')
            print(message)
        except:
            print("Ошибка соединения с сервером.")
            sock.close()
            break

# Отправка сообщений на сервер
def send_messages(sock):
    while True:
        message = input()
        try:
            sock.send(message.encode('utf-8'))
        except:
            print("Не удалось отправить сообщение.")
            break

# Подключение к серверу
def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    print("Подключен к чату. Пиши сообщения:")

    threading.Thread(target=receive_messages, args=(client,), daemon=True).start()

    send_messages(client)

if __name__ == "__main__":
    start_client()