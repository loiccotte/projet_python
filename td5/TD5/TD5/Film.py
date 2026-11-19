# Film.py : la classe mère, une classe fille et une usine

class Film:
    def __init__(self, titre, realisateur, annee):
        self.titre = titre
        self.realisateur = realisateur
        self.annee = annee
        self.type = "Film"              # champ type, dans la classe mère

    def __str__(self):
        return self.titre + " (" + str(self.annee) + ")"

    def getType(self):
        return self.type


# HÉRITAGE : Documentaire est une classe FILLE de Film (la classe MÈRE).
# Un documentaire EST UN film : il récupère tous les attributs et méthodes de Film.
class Documentaire(Film):
    def __init__(self, titre, realisateur, annee, sujet):
        # super() = la classe mère : on lui laisse remplir les attributs communs
        super().__init__(titre, realisateur, annee)
        # puis on ajoute le champ SPÉCIFIQUE à la classe fille
        self.sujet = sujet
        # la fille remplace la valeur du champ type hérité
        self.type = "Documentaire"

    # ACCESSEUR (getter) : lire le champ
    def get_sujet(self):
        return self.sujet

    # MUTATEUR (setter) : modifier le champ, en contrôlant la valeur
    def set_sujet(self, sujet):
        if sujet == "":
            print("Sujet vide refusé")
        else:
            self.sujet = sujet

    # REDÉFINITION : même nom que dans Film, c'est cette version qui est utilisée
    def __str__(self):
        return "[Documentaire] " + self.titre + " (" + str(self.annee) + ") : " + self.sujet


# PATRON USINE (factory) : un seul endroit qui sait quelle classe créer
class FilmFactory:
    @staticmethod                 # s'appelle sur la classe : FilmFactory.creer(...)
    def creer(genre, titre, realisateur, annee, sujet=None):
        if genre == "film":
            return Film(titre, realisateur, annee)
        elif genre == "documentaire":
            return Documentaire(titre, realisateur, annee, sujet)
        else:
            raise ValueError("Genre inconnu : " + genre)
