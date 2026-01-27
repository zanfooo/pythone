import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    print("Connesso alla centrale taxi 🚖")

    try:
        while True:
            partenza = input("Città di partenza (exit per uscire): ")
            if partenza.lower() == "exit":
                break

            arrivo = input("Città di arrivo: ")

            richiesta = f"{partenza},{arrivo}"
            client_socket.sendall(richiesta.encode())

            risposta = client_socket.recv(1024).decode()
            print("\nRisposta server:")
            print(risposta)
            print("-" * 30)

    except Exception as e:
        print("Errore:", e)

    client_socket.close()

if __name__ == "__main__":
    start_client()
