import socket

def calculate_area(a, b, h):
    return (a + b) * h / 2

def handle_client(conn):
    with conn:
        data = conn.recv(1024).decode('utf-8')
        a, b, h = map(float, data.split(','))
        
        area = calculate_area(a, b, h)
        conn.sendall(f"{area:.2f}".encode('utf-8'))

def main():
    HOST = '127.0.0.1'
    PORT = 1234
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print("Сервер запущен и ожидает подключений...")
        
        while True:
            conn, addr = s.accept()
            print(f"Подключен клиент: {addr}")
            handle_client(conn)
            print("Расчет завершен, соединение закрыто")

if __name__ == "__main__":
    main()