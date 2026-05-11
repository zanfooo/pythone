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

    client_socket.send(messaggio.encode())
    client_socket.close()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("localhost", 5000))

server.listen()

print("Server avviato...")


while True:

    client_socket, address = server.accept()

    print("Client collegato:", address)

    thread = threading.Thread(target=gestisci_client, args=(client_socket,))
    thread.start()
