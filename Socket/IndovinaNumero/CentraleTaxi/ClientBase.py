import socket

def start_client():
    # Inizializzazione socket client
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    while True:
        # Inserimento dati
        partenza = input("Inserisci città di partenza: ")
        arrivo = input("Inserisci città di arrivo: ")

        richiesta = partenza + "," + arrivo

        # Invio richiesta
        client_socket.sendall(richiesta.encode())

        # Ricezione risposta server
        data = client_socket.recv(1024).decode()
        print("\nRisposta dal server:")
        print(data)
        print("-----------------------")

    client_socket.close()

if __name__ == "__main__":
    start_client()
