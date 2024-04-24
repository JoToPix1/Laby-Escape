# -Librairies
import random
from colorama import init, Fore, Style
import numpy as np
import mysql.connector
import json
import time

mydb = mysql.connector.connect(
    host="localhost", user="root", password="", port="3306", database="labyrinthe"
)


# definition des couleurs
def blanc(text):
    newtext = Fore.LIGHTWHITE_EX + text
    return newtext + Style.RESET_ALL


def blue(text):
    newtext = Fore.LIGHTBLUE_EX + text
    return newtext + Style.RESET_ALL


def red(text):
    newtext = Fore.LIGHTRED_EX + text
    return newtext + Style.RESET_ALL


def yellow(text):
    newtext = Fore.LIGHTYELLOW_EX + text
    return newtext + Style.RESET_ALL


def green(text):
    newtext = Fore.LIGHTGREEN_EX + text
    return newtext + Style.RESET_ALL


def magenta(text):
    newtext = Fore.LIGHTMAGENTA_EX + text
    return newtext + Style.RESET_ALL


# enregistrer les scores
def sauvegarder_score(score, pseudo, difficulty):
    mycursor = mydb.cursor()
    sql = "INSERT INTO scores (score, pseudo, difficulty) VALUES (%s, %s, %s)"
    val = (score, pseudo, difficulty)
    mycursor.execute(sql, val)
    mydb.commit()


# afficher les meilleurs scores
def afficher_top_scores_easy():
    mycursor = mydb.cursor()
    sql = "SELECT score, pseudo, difficulty FROM scores WHERE difficulty='FACILE' ORDER BY score DESC LIMIT 5"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
        print("Pseudo:", x[1], "- Score:", x[0], "- Difficulté:", x[2])


def afficher_top_scores_normal():
    mycursor = mydb.cursor()
    sql = "SELECT score, pseudo, difficulty FROM scores WHERE difficulty='NORMALE' ORDER BY score DESC LIMIT 5"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
        print("Pseudo:", x[1], "- Score:", x[0], "- Difficulté:", x[2])


def afficher_top_scores_hard():
    mycursor = mydb.cursor()
    sql = "SELECT score, pseudo, difficulty FROM scores WHERE difficulty='DIFFICILE' ORDER BY score DESC LIMIT 5"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
        print("Pseudo:", x[1], "- Score:", x[0], "- Difficulté:", x[2])


# afficher les dernières sauvegarde
def afficher_sauvegarde():
    mycursor = mydb.cursor()
    sql = "SELECT score, pseudo, difficulty, id FROM sauvegarde ORDER BY id ASC LIMIT 5"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
        print("Pseudo:", x[1], "- Score:", x[0])


# sauegarder une partie
def sauvegarder_partie(
    joueur,
    score,
    difficulty,
    etat_matrice,
    entree_y,
    entree_x,
    monstre_x,
    monstre_y,
    tp_x,
    tp_y,
    tp2_x,
    tp2_y,
    tp3_x,
    tp3_y,
    tp4_x,
    tp4_y,
    tp5_x,
    tp5_y,
    tp6_x,
    tp6_y,
    sortie_x,
    sortie_y,
    hauteur,
    largeur,
    thesee_x,
    thesee_y,
):
    mycursor = mydb.cursor()
    sql = "INSERT INTO sauvegarde (pseudo, score, difficulty, etat_matrice, entree_y, entree_x, monstre_x, monstre_y, tp_x, tp_y, tp2_x, tp2_y, tp3_x, tp3_y, tp4_x, tp4_y, tp5_x, tp5_y, tp6_x, tp6_y, sortie_x, sortie_y, hauteur, largeur, thesee_x, thesee_y) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (
        joueur,
        score,
        difficulty,
        etat_matrice,
        entree_y,
        entree_x,
        monstre_x,
        monstre_y,
        tp_x,
        tp_y,
        tp2_x,
        tp2_y,
        tp3_x,
        tp3_y,
        tp4_x,
        tp4_y,
        tp5_x,
        tp5_y,
        tp6_x,
        tp6_y,
        sortie_x,
        sortie_y,
        hauteur,
        largeur,
        thesee_x,
        thesee_y,
    )
    mycursor.execute(sql, val)
    mydb.commit()


