from grille_humaine import CreationGrillehuman
import serveur
import client

def start_multi():
    jeu_human = CreationGrillehuman()
    taille = 2
    jeu_human.affichage()
    liste = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
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
    s = input("Quel connexion ? (serveur ou client) : ")
    if s == "serveur":
        serveur.start_serveur()
    else:
        client.start_client()



if __name__ == '__main__':
    choix_mode()