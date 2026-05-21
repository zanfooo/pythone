import socket
# Importa la libreria socket


def start_client():
    # Funzione principale del client

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Crea il socket del client
    # AF_INET = IPv4
    # SOCK_STREAM = protocollo TCP

    client.connect(("127.0.0.1", 5000))
    # Connette il client al server
    # 127.0.0.1 = localhost
    # 5000 = porta del server

    abbonamento = input("Inserisci abbonamento (mensile/annuale): ")
    # Chiede il tipo di abbonamento

    eta = input("Inserisci età: ")
    # Chiede l'età

    corsi = input("Inserisci numero corsi extra: ")
    # Chiede il numero di corsi extra

    client.sendall(abbonamento.encode())
    # Invia l'abbonamento al server

    client.sendall(eta.encode())
    # Invia l'età al server

    client.sendall(corsi.encode())
    # Invia il numero di corsi al server

    risposta = client.recv(1024).decode()
    # Riceve la risposta dal server

    print("Risposta dal server:", risposta)
    # Stampa il messaggio ricevuto

    client.close()
    # Chiude la connessione


if __name__ == "__main__":
    # Controlla se il file viene eseguito direttamente

    start_client()
    # Avvia il client
