from Document import Document

class ArxivDocument(Document):
    
    def __init__(self, titre, auteur, date, url, texte, coAuteurs = []):
        super().__init__(titre, auteur, date, url, texte)
        self.type = "Arxiv"
        self.coAuteurs = coAuteurs

    def getType(self):
        return self.type

    def getcoAuteurs(self):
        return self.coAuteur

    def setcoAuteurs(self,listCoAuteur):
        self.coAuteurs = listCoAuteur

    def __str__(self):
            return f"arxiv document {super().__str__()}"