import socket
import pickle
import threading
import grille_auto
from class_multi import Multi
import interface

creation = grille_auto.CreationTableauAuto()
tableau_serveur = []
tableau_nom = []


def main():
    """La fonction permet de récupérer l'adresse pour le client (joueur 2)

    :return: Renvoie la connexion avec le client
    """
    port = 5050
    recup_ip = socket.gethostbyname(socket.gethostname())  # récupère l'ip du serveur (même machine)
    adresse = (recup_ip, port)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET = IPV4
    client.connect(adresse)  # connecter le client au serveur
    return client


def gestion_objet(c, compteur, gui):
    """La fonction gère les informations concernant le serveur (données reçues du serveur et données envoyées
    au serveur).


    :param c: Permet la connexion avec le serveur
    :param compteur: Gère la gestion des envoies et des réceptions avec le serveur
    :param gui: Permet de démarrer ou non l'interface graphique via un input en console
    :return: -
    """
    if compteur == 0:
        c.send(pickle.dumps(creation.recup_grille()))  # dumps = compression
    elif compteur == 1:
        envoie_nom = input("Quel est ton pseudo ? : ")
        tableau_nom.append(envoie_nom)
        c.send(pickle.dumps(envoie_nom))  # dumps = compression
        compteur += 1
    else:
        interface.tableau_adversaire = tableau_serveur[0]
        other_player = Multi(tableau_serveur[0])
        print("Tableau Adversaire")
        print(other_player.affichage_cache())
        if gui == "oui":  # utilisation de l'interface
            while True:
                if interface.effectue[-1]:
                    while not other_player.initialisation_jeu(tableau_nom[0], interface.remplissage_tableau[-1]):
                        pass
                    interface.effectue.append(False)
                    break
            if other_player.winner():
                compteur = 999
                envoie = "Il a gagné !"
                c.send(pickle.dumps(envoie))  # dumps = compression
            else:
                c.send(pickle.dumps(interface.remplissage_tableau[-1]))  # dumps = compression
                print(other_player.affichage_cache())
        else:  # utilisation console
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

    donnees = c.recv(2048)  # réception
    msg_recu = pickle.loads(donnees)  # déchiffrer les données, décompression des données
    if msg_recu == "Il a gagné !":
        print(tableau_nom[1] + " a gagné !")
    if compteur == 0:
        compteur += 1
        tableau_serveur.append(msg_recu)
    print(msg_recu)
    if compteur != 999:
        gestion_objet(c, compteur, gui)  # boucle while


def start_client():
    """La fonction démarre le client, son tableau généré aléatoirement, et demande si le joueur veut une interface graphique ou non.
    Si oui, l'interface graphique démarre et la console réagit dynamiquement avec la console.
    Si non, le jeu démarre en console.

    :return: -
    """
    interface.player.append("Client")
    creation.creation_grille()
    print("Mon tableau")
    current_player = Multi(creation.recup_grille())
    print(current_player.affichage_bateau())
    c = main()
    gui = input("Interface graphique ? (oui ou non)")
    if gui == "oui":
        thread_interface = threading.Thread(target=interface.start)
        thread_interface.start()
    compteur = 0
    gestion_objet(c, compteur, gui)
