import socket
import pickle
import threading


def main():
    port = 5050
    recup_ip = socket.gethostbyname(socket.gethostname())
    adresse = (recup_ip, port)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET = IPV4
    client.connect(adresse) #connecter le client au serveur
    return client


def gestion_objet(c):
    envoie = input("Envoie quelque chose que tu veux : ")
    c.send(pickle.dumps(envoie))  # dumps = compression
    donnees = c.recv(2048)
    msg_recu = pickle.loads(donnees)  # déchiffrer les données, décompression des données
    print(msg_recu)
    gestion_objet(c)

if __name__ == '__main__':
    c = main()
    gestion_objet(c)