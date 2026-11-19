from Document import Document


class HackerNewsDocument(Document):

    def __init__(self, titre, auteur, date, url, texte, nb_commentaires=0):
        super().__init__(titre, auteur, date, url, texte)
        self.nb_commentaires = nb_commentaires

    def getNbCommentaire(self):
        return self.nb_commentaires

    def __str__(self):
        return f"Article HackerNews {super().__str__()}"
