import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(5)

host = input("Hostname: ")
port = int(input("Port: "))

def portScanner(port):
    if client.connect_ex((host,port)):
        print("The port is closed")
    else:
        print("The port is open")
        
portScanner(port)
