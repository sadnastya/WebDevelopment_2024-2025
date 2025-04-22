import socket

sock = socket.socket()
sock.bind(('localhost', 9090))
sock.listen(1)
print("Сервер ожидает подключения...")
conn, addr = sock.accept()

print('Подключен клиент:', addr)

while True:
    data = conn.recv(1024).decode('utf-8')
    if not data:
        break
    print(f"Получено сообщение: {data}")
    
    conn.send("Hello, client!".encode('utf-8'))

conn.close()