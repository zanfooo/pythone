import socket
# Importa la libreria socket per la comunicazione client-server

import threading
# Importa threading per gestire più client contemporaneamente


def gestisci_client(client_socket):
    # Funzione che gestisce il singolo client collegato

    abbonamento = client_socket.recv(1024).decode()
    # Riceve il tipo di abbonamento dal client
    # recv(1024) riceve massimo 1024 byte
    # decode() trasforma i byte in stringa

    eta = int(client_socket.recv(1024).decode())
    # Riceve l'età dal client
    # int() converte la stringa in numero intero

    corsi = int(client_socket.recv(1024).decode())
    # Riceve il numero di corsi extra

    totale_base = 0
    # Variabile che conterrà il costo base dell'abbonamento

    if abbonamento.lower() == "mensile":
        # lower() trasforma il testo in minuscolo
        # così "Mensile" e "mensile" vengono letti uguali

        totale_base = 50
        # Prezzo abbonamento mensile

    elif abbonamento.lower() == "annuale":
        # Controlla se l'abbonamento è annuale

        totale_base = 500
        # Prezzo abbonamento annuale

    costo_corsi = corsi * 20
    # Ogni corso extra costa 20 euro

    totale = totale_base + costo_corsi
    # Calcola il totale iniziale

    if eta < 26:
        # Se il cliente ha meno di 26 anni

        totale = totale - (totale * 0.10)
        # Applica sconto del 10%

    elif eta > 65:
        # Se il cliente ha più di 65 anni

        totale = totale - (totale * 0.15)
        # Applica sconto del 15%

    messaggio = "Totale finale: " + str(totale) + " euro"
    # Crea il messaggio finale da inviare al client
    # str() converte il numero in stringa

    client_socket.sendall(messaggio.encode())
    # Invia il messaggio al client
    # encode() converte la stringa in byte

    client_socket.close()
    # Chiude la connessione con il client


def start_server():
    # Funzione principale del server

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Crea il socket del server
    # AF_INET = IPv4
    # SOCK_STREAM = protocollo TCP

    server.bind(("127.0.0.1", 5000))
    # Collega il server all'indirizzo IP e alla porta 5000

    server.listen(5)
    # Mette il server in ascolto
    # 5 indica il numero massimo di connessioni in attesa

    print("Server avviato sulla porta 5000...")
    # Messaggio di avvio server

    while True:
        # Ciclo infinito per accettare sempre nuovi client

        client_socket, address = server.accept()
        # Accetta la connessione del client
        # client_socket = socket dedicato al client
        # address = indirizzo del client

        print("Client collegato:", address)
        # Stampa l'indirizzo del client collegato

        thread = threading.Thread(
            target=gestisci_client,
            args=(client_socket,)
        )
        # Crea un thread
        # target = funzione da eseguire
        # args = parametri della funzione

        thread.start()
        # Avvia il thread
        # Ogni client viene gestito separatamente

    server.close()
    # Chiude il server
    # In realtà qui non verrà mai eseguito
    # perché il while True è infinito


if __name__ == "__main__":
    # Controlla se il file è eseguito direttamente

    start_server()
    # Avvia il server
