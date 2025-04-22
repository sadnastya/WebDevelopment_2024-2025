import socket

def get_trapezoid_data():
    print("Введите параметры трапеции:")
    a = float(input("Основание a: "))
    b = float(input("Основание b: "))
    h = float(input("Высота h: "))
    return f"{a},{b},{h}"

def main():
    HOST = '127.0.0.1'
    PORT = 65432
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print("Соединение с сервером установлено")
        
        data = get_trapezoid_data()
        s.sendall(data.encode('utf-8'))
        
        result = s.recv(1024).decode('utf-8')
        print(f"Площадь трапеции: {result}")

if __name__ == "__main__":
    main()