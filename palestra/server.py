import socket
import threading

def gestisci_client(client_socket):

    abbonamento = client_socket.recv(1024).decode()
    eta = int(client_socket.recv(1024).decode())
    corsi = int(client_socket.recv(1024).decode())

    totale_base = 0

    if abbonamento.lower() == "mensile":
        totale_base = 50

    elif abbonamento.lower() == "annuale":
        totale_base = 500

    costo_corsi = corsi * 20
    totale = totale_base + costo_corsi

    if eta < 26:
        totale = totale - (totale * 0.10)

    elif eta > 65:
        totale = totale - (totale * 0.15)

    messaggio = "Totale finale: " + str(totale) + " euro"
    client_socket.sendall(messaggio.encode())
    client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("127.0.0.1", 5000))
    server.listen(5)
    print("Server avviato sulla porta 5000...")

    while True:
        client_socket, address = server.accept()
        print("Client collegato:", address)

        thread = threading.Thread(
            target=gestisci_client,
            args=(client_socket,)
        )
        thread.start()
        
    server.close()

if __name__ == "__main__":
    start_server()
