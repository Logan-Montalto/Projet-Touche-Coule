import socket
import pickle
import threading
import grille_auto


creation = grille_auto.CreationTableauAuto()
tableau_client = []


def main():
    port = 5050
    recup_ip = socket.gethostbyname(socket.gethostname())
    print(f"Le serveur écoute sur {recup_ip}")
    adresse = (recup_ip, port)
    serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET = IPV4
    serveur.bind(adresse) #lier le serveur avec l'adresse
    return serveur


def start_serveur():
    creation.creation_grille()
    s = main()
    print("Le serveur démarre")
    s.listen()
    while True:
        connexion, adresse_client = s.accept()
        thread_gestion = threading.Thread(target=gestion_client, args=(connexion, adresse_client, creation.recup_grille()))
        thread_gestion.start()
        print(f"Connexion active {threading.activeCount()-1}")


def gestion_client(connexion, adresse_client, tableau):
    print("Mon tableau")
    print(affichage(tableau))
    print(f"Adresse du client = {adresse_client}")
    connect = True
    compteur = 0
    while connect:
        try:
            donnees = connexion.recv(2048)
            reception = pickle.loads(donnees) #déchiffrer les données, décompression des données
            if compteur == 0:
                tableau_client.append(reception)
            print(reception)
            print(affichage(tableau_client[0]))
            if not donnees:
                print("Mince, je suis déconnecté")
                connect = False
            if compteur == 0:
                connexion.send(pickle.dumps(tableau)) #dumps = compression
                compteur += 1
            elif compteur == 1:
                envoie_nom = input("Quel est ton pseudo ? : ")
                connexion.send(pickle.dumps(envoie_nom))  # dumps = compression
                compteur += 1
            else:
                envoie = input("Envoie quelque chose que tu veux : ")
                connexion.send(pickle.dumps(envoie))  # dumps = compression
        except:
            print("client déconnecté")
            connect = False
    connexion.close()

def affichage(tableau):
    print()
    list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    print("   0 1 2 3 4 5 6 7 8 9")
    for y in range(10):
        print(list[y], "|", end='')
        for x in range(10):
            if tableau[y][x] == 10:
                print('o', end='|')
            elif tableau[y][x] % 10 == 0 and tableau[y][x] != 0:
                print('o', end='|')
            elif tableau[y][x] > 10 and tableau[y][x] % 10 != 0:
                print('x', end='|')
            else:
                print(str(tableau[y][x]), end='|')
        print()