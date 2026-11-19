import pandas as pd
from datetime import datetime
from Document import Document
from Auteur import Auteur

class Corpus:
    def __init__(self, nom):
        self.nom = nom
        self.auteur = {}
        self.id2doc = {}
        self.ndoc = 0
        self.naut = 0

    def add(self, doc):
        doc_id = self.ndoc
        self.id2doc[doc_id] = doc
        self.ndoc += 1

        noms_auteurs = [a.strip() for a in doc.auteur.split(",") if a.strip()]
        for nom_aut in noms_auteurs:
            if nom_aut not in self.auteur:
                self.auteur[nom_aut] = Auteur(nom_aut)
                self.naut += 1
            self.authors[nom_aut].add(doc_id, doc)

    
    def show_by_date(self, n=5):
        docs_tries = sorted(self.id2doc.values(), key=lambda d: d.date, reverse=True)
        print(f"documents les plus récents du corpus '{self.nom}'")
        for doc in docs_tries[:n]:
            print(f"[{doc.date.strftime('%Y-%m-%d')}] {doc.titre} ({doc.auteur})")

    def show_by_title(self, n=5):
        docs_tries = sorted(self.id2doc.values(), key=lambda d: d.titre.lower())
        print(f"premiers documents par ordre alphabétique")
        for doc in docs_tries[:n]:
            print(f"{doc.titre} - {doc.auteur} ({doc.date.strftime('%Y-%m-%d')})")

    def __repr__(self):
        return f"Corpus '{self.nom}' : {self.ndoc} documents, {self.naut} auteurs"

    def save(self, chemin_fichier):
        data = []
        for doc_id, doc in self.id2doc.items():
            data.append({
                "id": doc_id,
                "titre": doc.titre,
                "auteur": doc.auteur,
                "date": doc.date.strftime("%Y-%m-%d %H:%M:%S"),
                "url": doc.url,
                "texte": doc.texte
            })
        df = pd.DataFrame(data)
        df.to_csv(chemin_fichier, sep="\t", index=False)
        print(f"Corpus '{self.nom}' sauvegardé dans '{chemin_fichier}'.")

    def load(self, chemin_fichier):
        df = pd.read_csv(chemin_fichier, sep="\t")
        self.auteur = {}
        self.id2doc = {}
        self.ndoc = 0
        self.naut = 0

        for _, row in df.iterrows():
            date_obj = datetime.strptime(str(row["date"]), "%Y-%m-%d %H:%M:%S")
            doc = Document(
                titre=str(row["titre"]),
                auteur=str(row["auteur"]),
                date=date_obj,
                url=str(row["url"]),
                texte=str(row["texte"])
            )
            self.add(doc)
        print(f"Corpus '{self.nom}' rechargé : {self.ndoc} documents, {self.naut} auteurs.")
