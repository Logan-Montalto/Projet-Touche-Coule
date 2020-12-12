import socket
import pickle

def main():
    port = 5050
    recup_ip = socket.gethostbyname(socket.gethostname())
    print(f"Le serveur écoute sur {recup_ip}")
    