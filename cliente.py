import socket
import threading

HOST = '127.0.0.1'
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

name = input("Tu nombre: ")

def receive():
    while True:
        try:
            message = client.recv(1024).decode()
            if message == "NOMBRE":
                client.send(name.encode())
            else:
                print(message)
        except:
            print("Error")
            client.close()
            break

def write():
    while True:
        message = f"{name}: {input('')}"
        client.send(message.encode())

threading.Thread(target=receive).start()
threading.Thread(target=write).start()