# charger une partie (non fonctionnel actuellement)
def restaurer_partie(pseudo, score):
    mycursor = mydb.cursor()
    sql = "SELECT etat_matrice, entree_y, entree_x, monstre_x, monstre_y, tp_x, tp_y, tp2_x, tp2_y, tp3_x, tp3_y, tp4_x, tp4_y, tp5_x, tp5_y, tp6_x, tp6_y, sortie_x, sortie_y, difficulty, hauteur, largeur, thesee_x, thesee_y, score FROM sauvegarde WHERE pseudo = %s AND score = %s"
    val = (pseudo, score)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchone()
    if myresult:
        etat_matrice_str = myresult[0]
        labyrinthe = json.loads(etat_matrice_str)
        entree_y = myresult[1]
        entree_x = myresult[2]
        monstre_x = myresult[3]
        monstre_y = myresult[4]
        tp_x = myresult[5]
        tp_y = myresult[6]
        tp2_x = myresult[7]
        tp2_y = myresult[8]
        tp3_x = myresult[9]
        tp3_y = myresult[10]
        tp4_x = myresult[11]
        tp4_y = myresult[12]
        tp5_x = myresult[13]
        tp5_y = myresult[14]
        tp6_x = myresult[15]
        tp6_y = myresult[16]
        sortie_x = myresult[17]
        sortie_y = myresult[18]
        difficulty = myresult[19]
        hauteur = myresult[20]
        largeur = myresult[21]
        thesee_x = myresult[22]
        thesee_y = myresult[23]
        score = myresult[24]
        return (
            labyrinthe,
            entree_y,
            entree_x,
            monstre_x,
            monstre_y,
            tp_x,
            tp_y,
            tp2_x,
            tp2_y,
            tp3_x,
            tp3_y,
            tp4_x,
            tp4_y,
            tp5_x,
            tp5_y,
            tp6_x,
            tp6_y,
            sortie_x,
            sortie_y,
            difficulty,
            hauteur,
            largeur,
            thesee_x,
            thesee_y,
            score,
        )
    else:
        return None


# verifier si deux points sont accessible entre eux
def is_accessible(labyrinthe, y1, x1, y2, x2):
    verif = {(y1, x1)}
    verif2 = {(y1, x1)}

    while verif:
        a, b = verif.pop()

        for da, db in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            na, nb = a + da, b + db
            if na == y2 and nb == x2:
                return True
            if na >= 0 and na < len(labyrinthe) and nb >= 0 and nb < len(labyrinthe[0]):
                cell = labyrinthe[na][nb]
                if cell in (f"\x1b[8m█\x1b[0m", "O", "o") and (na, nb) not in verif2:
                    verif.add((na, nb))
                    verif2.add((na, nb))
    return False


# vérifier que c'est le labyrinthe est finissable
def is_finishable(
    labyrinthe, entree_y, entree_x, sortie_y, sortie_x, monstre_y, monstre_x
):
    verif = {(entree_y, entree_x)}
    verif2 = {(0, 0)}
    trouve_monstre = False
    trouve_sortie = False

    while verif and not (trouve_monstre and trouve_sortie):
        a, b = verif.pop()
        for da, db in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            na, nb = a + da, b + db
            if na >= 0 and na < len(labyrinthe) and nb >= 0 and nb < len(labyrinthe[0]):
                cell = labyrinthe[na][nb]
                if cell in (f"\x1b[8m█\x1b[0m", "O", "o") and (na, nb) not in verif2:
                    verif.add((na, nb))
                    verif2.add((na, nb))
                elif cell == labyrinthe[monstre_y][monstre_x]:
                    trouve_monstre = True
                elif cell == labyrinthe[sortie_y][sortie_x]:
                    trouve_sortie = True
        if not verif:
            return False

    if is_accessible(
        labyrinthe, sortie_y, sortie_x, monstre_y, monstre_x
    ) and is_accessible(labyrinthe, entree_y, entree_x, sortie_y, sortie_x):
        return True
    else:
        return False


print(yellow("dernières sauvegarde:"))
afficher_sauvegarde()
restaure = input("souhaiter vous charger une partie? (O/N)")

