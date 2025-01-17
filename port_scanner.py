import socket

def scan_ports(host):
    print(f"Сканирование портов на {host}...")
    for port in range(1, 65536):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                s.connect((host, port))
                print(f"Порт {port} открыт")
        except:
            pass

if __name__ == "__main__":
    host = input("Введите имя хоста или IP-адрес: ")
    scan_ports(host)
