# Ecrire un commentaire

"""
Ecrire un commentaire sur plusieurs lignes
"""

nom = input("Quel est ton nom ?")
age = input("Quel est ton age ?")

# nom = "toto"
# age = 30
print(type(nom))
print(type(age))

try:
    age_prochain = int(age) + 1
except:
    print("ERREUR: Vous devez renter un nombre pour l'age")


print(f"Vous vous appellez {nom}. ")
print("Vous avez " + age + " ans. ")
print("L'an prochain vous aurez " + str(age_prochain) + " ans. ")



