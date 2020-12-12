import socket
import pickle
import threading


def main():
    port = 5050
    recup_ip = socket.gethostbyname(socket.gethostname())
    print(f"Le serveur écoute sur {recup_ip}")
    adresse = (recup_ip, port)
    serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #IPV4
    serveur.bind(adresse) #lier le serveur avec l'adresse
    return serveur


def start_serveur():
    s = main()
    print("Le serveur démarre")
    s.listen()
    while True:
        conn, adresse_client = s.accept()
        thread_gestion = threading.Thread(target=gestion_client, args=(conn, adresse_client))
        thread_gestion.start()
        print(f"Connexion active {threading.activeCount()-1}")