import socket
import threading

# Disponibilità iniziale taxi
disponibilita_taxi = 10
lock = threading.Lock()

def taxiInstance(conn, addr):
    global disponibilita_taxi
    print(f"Connessione stabilita con {addr}")

    try:
        while True:
            data = conn.recv(1024).decode()
            if not data:
                break

            # Controllo formato messaggio
            if "," not in data:
                conn.send("Formato non valido. Usa: Partenza,Arrivo".encode())
                continue

            partenza, arrivo = data.split(",")

            with lock:
                if disponibilita_taxi > 0:
                    disponibilita_taxi -= 1
                    response = (
                        f"Taxi disponibile!\n"
                        f"Partenza: {partenza}\n"
                        f"Arrivo: {arrivo}\n"
                        f"Taxi rimanenti: {disponibilita_taxi}"
                    )
                else:
                    response = "Nessun taxi disponibile al momento."

            conn.send(response.encode())

    except Exception as e:
        print("Errore:", e)

    conn.close()
    print(f"Connessione terminata con {addr}")

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 12345))
    server_socket.listen(5)

    print("🚖 Centrale Taxi attiva sulla porta 12345")

    while True:
        conn, addr = server_socket.accept()
        client_thread = threading.Thread(
            target=taxiInstance,
            args=(conn, addr)
        )
        client_thread.start()

if __name__ == "__main__":
    start_server()
