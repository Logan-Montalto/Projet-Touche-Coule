from grille_humaine import CreationGrillehuman
import serveur
import client


def start_multi():
    """La fonction permet de placer 4 bateaux de tailles différentes sur une grille vierge

    :return: -
    """
    jeu_human = CreationGrillehuman()
    taille = 2
    jeu_human.affichage()
    while True:
        print(f"la taille du bateau est de {taille}")

        a = input("debut Y : ")
        b = int(input("debut X : "))
        c = input("fin Y : ")
        d = int(input("fin X : "))
        if jeu_human.placement([a, b], [c, d], taille):
            taille += 1
        if taille == 6:
            break


def choix_mode():
    """La fonction permet de démarrer la connexion serveur ou la connexion client

    :return: -
    """
    s = input("Quel connexion ? (serveur ou client) : ")
    if s == "serveur":
        serveur.start_serveur()
    else:
        client.start_client()