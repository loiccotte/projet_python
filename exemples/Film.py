# Film.py : un module qui contient une classe
class Film:
    # le constructeur : appelé quand on écrit Film(...)
    def __init__(self, titre, realisateur, annee):
        self.titre = titre              # self.titre : attribut gardé par l'objet
        self.realisateur = realisateur
        self.annee = annee
        self.notes = []                 # liste vide au départ
        self.nb_notes = 0

    # méthode qui MODIFIE l'objet : on touche à ses attributs via self
    def noter(self, note):
        self.notes.append(note)
        self.nb_notes += 1

    # méthode ordinaire : on l'appelle nous-même avec f.afficher()
    def afficher(self):
        print("Titre :", self.titre)
        print("Réalisateur :", self.realisateur)
        print("Année :", self.annee)

    # méthode spéciale : Python l'appelle tout seul lors d'un print(f)
    # attention : elle RETOURNE une chaîne, elle ne l'affiche pas
    def __str__(self):
        return self.titre + " (" + str(self.annee) + ")"
