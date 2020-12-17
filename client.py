import socket
import pickle
import grille_auto
from class_multi import Multi

creation = grille_auto.CreationTableauAuto()
tableau_serveur = []
tableau_nom = []


def main():
    port = 5050
    recup_ip = socket.gethostbyname(socket.gethostname())
    adresse = (recup_ip, port)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET = IPV4
    client.connect(adresse)  # connecter le client au serveur
    return client


def gestion_objet(c, compteur):
    if compteur == 0:
        c.send(pickle.dumps(creation.recup_grille()))  # dumps = compression
    elif compteur == 1:
        envoie_nom = input("Quel est ton pseudo ? : ")
        tableau_nom.append(envoie_nom)
        c.send(pickle.dumps(envoie_nom))  # dumps = compression
        compteur += 1
    else:
        other_player = Multi(tableau_serveur[0])
        print("Tableau Adversaire")
        print(other_player.affichage_cache())
        envoie = input("Quel est ton coup " + tableau_nom[0] + ' ?')
        while not other_player.initialisation_jeu(tableau_nom[0], envoie):
            envoie = input("Quel est ton coup " + tableau_nom[0] + ' ?')
        if other_player.winner():
            compteur = 999
            envoie = "Il a gagné !"
            c.send(pickle.dumps(envoie))  # dumps = compression
        else:
            c.send(pickle.dumps(envoie))  # dumps = compression
            print(other_player.affichage_cache())

    donnees = c.recv(2048)
    msg_recu = pickle.loads(donnees)  # déchiffrer les données, décompression des données
    if msg_recu == "Il a gagné !":
        print(tableau_nom[1] + " a gagné !")
    if compteur == 0:
        compteur += 1
        tableau_serveur.append(msg_recu)
    print(msg_recu)
    if compteur != 999:
        gestion_objet(c, compteur)



def start_client():
    creation.creation_grille()
    print("Mon tableau")
    current_player = Multi(creation.recup_grille())
    print(current_player.affichage_bateau())
    c = main()
    compteur = 0
    gestion_objet(c, compteur)
