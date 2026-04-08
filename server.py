import socket
import threading

HOST = '0.0.0.0'
PORT = 5000

clients = []
names = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            if message:
                broadcast(message)
        except:
            index = clients.index(client)
            name = names[index]

            clients.remove(client)
            names.remove(name)

            client.close()

            broadcast(f"{name} salió del chat".encode())
            break

def receive():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print("Servidor activo...")

    while True:
        client, address = server.accept()
        print(f"Conectado con {address}")

        client.send("NOMBRE".encode())
        name = client.recv(1024).decode()

        names.append(name)
        clients.append(client)

        print(f"Usuario: {name}")

        broadcast(f"{name} se unió al chat".encode())

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

receive()   