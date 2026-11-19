# Classe auteur
class Auteur:
    def __init__(self, name):
        self.name = name
        self.ndoc = 0
        self.production = {}

    def add(self, doc_id, doc):
        self.production[doc_id] = doc
        self.ndoc = len(self.production)

    def afficher_infos(self):
        print(f"Nom de l'auteur     : {self.name}")
        print(f"Nombre de documents : {self.ndoc}")
        print("Production          :")
        for doc_id, doc in self.production.items():
            print(f"  - [{doc_id}] {doc.titre}")

    def __str__(self):
        return f"Auteur : {self.name} ({self.ndoc} document(s))"
