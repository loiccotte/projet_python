from Document import Document
from HackerNewsDocument import HackerNewsDocument
from ArxivDocument import ArxivDocument


class DocumentFactory:
    @staticmethod
    def create_document(source, titre, auteur, date, url, texte, **kwargs):
        if source.lower() in ["hacker news", "hn"]:
            return HackerNewsDocument(
                titre, auteur, date, url, texte, kwargs.get("nb_commentaires", 0)
            )
        elif source.lower() == "arxiv":
            return ArxivDocument(
                titre, auteur, date, url, texte, kwargs.get("coAuteurs", [])
            )
        return Document(titre, auteur, date, url, texte)
