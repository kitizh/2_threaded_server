import socket
import threading

def handle_client(client_socket, client_address):
    print(f"Клиент подключился: {client_address}")
    with client_socket:
        while True:
            data = client_socket.recv(1024)
            if not data:
                print(f"Клиент отключился: {client_address}")
                break
            message = data.decode('utf-8').strip()
            print(f"Получено от клиента {client_address}: {message}")
            client_socket.sendall(data)
            print(f"Отправлено клиенту {client_address}: {message}")

def start_server(host='127.0.0.1', port=65432):
    print("Запуск сервера...")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        print(f"Сервер привязан к {host}:{port}")
        server_socket.listen()
        print("Сервер слушает порт...")

        while True:
            client_socket, client_address = server_socket.accept()
            client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
            client_thread.daemon = True  # Поток завершится при завершении основной программы
            client_thread.start()

if __name__ == "__main__":
    try:
        start_server()
    except KeyboardInterrupt:
        print("\nСервер остановлен.")