if restaure.upper() == "N":
    # -Nom joueur
    joueur = "defaulname1"
    while not (len(joueur) < 10 and len(joueur) > 0):
        joueur = input(blue("Entrez le nom du joueur : ")).capitalize()
        if len(joueur) >= 10:
            print(red("Le nom ne doit pas comporter plus de 9 lettres"))
        if len(joueur) <= 0:
            print(red("Le nom doit au minimum contenir 1 lettre"))

    print(
        yellow("Entrée la difficulté:"),
        green("FACILE"),
        yellow("NORMALE"),
        red("DIFFICILE"),
    )
    difficulty = input("").upper()
    if (
        difficulty.upper() == "FACILE"
        or difficulty.upper() == "NORMALE"
        or difficulty.upper() == "DIFFICILE"
    ):
        pass
    else:
        print(yellow("Ce n'est pas un niveau de difficulté."))
        print(
            yellow("Entrée la difficulté:"),
            green("FACILE"),
            yellow("NORMALE"),
            red("DIFFICILE"),
        )
        difficulty = input("").upper()

    print("")
    print("")
    print("")

    # -Histoire du jeu

    print(green("Bienvenue sur le LABY-ESCAPE"))

    print("")

    print
    (
        yellow(
            "Pour poursuivre sa quete, Thésée doit franchir le labyrinthe en terrasant le minautore afin de trouver la sortie "
        )
    )

    print("")

    print(blue("□"), yellow("= Mur magique incassable par le minautore"))
    print(blanc("#"), yellow("= Mur du labyrinthe cassable par le minautore"))
    print(magenta("M"), yellow("= Minautore"))
    print(blue("O - o"), yellow(" = Portails de teleportations"))
    print(green("T"), yellow("= Thésée"))
    print(yellow("S"), yellow("= Sortie"))
    print(yellow("E"), yellow("= Entrée"))

    print("")

    print(
        yellow(
            "l'emplacement des murs interieurs, minautore, portails de téléportations, sortie et Thésée change a chaque partie"
        )
    )
    print("")

# Initialise la bibliothèque colorama
init()

