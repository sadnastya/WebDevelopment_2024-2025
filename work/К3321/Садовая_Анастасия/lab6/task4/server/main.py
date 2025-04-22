import socket
import threading

HOST = '127.0.0.1'
PORT = 1234

clients = []
client_ids = {}
client_id_counter = 1
lock = threading.Lock()

def broadcast(message, sender_socket):
    for client in clients:
        try:
            if client != sender_socket:
                client.send(f"{client_ids[sender_socket]}: {message}".encode('utf-8'))
        except:
            clients.remove(client)

def handle_client(client_socket):
    global client_id_counter
    with lock:
        client_ids[client_socket] = f"User{client_id_counter}"
        client_id_counter += 1

    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            broadcast(message, client_socket)
        except:
            clients.remove(client_socket)
            break

    with lock:
        print(f"[ОТКЛЮЧЕНО] {client_ids[client_socket]}")
        del client_ids[client_socket]
        client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"[СЕРВЕР ЗАПУЩЕН] {HOST}:{PORT}")

    while True:
        client_socket, addr = server.accept()
        print(f"[ПОДКЛЮЧЕНИЕ] {addr}")
        clients.append(client_socket)
        threading.Thread(target=handle_client, args=(client_socket,), daemon=True).start()

if __name__ == "__main__":
    start_server()

