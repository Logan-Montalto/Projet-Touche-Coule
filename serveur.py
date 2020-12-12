import socket
import pickle
import threading


def main():
    port = 5050
    recup_ip = socket.gethostbyname(socket.gethostname())
    print(f"Le serveur écoute sur {recup_ip}")
    adresse = (recup_ip, port)
    serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET = IPV4
    serveur.bind(adresse) #lier le serveur avec l'adresse
    return serveur


def start_serveur():
    s = main()
    print("Le serveur démarre")
    s.listen()
    while True:
        connexion, adresse_client = s.accept()
        thread_gestion = threading.Thread(target=gestion_client, args=(connexion, adresse_client))
        thread_gestion.start()
        print(f"Connexion active {threading.activeCount()-1}")


def gestion_client(connexion, adresse_client):
    print(f"Adresse du client = {adresse_client}")
    connect = True
    while connect:
        try:
            donnees = connexion.recv(2048)
            reception = pickle.loads(donnees) #déchiffrer les données, décompression des données
            print(reception)
            if not donnees:
                print("Mince, je suis déconnecté")
                connect = False
            envoie = input("Envoie quelque chose que tu veux : ")
            connexion.send(pickle.dumps(envoie)) #dumps = compression
        except:
            print("client déconnecté")
            connect = False
    connexion.close()

if __name__ == '__main__':
    start_serveur()