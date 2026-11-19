import json
import html
import urllib.request
import urllib.parse
import xmltodict
import pandas as pd
from datetime import datetime
from Document import Document
from Auteur import Auteur
from Corpus import Corpus

theme = "climat"
id2doc = {}
id2aut = {}
doc_id = 0
corpus = Corpus(theme)

params = {"query": theme, "tags": "story", "hitsPerPage": 50}
url = f"https://hn.algolia.com/api/v1/search?{urllib.parse.urlencode(params)}"


with urllib.request.urlopen(url) as response:
    d_hn = json.load(response)
print(d_hn.keys())

print(d_hn["nbHits"])

hits = d_hn["hits"]
print(len(hits))

print(hits[0].keys())

for hit in hits:
    titre = hit.get("title", "")
    auteur = hit.get("author", "Inconnu")
    date_pub = datetime.fromtimestamp(hit["created_at_i"])
    url_doc = (
        hit.get("url") or f"https://news.ycombinator.com/item?id={hit['objectID']}"
    )
    texte = hit.get("story_text")
    if not texte:
        texte = hit.get("title", "")
    texte = html.unescape(texte).replace("<p>", " ").strip()
    doc = Document(titre=titre, auteur=auteur, date=date_pub, url=url_doc, texte=texte)
    corpus.add(doc)


url_arxiv = "http://export.arxiv.org/api/query?" + urllib.parse.urlencode(
    {"search_query": "all :" + theme, "start": 0, "max_results": 50}
)
print(url_arxiv)

with urllib.request.urlopen(url_arxiv) as response:
    d_arxiv = xmltodict.parse(response.read())

entrees = d_arxiv["feed"].get("entry", [])

if isinstance(entrees, dict):
    entrees = [entrees]

for entree in entrees:
    titre = entree["title"].replace("\n", " ").strip()
    if isinstance(entree["author"], list):
        liste_auteurs = [a["name"] for a in entree["author"]]
    else:
        liste_auteurs = [entree["author"]["name"]]

    date_pub = datetime.strptime(entree["published"][:10], "%Y-%m-%d")
    url_doc = entree["id"]
    texte = entree["summary"].replace("\n", " ").strip()
    doc = Document(
        titre=titre,
        auteur=", ".join(liste_auteurs),
        date=date_pub,
        url=url_doc,
        texte=texte,
    )
    corpus.add(doc)


df = pd.DataFrame({"id": range(len(docs)), "texte": docs, "origine": origines})
print(df.shape)
print(df.head())
print(df["origine"].value_counts())

df.to_csv("corpus.csv", sep="\t", index=False)
df = pd.read_csv("corpus.csv", sep="\t")
print(df.shape)
print("Nombre de documents :", len(df))

for texte in df["texte"]:
    mots = texte.split(" ")
    phrases = texte.split(".")
    print(len(mots), "mots,", len(phrases), "phrases")

print("Avant filtrage :", len(df))
df = df[df["texte"].str.len() >= 20]
print("Après filtrage :", len(df))

chaine = " ".join(df["texte"])
print(len(chaine))
print(chaine[:500])

nom_recherche = input("Entrez le nom de l'auteur recherché : ").strip()

if nom_recherche in id2aut:
    auteur_obj = id2aut[nom_recherche]
    nb_docs = auteur_obj.ndoc

    total_caracteres = 0
    total_mots = 0

    for doc in auteur_obj.production.values():
        total_caracteres += len(doc.texte)
        total_mots += len(doc.texte.split())

    taille_moy_car = total_caracteres / nb_docs
    taille_moy_mots = total_mots / nb_docs

    print(f"\n--- Statistiques pour {auteur_obj.name} ---")
    print(f"Nombre de documents produits : {nb_docs}")
    print(f"Taille moyenne (caractères)  : {taille_moy_car:.1f} caractères")
    print(f"Taille moyenne (mots)        : {taille_moy_mots:.1f} mots")
else:
    print(f"L'auteur '{nom_recherche}' n'a pas été trouvé dans la base.")


print(corpus)
corpus.show_by_date(5)
print()
corpus.show_by_title(5)

corpus.save("corpus_climat.csv")

corpus_charge = Corpus("Climat (rechargé)")
corpus_charge.load("corpus_climat.csv")
print(corpus_charge)
corpus_charge.show_by_date(3)

from HackerNewsDocument import HackerNewsDocument
from ArxivDocument import ArxivDocument

corpus = Corpus("Corpus_3.1")
h1 = HackerNewsDocument(
    "T1", "A1", datetime(2026, 11, 1), "http://hn/1", "texte hn 1", 10
)
h2 = HackerNewsDocument(
    "T2", "A2", datetime(2026, 11, 2), "http://hn/2", "texte hn 2", 25
)
a1 = ArxivDocument(
    "T3", "A3", datetime(2026, 11, 3), "http://arxiv/1", "texte arxiv 1", ["A4", "A5"]
)
a2 = ArxivDocument(
    "T4", "A1", datetime(2026, 11, 4), "http://arxiv/2", "texte arxiv 2", ["A6"]
)
corpus.add(h1)
corpus.add(h2)
corpus.add(a1)
corpus.add(a2)

print(corpus)

for document in corpus.id2doc.values():
    print(doc)
