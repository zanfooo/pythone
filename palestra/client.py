import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 5000))

abbonamento = input("Inserisci abbonamento (mensile/annuale): ")
eta = input("Inserisci età: ")
corsi = input("Inserisci numero corsi extra: ")

client.send(abbonamento.encode())
client.send(eta.encode())
client.send(corsi.encode())

risposta = client.recv(1024).decode()
print(risposta)

client.close()
