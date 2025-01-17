import socket
import threading
from queue import Queue
from tqdm import tqdm

open_ports = []
lock = threading.Lock()

def scan_port(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            s.connect((host, port))
            with lock:
                open_ports.append(port)
    except:
        pass

def worker(host, port_queue, progress_bar):
    while not port_queue.empty():
        port = port_queue.get()
        scan_port(host, port)
        progress_bar.update(1)

def scan_ports_parallel(host, num_threads=100):
    print(f"Сканирование портов на {host}...")

    port_queue = Queue()
    for port in range(1, 65536):
        port_queue.put(port)

    progress_bar = tqdm(total=65535, desc="Сканирование портов", unit="порт")

    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=worker, args=(host, port_queue, progress_bar))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    progress_bar.close()
    open_ports.sort()
    print("Открытые порты:", open_ports)

if __name__ == "__main__":
    host = input("Введите имя хоста или IP-адрес: ")
    scan_ports_parallel(host)
