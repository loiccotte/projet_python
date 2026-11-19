# main.py : démo TD5, à lancer dans le même dossier que Film.py et Videotheque.py
from Film import Film, Documentaire, FilmFactory
from Videotheque import Videotheque

print("1. Héritage et super()")
d = Documentaire("Microcosmos", "Nuridsany", 1996, "insectes")
print(d.titre, d.annee)        # attributs hérités de Film, remplis par super().__init__
print(isinstance(d, Film))     # True : un Documentaire EST UN Film

print("\n2. Accesseur et mutateur")
print(d.get_sujet())
d.set_sujet("")                # refusé : le mutateur contrôle la valeur
d.set_sujet("nature")
print(d.get_sujet())
# SANS mutateur : rien n'empêche d'écrire n'importe quoi
d.sujet = ""
print("Après modification directe :", repr(d.sujet))
d.sujet = "insectes"

print("\n3. Polymorphisme")
films = [Film("Alien", "Scott", 1979), d]
# SANS : il faudrait tester le type de chaque objet, à chaque affichage
for f in films:
    if isinstance(f, Documentaire):
        print("[Documentaire] " + f.titre + " (" + str(f.annee) + ") : " + f.sujet)
    else:
        print(f.titre + " (" + str(f.annee) + ")")
# AVEC : la même ligne pour tous, chaque objet utilise SON __str__
for f in films:
    print(f)
# Champ type : chaque objet indique sa catégorie, sans aucun test de type
for f in films:
    print(f.getType(), ":", f.titre)

#pour plus d'informations sur les patrons, livre : Design Patterns: Elements of Reusable Object-Oriented Software
print("\n4. Singleton")
# SANS : chaque Videotheque() crée une nouvelle vidéothèque, vide
v1 = Videotheque()
v1.ajouter(d)
v2 = Videotheque()
print("Sans singleton :", len(v2.films), "film dans v2")
# AVEC : on passe par le guichet, et on obtient toujours la même
v1 = Videotheque.get_instance()
v1.ajouter(d)
v2 = Videotheque.get_instance()
print("Avec singleton :", len(v2.films), "film dans v2")
print("v1 et v2 sont le même objet :", v1 is v2)

print("\n 5. Usine")
# SANS : le programme principal choisit lui-même la classe, à chaque création
genre = "documentaire"
if genre == "documentaire":
    f = Documentaire("Océans", "Perrin", 2009, "mer")
else:
    f = Film("Océans", "Perrin", 2009)
# AVEC : on demande à l'usine, qui sait quelle classe créer
catalogue = [("film", "Gladiator", "Scott", 2000, None),
             ("documentaire", "Océans", "Perrin", 2009, "mer")]
v = Videotheque.get_instance()     # toujours la même vidéothèque (singleton)
for genre, titre, real, annee, sujet in catalogue:
    v.ajouter(FilmFactory.creer(genre, titre, real, annee, sujet))
v.afficher()                       # polymorphisme : afficher ne connaît pas les types
