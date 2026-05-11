# Importiamo la libreria socket
import socket

# Creiamo la socket del client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Ci colleghiamo al server
client.connect(("localhost", 5000))

# Chiediamo il tipo di abbonamento
abbonamento = input("Inserisci abbonamento (mensile/annuale): ")

# Chiediamo l'età
eta = input("Inserisci età: ")

# Chiediamo il numero di corsi extra
corsi = input("Inserisci numero corsi extra: ")

# Inviamo il tipo di abbonamento
client.send(abbonamento.encode())

# Inviamo l'età
client.send(eta.encode())

# Inviamo il numero di corsi
client.send(corsi.encode())

# Riceviamo il messaggio finale dal server
risposta = client.recv(1024).decode()

# Stampiamo il risultato
print(risposta)

# Chiudiamo la connessione
client.close()
