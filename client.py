import socket

def start_client(host='127.0.0.1', port=65432):
    print("Попытка подключения к серверу...")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        print(f"Соединение с сервером {host}:{port} установлено.")

        try:
            while True:
                message = input("Введите сообщение (или 'exit' для выхода): ")
                client_socket.sendall(message.encode('utf-8'))
                print(f"Отправлено серверу: {message}")

                if message.lower() == 'exit':
                    print("Разрыв соединения с сервером...")
                    break

                response = client_socket.recv(1024)
                print(f"Ответ от сервера: {response.decode('utf-8')}")
        except KeyboardInterrupt:
            print("\nПринудительный разрыв соединения.")
        finally:
            print("Клиент завершил работу.")

if __name__ == "__main__":
    start_client()
