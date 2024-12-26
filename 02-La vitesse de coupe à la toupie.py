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