import socket
import pickle
import grille_auto


creation = grille_auto.CreationTableauAuto()
tableau_serveur = []


def main():
    port = 5050
    recup_ip = socket.gethostbyname(socket.gethostname())
    adresse = (recup_ip, port)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET = IPV4
    client.connect(adresse) #connecter le client au serveur
    return client


def gestion_objet(c, compteur):
    if compteur == 0:
        c.send(pickle.dumps(creation.recup_grille()))  # dumps = compression
        compteur += 1
    elif compteur == 1:
        envoie_nom = input("Quel est ton pseudo ? : ")
        c.send(pickle.dumps(envoie_nom))  # dumps = compression
        compteur += 1
    else:
        envoie = input("Envoie quelque chose que tu veux : ")
        c.send(pickle.dumps(envoie))  # dumps = compression
    donnees = c.recv(2048)
    msg_recu = pickle.loads(donnees)  # déchiffrer les données, décompression des données
    if compteur == 1:
        tableau_serveur.append(msg_recu)
    print(affichage(msg_recu))
    print(affichage(tableau_serveur[0]))
    gestion_objet(c, compteur)


def start_client():
    creation.creation_grille()
    print("Mon tableau")
    print(affichage(creation.recup_grille()))
    c = main()
    compteur = 0
    gestion_objet(c, compteur)


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