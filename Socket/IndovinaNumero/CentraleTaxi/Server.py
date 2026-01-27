import socket
import threading

# Disponibilità iniziale taxi
disponibilita_taxi = 10

# Funzione istanza di servizio
def taxiInstance(conn, addr):
    global disponibilita_taxi
    print(f"Connessione stabilita con {addr}")

    while True:
        # Ricezione dati dal client
        data = conn.recv(1024).decode()

        # Se il client chiude la connessione
        if not data:
            break

        # Data contiene: città_partenza,città_arrivo
        partenza, arrivo = data.split(",")

        if disponibilita_taxi > 0:
            disponibilita_taxi -= 1
            response = (
                "Taxi disponibile!\n"
                f"Partenza: {partenza}\n"
                f"Arrivo: {arrivo}\n"
                f"Taxi rimanenti: {disponibilita_taxi}"
            )
        else:
            response = "Nessun taxi disponibile."

        # Invio risposta al client
        conn.send(response.encode())

    conn.close()
    print(f"Connessione terminata con {addr}")

def start_server():
    # Inizializzazione socket server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 12345))
    server_socket.listen(5)

    print("Server taxi in ascolto sulla porta 12345...")

    while True:
        conn, addr = server_socket.accept()
        client_thread = threading.Thread(
            target=taxiInstance,
            args=(conn, addr)
        )
        client_thread.start()

if __name__ == "__main__":
    start_server()
