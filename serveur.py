import socket
import pickle
import threading
import grille_auto
from class_multi import Multi
import interface

creation = grille_auto.CreationTableauAuto()
tableau_client = []
tableau_nom = []


def main():
    """La fonction permet de récupérer l'adresse pour le serveur (joueur 1)

    :return: Renvoie la connexion avec le serveur
    """
    port = 5050
    recup_ip = socket.gethostbyname(socket.gethostname())
    print(f"Le serveur écoute sur {recup_ip}")
    adresse = (recup_ip, port)
    serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET = IPV4
    serveur.bind(adresse)  # lier le serveur avec l'adresse
    return serveur


def start_serveur():
    """La fonction démarre le serveur et demande si le joueur veut une interface graphique ou non.
    Si oui, l'interface graphique démarre et la console réagit dynamiquement avec la console.
    Si non, le jeu démarre en console.

    :return: -
    """
    interface.player.append("Serveur")
    s = main()
    gui = input("Voulez-vous une interface ou non ? (oui ou non)")
    if gui == "oui":
        thread_interface = threading.Thread(target=interface.start)
        thread_interface.start()

    print("Le serveur démarre")
    creation.creation_grille()
    s.listen()
    while True:
        connexion, adresse_client = s.accept()
        thread_gestion = threading.Thread(target=gestion_client,
                                          args=(connexion, adresse_client, creation.recup_grille(), gui))
        thread_gestion.start()
        print(f"Connexion active {threading.activeCount() - 1}")


def gestion_client(connexion, adresse_client, tableau, gui):
    """La fonction gère les informations concernant le client (données reçues du client et données envoyées au client).
    Un compteur détermine quelle partie du processus se met en marche pour l'envoie et la réception des données.
    La fonction gère aussi la partie interface et console en fonction de la réponse de l'input de la variable gui.

    :param connexion: Permet la connexion avec le client
    :param adresse_client: Affiche l'adresse du client
    :param tableau: Affiche le tableau généré aléatoirement pour le serveur (joueur 1)
    :param gui: Permet de démarrer ou non l'interface graphique via un input en console
    :return: -
    """
    print("Mon tableau")
    current_player = Multi(tableau)
    print(current_player.affichage_bateau())
    print(f"Adresse du client = {adresse_client}")
    connect = True
    compteur = 0
    while connect:
        try:
            donnees = connexion.recv(2048)  # réception
            reception = pickle.loads(donnees)  # déchiffrer les données, décompression des données
            if reception == "Il a gagné !":
                print(tableau_nom[0] + " a gagné !")
                connect = False
            if compteur == 0:
                interface.tableau_adversaire = reception
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
                if gui == "oui":  # Utilisation interface
                    while True:
                        if interface.effectue[-1]:
                            while not other_player.initialisation_jeu(tableau_nom[1],
                                                                      interface.remplissage_tableau[-1]):
                                pass
                            interface.effectue.append(False)
                            break
                    if other_player.winner():
                        envoie = "Il a gagné !"
                        connexion.send(pickle.dumps(envoie))  # dumps = compression
                        connect = False  # Erreur
                    else:
                        connexion.send(pickle.dumps(interface.remplissage_tableau[-1]))  # dumps = compression
                        print(other_player.affichage_cache())
                else:  # utilisation console
                    envoie = input("Quel est ton coup " + tableau_nom[1] + ' ?')
                    while not other_player.initialisation_jeu(tableau_nom[0], envoie):
                        envoie = input("Quel est ton coup " + tableau_nom[0] + ' ?')
                    if other_player.winner():
                        envoie = "Il a gagné !"
                        connexion.send(pickle.dumps(envoie))  # dumps = compression
                        connect = False  # Erreur
                    else:
                        connexion.send(pickle.dumps(envoie))  # dumps = compression
                        print(other_player.affichage_cache())
        except:
            print("client déconnecté")
            connect = False
    connexion.close()
