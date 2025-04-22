import socket

HOST = '127.0.0.1'
PORT = 1234

def handle_client(conn, addr):
    print(f'Новое подключение {addr}')
    
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            html_content = f.read()
            http_code = 200
    except FileNotFoundError:
        html_content = '<h1>Error: index.html not found</h1>'
        http_code = 404
    
    http_response = (
        f"HTTP/1.1 {http_code} OK\r\n"
        "Content-Type: text/html; charset=utf-8\r\n"
        f"Content-Length: {len(html_content.encode('utf-8'))}\r\n"
        "\r\n"
        f"{html_content}"
    )

    conn.sendall(http_response.encode('utf-8'))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f'Ожидание подключений на {HOST}:{PORT}')
    
    while True:
        conn, addr = s.accept()
        with conn:
            handle_client(conn, addr)
