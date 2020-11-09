from donnees import creation_grille
import time
import keyboard


grille = creation_grille()
touche = 0

def affichage(g):
    print()
    list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    print(g)
    print("   0 1 2 3 4 5 6 7 8 9")
    for y in range(10):
        print(list[y], "|", end='')
        for x in range(10):
            if g[y][x] == 10:
                print('o', end='|')
            elif g[y][x] % 10 == 0 and g[y][x] != 0:
                print('o', end='|')
            elif g[y][x] > 10 and g[y][x] % 10 != 0:
                print('x', end='|')
            else:
                print('.', end='|')
        print()

nom = input("Saisir votre nom : ")
print()
print("Bienvenue", nom + '!')
print("Le but est de couler les 4 bateaux le plus rapidement possible. Bonne Chance !")
print()
print("Tapez la touche 'Ctrl' pour commencer la partie : ")
rk = keyboard.record(until ='Ctrl')
keyboard.play(rk, speed_factor = 1)
t1 = time.time()

while touche != 14:
    affichage(grille)
    print()
    chaine = input("Quel est ton coup " + nom + ' ?')
    while len(chaine) != 2 or chaine[0] < 'A' or 'K' <= chaine[0] < 'a' or 'k' <= chaine[0] or chaine[1] < '0' or chaine[1] > '9':
        print("Veuillez entrer une lettre et un chiffre")
        chaine = input("Quel est ton coup " + nom + ' ?')
    print("Tu as joué", chaine[0].upper() + chaine[1])
    y = ord(chaine[0].upper()) - 65
    x = int(chaine[1])

    if 1 < grille[y][x] < 6:
        print("Touché !")
        touche += 1
    else:
        print("Raté !")
    grille[y][x] += 10
affichage(grille)
print()

def fin_jeu():
    print("Bien joué, tu as coulé tous les bateaux !")
    t2 = time.time()
    t = t2-t1
    z = round(t,2)
    print("Tu as mis " + str(z) + " secondes.")
fin_jeu()