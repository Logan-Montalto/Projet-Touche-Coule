import socket
import pickle
import threading
import grille_auto
from class_multi import Multi

creation = grille_auto.CreationTableauAuto()
tableau_client = []
tableau_nom = []


def main():
    """

    :return:
    """
    port = 5050
    recup_ip = socket.gethostbyname(socket.gethostname())
    print(f"Le serveur écoute sur {recup_ip}")
    adresse = (recup_ip, port)
    serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET = IPV4
    serveur.bind(adresse)  # lier le serveur avec l'adresse
    return serveur


def start_serveur():
    """

    :return:
    """
    s = main()
    print("Le serveur démarre")
    creation.creation_grille()
    s.listen()
    while True:
        connexion, adresse_client = s.accept()
        thread_gestion = threading.Thread(target=gestion_client,
                                          args=(connexion, adresse_client, creation.recup_grille()))
        thread_gestion.start()
        print(f"Connexion active {threading.activeCount() - 1}")


def gestion_client(connexion, adresse_client, tableau):
    """

    :param connexion:
    :param adresse_client:
    :param tableau:
    :return:
    """
    print("Mon tableau")
    current_player = Multi(tableau)
    print(current_player.affichage_bateau())
    print(f"Adresse du client = {adresse_client}")
    connect = True
    compteur = 0
    while connect:
        try:
            donnees = connexion.recv(2048)
            reception = pickle.loads(donnees)  # déchiffrer les données, décompression des données
            if reception == "Il a gagné !":
                print(tableau_nom[0] + " a gagné !")
                connect = False
            if compteur == 0:
                tableau_client.append(reception)
            if compteur == 1:
                tableau_nom.append(reception)
            print(reception)
            other_player = Multi(tableau_client[0])
            print(other_player.affichage_cache())
            if not donnees:
                print("Mince, je suis déconnecté")
                connect = False
            if compteur == 0:
                connexion.send(pickle.dumps(tableau))  # dumps = compression
                compteur += 1
            elif compteur == 1:
                envoie_nom = input("Quel est ton pseudo ? : ")
                tableau_nom.append(envoie_nom)
                connexion.send(pickle.dumps(envoie_nom))  # dumps = compression
                compteur += 1
            else:
                envoie = input("Quel est ton coup " + tableau_nom[1] + ' ?')
                while not other_player.initialisation_jeu(tableau_nom[1], envoie):
                    envoie = input("Quel est ton coup " + tableau_nom[1] + ' ?')
                if other_player.winner():
                    envoie = "Il a gagné !"
                    connexion.send(pickle.dumps(envoie))  # dumps = compression
                    connect = False
                else:
                    connexion.send(pickle.dumps(envoie))  # dumps = compression
                    print(other_player.affichage_cache())
        except:
            print("client déconnecté")
            connect = False
    connexion.close()
