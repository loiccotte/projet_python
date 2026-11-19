import datetime


class Document:

    def __init__(self, titre, auteur, date, url, texte):
        self.titre = titre
        self.auteur = auteur
        self.date = date
        self.url = url
        self.texte = texte

    def afficher(self):
        print("Titre :", self.titre)
        print("auteur :", self.auteur)
        print("date :", self.date)
        print("Url :", self.url)
        print("texte :", self.texte)

    def __str__(self):
        return f"{self.titre} ({str(self.date)}),auteur : {self.auteur} url : {self.url}, texte : {self.texte}"


    def __str__(self):
        return f'{self.}'
