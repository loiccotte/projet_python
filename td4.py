import json
import xml.etree.ElementTree as ET
from urllib import parse, request

from Document import Document

mot = "climate"
id2doc = {}
compteur = 0

# --- Source 1 : Hacker News ---
params = {"query": mot, "tags": "story", "hitsPerPage": 50}
url = f"https://hn.algolia.com/api/v1/search?{parse.urlencode(params)}"
data = json.load(request.urlopen(url))

for post in data["hits"]:
    id2doc[compteur] = Document(
        titre=post.get("title"),
        auteur=post.get("author"),
        date=post.get("created_at"),
        url=post.get("url"),
        texte=post.get("story_text"),
    )
    compteur += 1

# --- Source 2 : arXiv ---
params = {"search_query": f"all:{mot}", "start": 0, "max_results": 50}
url = f"http://export.arxiv.org/api/query?{parse.urlencode(params)}"
ns = {"a": "http://www.w3.org/2005/Atom"}
root = ET.fromstring(request.urlopen(url).read())

for entry in root.findall("a:entry", ns):
    auteurs = [n.text for n in entry.findall("a:author/a:name", ns)]
    id2doc[compteur] = Document(
        titre=" ".join(entry.findtext("a:title", "", ns).split()),
        auteur=auteurs[0] if auteurs else None,
        date=entry.findtext("a:published", None, ns),
        url=entry.findtext("a:id", None, ns),
        texte=" ".join(entry.findtext("a:summary", "", ns).split()),
    )
    compteur += 1

print(f"{len(id2doc)} documents")
for doc in list(id2doc.values())[:5]:
    print(doc)
