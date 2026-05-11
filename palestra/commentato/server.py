# Importiamo la libreria socket
import socket

# Importiamo la libreria threading
import threading


# Funzione che gestisce ogni client
def gestisci_client(client_socket):

    # Riceviamo il tipo di abbonamento
    abbonamento = client_socket.recv(1024).decode()

    # Riceviamo l'età del cliente
    eta = int(client_socket.recv(1024).decode())

    # Riceviamo il numero di corsi extra
    corsi = int(client_socket.recv(1024).decode())

    # Variabile per il prezzo base
    totale_base = 0

    # Controlliamo il tipo di abbonamento
    if abbonamento.lower() == "mensile":

        # Prezzo abbonamento mensile
        totale_base = 50

    elif abbonamento.lower() == "annuale":

        # Prezzo abbonamento annuale
        totale_base = 500

    # Ogni corso extra costa 20 euro
    costo_corsi = corsi * 20

    # Calcoliamo il totale iniziale
    totale = totale_base + costo_corsi

    # Se il cliente ha meno di 26 anni
    if eta < 26:

        # Applichiamo sconto del 10%
        totale = totale - (totale * 0.10)

    # Se il cliente ha più di 65 anni
    elif eta > 65:

        # Applichiamo sconto del 15%
        totale = totale - (totale * 0.15)

    # Creiamo il messaggio finale
    messaggio = "Totale finale: " + str(totale) + " euro"

    # Inviamo il messaggio al client
    client_socket.send(messaggio.encode())

    # Chiudiamo la connessione con il client
    client_socket.close()


# Creiamo la socket del server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Assegniamo IP e porta
server.bind(("localhost", 5000))

# Mettiamo il server in ascolto
server.listen()

# Messaggio di avvio server
print("Server avviato...")

# Ciclo infinito
while True:

    # Accettiamo la connessione del client
    client_socket, address = server.accept()

    # Stampiamo il client collegato
    print("Client collegato:", address)

    # Creiamo un thread per il client
    thread = threading.Thread(target=gestisci_client, args=(client_socket,))

    # Avviamo il thread
    thread.start()
