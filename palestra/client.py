import socket

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 5000))

    abbonamento = input("Inserisci abbonamento (mensile/annuale): ")
    eta = input("Inserisci età: ")
    corsi = input("Inserisci numero corsi extra: ")

    client.sendall(abbonamento.encode())
    client.sendall(eta.encode())
    client.sendall(corsi.encode())

    risposta = client.recv(1024).decode()
    print("Risposta dal server:", risposta)
    client.close()

if __name__ == "__main__":
    start_client()
