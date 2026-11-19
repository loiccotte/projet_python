# Videotheque.py : une collection de films, en patron SINGLETON

class Videotheque:
    instance = None               # attribut de CLASSE : le « tiroir » qui garde l'objet unique

    def __init__(self):
        self.films = []

    # PATRON SINGLETON : le « guichet », seule porte pour obtenir LA vidéothèque
    @classmethod                  # s'appelle sur la classe : Videotheque.get_instance()
    def get_instance(cls):
        if cls.instance is None:          # tiroir vide : on crée l'objet et on le range
            cls.instance = Videotheque()
        return cls.instance               # sinon : on renvoie celui du tiroir

    def ajouter(self, film):
        self.films.append(film)

    # POLYMORPHISME : écrite une seule fois, cette méthode marche pour
    # n'importe quel type de film, même ceux créés après elle
    def afficher(self):
        for film in self.films:
            print(film)
