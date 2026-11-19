from urllib import request, parse
import json
import html
from Document import Document

docs = []

mot = "climate"

params = {"query": mot, "tags": "story", "hitsPerPage": 50}
url = f"https://hn.algolia.com/api/v1/search?{parse.urlencode(params)}"


reponse = request.urlopen(url)
data = json.load(reponse)
# print(url)
# print(data)


id2doc = {}
compteur = 0
for post in data["hits"]:
    titre = post.get("title")
    texte = post.get("story_text")
    auteur = post.get("author")
    date = post.get("created_at")
    url = post.get("url")

    id2doc[compteur] = Document(
        titre=titre, texte=texte, auteur=auteur, date=date, url=url
    )
    compteur += 1

print(docs)
