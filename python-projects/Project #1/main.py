# Ecrire un commentaire

"""
Ecrire un commentaire sur plusieurs lignes
"""


def demander_nom():
    nom = ""
    while nom == "":
        nom = input("Quel est ton nom ?")
    print(f"Vous vous appellez {nom}. ")
    return nom


# # nom = "toto"
# # age = 30
# print(type(nom))
# print(type(age))

def demander_age():
    age = 0
    while age == 0:
        age_str = input("Quel est ton age ?")
        try:
            age = int(age_str)
        except ValueError:
            print("ERREUR: Vous devez renter un nombre pour l'age")  
    return age

def afficher_infos_personne(nom, age):
    print()
    print(f"Vous vous appelez {nom}")
    print("Vous avez " + str(age) + " ans. ")
    print("L'an prochain vous aurez " + str(age + 1) + " ans. ")

    if age == 17:
        print("presque, reviens dans un an !")
    elif age == 18:
        print("tout juste comment ça va jeune homme !")
    elif age >= 65:
        print("Hey, old man")
    elif age <= 10:
        print("little boy")
    elif age > 18:
        print("Bienvenue")
    else:
        print("Sors d'ici gamin !")


# n = 0

# print("Début de la boucle")
# while n < 4:
#     print("Valeur de n: " + str(n))
#     n += 1
# print("Fin de la boucle")

# mot_de_passe = ""
# while not mot_de_passe == "TOTO":
#     mot_de_passe = input("Quel est le mot de passe ? ")

# print("Mot de passe correct,vous avez accès au compte")

# # demander nom
# nom = demander_nom()

# # demander age
# age = demander_age()


# afficher_infos_personne(nom,age)

NB_PERSONNES = 3

for i in range(0,NB_PERSONNES):
    nom = "personne" + str(i+1)
    age = demander_age()
    afficher_infos_personne(nom,age)








