import socket
import pickle

def main():
    port = 5050
    recup_ip = socket.gethostbyname(socket.gethostname())
    print(f"Le serveur écoute sur {recup_ip}")
    addresse = (recup_ip, port)
    serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #IPV4
    serveur.bind(addresse) #lier le serveur avec l'adresse
    return serveur

def start_serveur():
    s = main()