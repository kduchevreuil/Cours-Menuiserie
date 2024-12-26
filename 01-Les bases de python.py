# Les variables en python
# Les variables sont des espaces mémoire qui permettent de stocker des valeurs.
# En python, on peut déclarer une variable et lui affecter une valeur en une seule instruction.

# Types de variables

a = "Bonjour" # chaine de caractères : str
b = 5 # nombre entier : int
c = 1.5 # nombre à virgules : float
d = True # True ou False : bool

# Print et Input

nom = input("Quel est votre nom ?")
print("Vous vous appelez " + nom) # concaténation de chaine
print(f"Vous vous appelez {nom}") # chaine formatée
print("Vous vous appelez %s" % nom) # chaine formatée (ancien format)

# Commentaire sur une ligne

"""Commentaire
sur
plusieurs 
lignes""" 

# Conversions

age = 30
print("Votre age est: " + str(age)) # conversion de int vers str, et concaténation
age_str = "30"
age_int = int(age_str) # conversion de str vers int.


# Boucle While
nom = ""
while nom == "":
    nom = input("Quel est votre nom? ")
    if nom == "":
        print("Vous devez rentrer un nom")
    else:
        print("Vous vous appelez " + nom)


# Boucle For
# Boucle un nombre de fois
for i in range(0, 4): # de 0 (inclus) à 4 (exclu) : 0, 1, 2, 3
    print(i) # affiche 0, 1, 2, 3

# Fonctions
# Définition (taille est un paramètre optionnel)
def afficher_informations_personne(nom, age, taille=0):
    print("Vous vous appelez " + nom + ", vous avez " + str(age) + " ans")

# Appel
afficher_informations_personne("Jean", 25)


# Conditions
# ==
# <=
# <
# >=
# >
if age == 17:
    print("Vous êtres presque majeur")
elif 12 <= age < 18:
    print("Vous êtes adolescent")
elif age == 1 or age == 2:
    print("Vous êtes un bébé")
elif age >= 18:
    print("Vous êtes majeur")
else:
    print("Vous êtes mineur")
    

# Importer le module math, qui contient des fonctions mathématiques comme pi
import math

# Demander à l'utilisateur de saisir le diamètre de l'outil
diametre_input = input("Entrez le diamètre de l'outil en mètres : ")

# Convertir la saisie en un nombre flottant (float)
diametre_outil = float(diametre_input)

# Demander à l'utilisateur de saisir la vitesse de rotation de la toupie en tr/min
vitesse_input = input("Entrez la vitesse de rotation de la toupie en tr/min : ")

# Convertir la saisie en un nombre flottant (float)
vitesse_rotation = float(vitesse_input)

# Calculer la vitesse de coupe en utilisant la formule V_c = π * D * N
vitesse_coupe = math.pi * diametre_outil * vitesse_rotation

# Afficher le résultat avec une précision de deux décimales en mètres par minute
print(f"La vitesse de coupe est de {vitesse_coupe} m/min.")
