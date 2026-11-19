# main.py : le programme principal, dans le même dossier que Film.py
from Film import Film     # depuis le fichier Film.py, on importe la classe Film

# 1. créer un objet et l'afficher de deux façons
f = Film("Amélie", "Jeunet", 2001)
f.afficher()
print(f)                  # utilise __str__

# 2. ranger des objets dans un dictionnaire, avec un compteur comme clé
id2film = {}
compteur = 0
for titre, real, annee in [("Alien", "Scott", 1979),
                           ("Delicatessen", "Jeunet", 1991),
                           ("Gladiator", "Scott", 2000)]:
    id2film[compteur] = Film(titre, real, annee)
    compteur += 1

# 3. regrouper : on crée l'entrée seulement si la clé n'existe pas encore
nb_par_real = {}
for film in id2film.values():
    if film.realisateur not in nb_par_real:
        nb_par_real[film.realisateur] = 0
    nb_par_real[film.realisateur] += 1
print(nb_par_real)

# 4. trier des objets selon un de leurs attributs
for film in sorted(id2film.values(), key=lambda film: film.annee):
    print(film)

# 5. appeler une méthode sur un objet rangé dans un dictionnaire
id2film[0].noter(4)       # id2film[0] est un Film : on peut appeler ses méthodes
id2film[0].noter(5)
print(id2film[0], ":", id2film[0].nb_notes, "notes", id2film[0].notes)
