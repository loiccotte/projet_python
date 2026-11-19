from Document import Document

class ArxivDocument:
    
    def __init__(self, titre, auteur, date, url, texte, coAuteurs = []):
        super().__init__(titre, auteur, date, url, texte)
        self.coAuteurs = coAuteurs

    def getcoAuteurs(self):
        return self.coAuteur

    def setcoAuteurs(self,listCoAuteur):
        self.coAuteurs = listCoAuteur

    def __str__(self):
            return f"arxiv document {super().__str__()}"