# boucle permettant de relancer une partie
quitte = False
while True:
    # -Dimensions du labyrinthe
    hauteur = 16
    largeur = 22

    # variable utilisé plus tard:
    dead_m = False  # verifier mort du minotaure
    non_relance = True  # variable servant à redémarrer

    if restaure.upper() == "N":
        # -Créer une matrice de cases
        labyrinthe = [
            [f"\x1b[8m{chr(9608)}\x1b[0m" for x in range(largeur)]
            for y in range(hauteur)
        ]

        #  -Ajouter des murs autour du labyrinthe
        for x in range(largeur):
            labyrinthe[0][x] = blue("□")
            labyrinthe[hauteur - 1][x] = blue("□")
        for y in range(hauteur):
            labyrinthe[y][0] = blue("□")
            labyrinthe[y][largeur - 1] = blue("□")

        # -Position monstre aléatoire
        rng = np.random.default_rng()
        monstre_x, monstre_y = random.choice(
            [(rng.integers(1, y + 1), y) for y in range(1, hauteur - 2)]
            + [(largeur - 2, y) for y in range(1, hauteur - 2)]
            + [(x, rng.integers(1, x + 1)) for x in range(1, largeur - 2)]
            + [(x, hauteur - 2) for x in range(1, largeur - 2)]
        )
        while not (
            ((monstre_y) >= 1)
            and ((monstre_y) <= (hauteur - 1))
            and ((monstre_x) >= 1)
            and ((monstre_x) <= (largeur - 1))
        ):
            monstre_x, monstre_y = random.choice(
                [(rng.integers(1, y + 1), y) for y in range(1, hauteur - 2)]
                + [(largeur - 2, y) for y in range(1, hauteur - 2)]
                + [(x, rng.integers(1, x + 1)) for x in range(1, largeur - 2)]
                + [(x, hauteur - 2) for x in range(1, largeur - 2)]
            )

        labyrinthe[monstre_y][monstre_x] = magenta("M")

        # -TP aléatoire, à faire par couple entrée/sortie
        rng = np.random.default_rng()
        tp_x, tp_y = random.choice(
            [(rng.integers(1, y + 1), y) for y in range(1, hauteur - 2)]
            + [(largeur - 2, y) for y in range(1, hauteur - 2)]
            + [(x, rng.integers(1, x + 1)) for x in range(1, largeur - 2)]
            + [(x, hauteur - 2) for x in range(1, largeur - 2)]
        )
        while not (
            ((tp_y) >= 1)
            and ((tp_y) <= (hauteur - 1))
            and ((tp_x) >= 1)
            and ((tp_x) <= (largeur - 1))
        ):
            tp_x, tp_y = random.choice(
                [(rng.integers(1, y + 1), y) for y in range(1, hauteur - 2)]
                + [(largeur - 2, y) for y in range(1, hauteur - 2)]
                + [(x, rng.integers(1, x + 1)) for x in range(1, largeur - 2)]
                + [(x, hauteur - 2) for x in range(1, largeur - 2)]
            )
        labyrinthe[tp_y][tp_x] = blue("O")

        tp2_x, tp2_y = random.choice(
            [(rng.integers(1, y + 1), y) for y in range(1, hauteur - 2)]
            + [(largeur - 2, y) for y in range(1, hauteur - 2)]
            + [(x, rng.integers(1, x + 1)) for x in range(1, largeur - 2)]
            + [(x, hauteur - 2) for x in range(1, largeur - 2)]
        )
        while not (
            ((tp2_y) >= 1)
            and ((tp2_y) <= (hauteur - 1))
            and ((tp2_x) >= 1)
            and ((tp2_x) <= (largeur - 1))
        ):
            tp2_x, tp2_y = random.choice(
                [(rng.integers(1, y + 1), y) for y in range(1, hauteur - 2)]
                + [(largeur - 2, y) for y in range(1, hauteur - 2)]
                + [(x, rng.integers(1, x + 1)) for x in range(1, largeur - 2)]
                + [(x, hauteur - 2) for x in range(1, largeur - 2)]
            )
        labyrinthe[tp2_y][tp2_x] = blue("O")

        tp3_x, tp3_y = random.choice(
            [(rng.integers(1, y + 1), y) for y in range(1, hauteur - 2)]
            + [(largeur - 2, y) for y in range(1, hauteur - 2)]
            + [(x, rng.integers(1, x + 1)) for x in range(1, largeur - 2)]
            + [(x, hauteur - 2) for x in range(1, largeur - 2)]
        )
        while not (
            ((tp3_y) >= 1)
            and ((tp3_y) <= (hauteur - 1))
            and ((tp3_x) >= 1)
            and ((tp3_x) <= (largeur - 1))
        ):
            tp3_x, tp3_y = random.choice(
                [(rng.integers(1, y + 1), y) for y in range(1, hauteur - 2)]
                + [(largeur - 2, y) for y in range(1, hauteur - 2)]
                + [(x, rng.integers(1, x + 1)) for x in range(1, largeur - 2)]
                + [(x, hauteur - 2) for x in range(1, largeur - 2)]
            )

        tp4_x, tp4_y = random.choice(
            [(rng.integers(1, y + 1), y) for y in range(1, hauteur - 2)]
            + [(largeur - 2, y) for y in range(1, hauteur - 2)]
            + [(x, rng.integers(1, x + 1)) for x in range(1, largeur - 2)]
            + [(x, hauteur - 2) for x in range(1, largeur - 2)]
        )
        while not (
            ((tp4_y) >= 1)
            and ((tp4_y) <= (hauteur - 1))
            and ((tp4_x) >= 1)
            and ((tp4_x) <= (largeur - 1))
        ):
            tp4_x, tp4_y = random.choice(
                [(rng.integers(1, y + 1), y) for y in range(1, hauteur - 2)]
                + [(largeur - 2, y) for y in range(1, hauteur - 2)]
                + [(x, rng.integers(1, x + 1)) for x in range(1, largeur - 2)]
                + [(x, hauteur - 2) for x in range(1, largeur - 2)]
            )

        tp5_x, tp5_y = random.choice(
            [(rng.integers(1, y + 1), y) for y in range(1, hauteur - 2)]
            + [(largeur - 2, y) for y in range(1, hauteur - 2)]
            + [(x, rng.integers(1, x + 1)) for x in range(1, largeur - 2)]
            + [(x, hauteur - 2) for x in range(1, largeur - 2)]
        )
        while not (
            ((tp5_y) >= 1)
            and ((tp5_y) <= (hauteur - 1))
            and ((tp5_x) >= 1)
            and ((tp5_x) <= (largeur - 1))
        ):
            tp5_x, tp5_y = random.choice(
                [(rng.integers(1, y + 1), y) for y in range(1, hauteur - 2)]
                + [(largeur - 2, y) for y in range(1, hauteur - 2)]
                + [(x, rng.integers(1, x + 1)) for x in range(1, largeur - 2)]
                + [(x, hauteur - 2) for x in range(1, largeur - 2)]
            )

        tp6_x, tp6_y = random.choice(
            [(rng.integers(1, y + 1), y) for y in range(1, hauteur - 2)]
            + [(largeur - 2, y) for y in range(1, hauteur - 2)]
            + [(x, rng.integers(1, x + 1)) for x in range(1, largeur - 2)]
            + [(x, hauteur - 2) for x in range(1, largeur - 2)]
        )
        while not (
            ((tp6_y) >= 1)
            and ((tp6_y) <= (hauteur - 1))
            and ((tp6_x) >= 1)
            and ((tp6_x) <= (largeur - 1))
        ):
            tp6_x, tp6_y = random.choice(
                [(rng.integers(1, y + 1), y) for y in range(1, hauteur - 2)]
                + [(largeur - 2, y) for y in range(1, hauteur - 2)]
                + [(x, rng.integers(1, x + 1)) for x in range(1, largeur - 2)]
                + [(x, hauteur - 2) for x in range(1, largeur - 2)]
            )
        if difficulty.upper() == "FACILE":
            labyrinthe[tp3_y][tp3_x] = blue("o")
            labyrinthe[tp4_y][tp4_x] = blue("o")
            labyrinthe[tp5_y][tp5_x] = blue("o")
            labyrinthe[tp6_y][tp6_x] = blue("o")
        elif difficulty.upper() == "NORMALE":
            labyrinthe[tp3_y][tp3_x] = blue("o")
            labyrinthe[tp4_y][tp4_x] = blue("o")
        else:
            pass

        # -Sortie aléatoire
        sortie_x, sortie_y = random.choice(
            [(0, y) for y in range(1, hauteur - 1)]
            + [(largeur - 1, y) for y in range(1, hauteur - 1)]
            + [(x, 0) for x in range(1, largeur - 1)]
            + [(x, hauteur - 1) for x in range(1, largeur - 1)]
        )
        labyrinthe[sortie_y][sortie_x] = yellow("S")

        # -Thésee entrée
        entree_x, entree_y = random.choice(
            [(0, y) for y in range(1, hauteur - 1)]
            + [(largeur - 1, y) for y in range(1, hauteur - 1)]
            + [(x, 0) for x in range(1, largeur - 1)]
            + [(x, hauteur - 1) for x in range(1, largeur - 1)]
        )
        labyrinthe[entree_y][entree_x] = yellow("E")

        # -Position de Thésée
        thesee_x, thesee_y = entree_x, entree_y

        # afficher les murs / Ajouter des "#" supplémentaires
        if difficulty.upper() == "FACILE":
            nb_murs = 71
        elif difficulty.upper() == "NORMALE":
            nb_murs = 83
        elif difficulty.upper() == "DIFFICILE":
            nb_murs = 99

        for i in range(nb_murs):
            while True:
                x, y = random.randint(1, largeur - 2), random.randint(1, hauteur - 2)
                if labyrinthe[y][x] == f"\x1b[8m{chr(9608)}\x1b[0m":
                    if (x, y) in [
                        (entree_x + dx, entree_y + dy)
                        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]
                    ] or (x, y) in [
                        (sortie_x + dx, sortie_y + dy)
                        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]
                    ]:
                        continue
                    labyrinthe[y][x] = blanc("#")
                    break

        # -Compteur de score de la partie
        score = (
            ((((hauteur * largeur) - (2 * largeur)) - (2 * hauteur)) + 4)
            - nb_murs
            - 111
        )

        # usage fonction is_finishable pour le savoir et potentiellement redémarrer
        is_finishable(
            labyrinthe, entree_y, entree_x, sortie_y, sortie_x, monstre_y, monstre_x
        )

        if not is_finishable(
            labyrinthe, entree_y, entree_x, sortie_y, sortie_x, monstre_y, monstre_x
        ):
            non_relance = False

    # restauration du labyrinthe si valider
    elif restaure.upper() == "O":
        print(afficher_sauvegarde)
        pseudo_restaure = input(yellow("entrer le pseudo: "))
        score_restaure = input(yellow("entrer le score: "))

        labyrinthe_recup = restaurer_partie(pseudo_restaure, score_restaure)
        if labyrinthe_recup:
            labyrinthe = labyrinthe_recup[0]

            entree_y = labyrinthe_recup[1]
            entree_x = labyrinthe_recup[2]
            monstre_x = labyrinthe_recup[3]
            monstre_y = labyrinthe_recup[4]

            tp_x = labyrinthe_recup[5]
            tp_y = labyrinthe_recup[6]
            tp2_x = labyrinthe_recup[7]
            tp2_y = labyrinthe_recup[8]
            tp3_x = labyrinthe_recup[9]
            tp3_y = labyrinthe_recup[10]
            tp4_x = labyrinthe_recup[11]
            tp4_y = labyrinthe_recup[12]
            tp5_x = labyrinthe_recup[13]
            tp5_y = labyrinthe_recup[14]
            tp6_x = labyrinthe_recup[15]
            tp6_y = labyrinthe_recup[16]

            sortie_x = labyrinthe_recup[17]
            sortie_y = labyrinthe_recup[18]
            difficulty = labyrinthe_recup[19]
            hauteur = labyrinthe_recup[20]
            largeur = labyrinthe_recup[21]
            thesee_x = labyrinthe_recup[22]
            thesee_y = labyrinthe_recup[23]
            score = labyrinthe_recup[24]
        else:
            print(yellow("Aucune partie trouvée pour ce pseudo et ce score."))
        non_relance = True
        restaure = "N"

    # -Faire avancer Thésée dans le labyrinthe
    while True:
        # -Ajouter des murs autour du labyrinthe
        for x in range(largeur):
            labyrinthe[0][x] = blue("□")
            labyrinthe[hauteur - 1][x] = blue("□")
        for y in range(hauteur):
            labyrinthe[y][0] = blue("□")
            labyrinthe[y][largeur - 1] = blue("□")

        # afficher entrée et sortie en permanence
        labyrinthe[entree_y][entree_x] = yellow("E")
        labyrinthe[sortie_y][sortie_x] = yellow("S")

        labyrinthe[thesee_y][thesee_x] = green("T")

        # arreter la génération en cours pour redémarrer
        if not non_relance:
            break

        # -regénérer le labyrinthe avec la position de Thésée en cas de dysfonctionnement sur l'apparition d'objet
        for y in range(hauteur):
            for x in range(largeur):
                print(labyrinthe[y][x], end=" ")
            print()

        # -Demander à l'utilisateur de choisir une direction
        print("score:", score)
        direction = input(yellow("Choisissez une direction (Z/Q/S/D) ou enregistrer (P): "))
        score -= 1
        print("")
        print("")
        print("")
        print("")
        print("")

        # -Ajouter la trace derrière Thésée
        if direction.upper() == "Q" and labyrinthe != blanc("#"):
            labyrinthe[thesee_y][thesee_x] = red("←")
        elif direction.upper() == "D" and labyrinthe != blanc("#"):
            labyrinthe[thesee_y][thesee_x] = red("→")
        elif direction.upper() == "Z" and labyrinthe != blanc("#"):
            labyrinthe[thesee_y][thesee_x] = red("↑")
        elif direction.upper() == "S" and labyrinthe != blanc("#"):
            labyrinthe[thesee_y][thesee_x] = red("↓")

        # -Déplacer Thésée dans la direction choisie
        if (
            direction.upper() == "Z"
            and labyrinthe[thesee_y - 1][thesee_x] != blanc("#")
            and labyrinthe[thesee_y - 1][thesee_x] != blue("□")
        ):
            thesee_y -= 1
        elif (
            direction.upper() == "S"
            and labyrinthe[thesee_y + 1][thesee_x] != blanc("#")
            and labyrinthe[thesee_y + 1][thesee_x] != blue("□")
        ):
            thesee_y += 1
        elif (
            direction.upper() == "Q"
            and labyrinthe[thesee_y][thesee_x - 1] != blanc("#")
            and labyrinthe[thesee_y][thesee_x - 1] != blue("□")
        ):
            thesee_x -= 1
        elif (
            direction.upper() == "D"
            and labyrinthe[thesee_y][thesee_x + 1] != blanc("#")
            and labyrinthe[thesee_y][thesee_x + 1] != blue("□")
        ):
            thesee_x += 1
        elif direction == "":
            print((red("Veuillez selectioner une direction")))

        elif direction.upper() == "P":
            # Concaténer les lignes avec des sauts de ligne pour obtenir une seule chaîne de caractères
            etat_matricee = json.dumps(labyrinthe)
            entree_x = int(entree_x)
            entree_y = int(entree_y)
            monstre_x = int(monstre_x)
            monstre_y = int(monstre_y)
            tp_x = int(tp_x)
            tp_y = int(tp_y)
            tp2_x = int(tp2_x)
            tp2_y = int(tp2_y)
            tp3_x = int(tp3_x)
            tp3_y = int(tp3_y)
            tp4_x = int(tp4_x)
            tp4_y = int(tp4_y)
            tp5_x = int(tp5_x)
            tp5_y = int(tp5_y)
            tp6_x = int(tp6_x)
            tp6_y = int(tp6_y)
            sortie_x = int(sortie_x)
            sortie_y = int(sortie_y)
            hauteur = int(hauteur)
            largeur = int(largeur)
            thesee_x = int(thesee_x)
            thesee_y = int(thesee_y)
            sauvegarder_partie(
                joueur,
                score,
                difficulty,
                etat_matricee,
                entree_y,
                entree_x,
                monstre_x,
                monstre_y,
                tp_x,
                tp_y,
                tp2_x,
                tp2_y,
                tp3_x,
                tp3_y,
                tp4_x,
                tp4_y,
                tp5_x,
                tp5_y,
                tp6_x,
                tp6_y,
                sortie_x,
                sortie_y,
                hauteur,
                largeur,
                thesee_x,
                thesee_y,
            )
            non_relance = True
            break
        else:
            print((red("Vous ne pouvez pas passer le mur")))

        # -Vérifier si Thésée a atteint le minautore
        if thesee_x == monstre_x and thesee_y == monstre_y:
            dead_m = True
            labyrinthe[monstre_y][monstre_x] = f"\x1b[8m{chr(9608)}\x1b[0m"

        # déplacement du minotaure dans le cadre
        if not dead_m:
            labyrinthe[monstre_y][monstre_x] = f"\x1b[8m{chr(9608)}\x1b[0m"
            if difficulty.upper() == "FACILE" or difficulty.upper() == "NORMALE":
                if (
                    direction.upper() == "Z"
                    or direction.upper() == "Q"
                    or direction.upper() == "S"
                    or direction.upper() == "D"
                ):
                    minotaure_dir = random.randint(0, 3)
                    if (
                        minotaure_dir == 0
                        and ((monstre_y - 1) >= 1)
                        and ((monstre_y - 1) < (hauteur - 1))
                    ):
                        if labyrinthe[monstre_y - 1][monstre_x] != blanc("#"):
                            monstre_y -= 1
                            labyrinthe[monstre_y][monstre_x] = magenta("M")
                        else:
                            labyrinthe[monstre_y][monstre_x] = magenta("M")
                            continue

                    elif (
                        minotaure_dir == 1
                        and ((monstre_y + 1) >= 1)
                        and ((monstre_y + 1) < (hauteur - 1))
                    ):
                        if labyrinthe[monstre_y + 1][monstre_x] != blanc("#"):
                            monstre_y += 1
                            labyrinthe[monstre_y][monstre_x] = magenta("M")
                        else:
                            labyrinthe[monstre_y][monstre_x] = magenta("M")
                            continue

                    elif (
                        minotaure_dir == 2
                        and ((monstre_x - 1) >= 1)
                        and ((monstre_x - 1) < (largeur - 1))
                    ):
                        if labyrinthe[monstre_y][monstre_x - 1] != blanc("#"):
                            monstre_x -= 1
                            labyrinthe[monstre_y][monstre_x] = magenta("M")
                        else:
                            labyrinthe[monstre_y][monstre_x] = magenta("M")
                            continue

                    elif (
                        minotaure_dir == 3
                        and ((monstre_x + 1) >= 1)
                        and ((monstre_x + 1) < (largeur - 1))
                    ):
                        if labyrinthe[monstre_y][monstre_x + 1] != blanc("#"):
                            monstre_x += 1
                            labyrinthe[monstre_y][monstre_x] = magenta("M")
                        else:
                            labyrinthe[monstre_y][monstre_x] = magenta("M")
                            continue
                    else:
                        labyrinthe[monstre_y][monstre_x] = magenta("M")
            elif difficulty.upper() == "DIFFICILE":
                if (
                    direction.upper() == "Z"
                    or direction.upper() == "Q"
                    or direction.upper() == "S"
                    or direction.upper() == "D"
                ):
                    minotaure_dir = random.randint(0, 3)
                    if (
                        minotaure_dir == 0
                        and ((monstre_y - 1) >= 1)
                        and ((monstre_y - 1) < (hauteur - 1))
                    ):
                        monstre_y -= 1
                        labyrinthe[monstre_y][monstre_x] = magenta("M")

                    elif (
                        minotaure_dir == 1
                        and ((monstre_y + 1) >= 1)
                        and ((monstre_y + 1) < (hauteur - 1))
                    ):
                        monstre_y += 1
                        labyrinthe[monstre_y][monstre_x] = magenta("M")

                    elif (
                        minotaure_dir == 2
                        and ((monstre_x - 1) >= 1)
                        and ((monstre_x - 1) < (largeur - 1))
                    ):
                        monstre_x -= 1
                        labyrinthe[monstre_y][monstre_x] = magenta("M")

                    elif (
                        minotaure_dir == 3
                        and ((monstre_x + 1) >= 1)
                        and ((monstre_x + 1) < (largeur - 1))
                    ):
                        monstre_x += 1
                        labyrinthe[monstre_y][monstre_x] = magenta("M")
                    else:
                        labyrinthe[monstre_y][monstre_x] = magenta("M")

        # -Vérifier si Thésée a atteint le minautore
        if thesee_x == monstre_x and thesee_y == monstre_y:
            dead_m = True
            print((yellow("Bravo, vous avez atteint le minautore !")) + Fore.RESET)

        # -Vérifier si Thésée a atteint un portail de téléportation
        if thesee_x == tp_x and thesee_y == tp_y:
            print((yellow("Bravo vous avez trouver un portail de teleportation !")))
            thesee_x, thesee_y = tp2_x, tp2_y
        elif thesee_x == tp2_x and thesee_y == tp2_y:
            print((yellow("Bravo vous avez trouver un portail de teleportation !")))
            thesee_x, thesee_y = tp_x, tp_y

        if difficulty.upper() == "FACILE":
            if thesee_x == tp3_x and thesee_y == tp3_y:
                print((yellow("Bravo vous avez trouver un portail de teleportation !")))
                thesee_x, thesee_y = tp4_x, tp4_y
            if thesee_x == tp4_x and thesee_y == tp4_y:
                print((yellow("Bravo vous avez trouver un portail de teleportation !")))
                thesee_x, thesee_y = tp3_x, tp3_y

            if thesee_x == tp5_x and thesee_y == tp5_y:
                print((yellow("Bravo vous avez trouver un portail de teleportation !")))
                thesee_x, thesee_y = tp6_x, tp6_y
            elif thesee_x == tp6_x and thesee_y == tp6_y:
                print((yellow("Bravo vous avez trouver un portail de teleportation !")))
                thesee_x, thesee_y = tp5_x, tp5_y
        elif difficulty.upper() == "NORMALE":
            if thesee_x == tp3_x and thesee_y == tp3_y:
                print((yellow("Bravo vous avez trouver un portail de teleportation !")))
                thesee_x, thesee_y = tp4_x, tp4_y
            if thesee_x == tp4_x and thesee_y == tp4_y:
                print((yellow("Bravo vous avez trouver un portail de teleportation !")))
                thesee_x, thesee_y = tp3_x, tp3_y

        # -Vérifier si Thésée a atteint la sortie
        if thesee_x == sortie_x and thesee_y == sortie_y and dead_m:
            print((yellow("Bravo, vous avez réussi à sortir du labyrinthe !")))
            print((yellow("Votre score final:", score)))
            sauvegarder_score(score, joueur, difficulty)
            break
        elif thesee_x == sortie_x and thesee_y == sortie_y and not dead_m:
            print((red("Vous n'avez pas tué le minautore !")))

        # score game over
        if score == 0:
            print((red("GAME OVER, VOUS ETES MORT DE SOIF")))
            break
        print("")

    # -Afficher le labyrinthe
    if non_relance:
        for ligne in labyrinthe:
            print(" ".join(ligne))

    while non_relance:
        record = str(input(red("souhaitez vous voir les 5 records? (O/N)")))
        if record.upper() == "O":
            if difficulty == "FACILE":
                afficher_top_scores_easy()
            elif difficulty == "NORMALE":
                afficher_top_scores_normal()
            elif difficulty == "DIFFICILE":
                afficher_top_scores_hard()
        else:
            pass
        choix = input(yellow("Voulez-vous relancer la partie ? (O/N) "))
        if choix.upper() == "O":
            break

        elif choix.upper() == "N":
            print(yellow("Merci d'avoir joué !"))
            time.sleep(2)
            quitte = True
            break

        else:
            print(red("Réponse invalide. Veuillez répondre par O ou N."))

    if quitte:
        break
