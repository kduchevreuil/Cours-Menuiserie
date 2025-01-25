import math

print('''
      
 ▌ ▐·▪  ▄▄▄▄▄▄▄▄ ..▄▄ · .▄▄ · ▄▄▄ .    ·▄▄▄▄  ▄▄▄ .     ▄▄·       ▄• ▄▌ ▄▄▄·▄▄▄ .
▪█·█▌██ •██  ▀▄.▀·▐█ ▀. ▐█ ▀. ▀▄.▀·    ██▪ ██ ▀▄.▀·    ▐█ ▌▪▪     █▪██▌▐█ ▄█▀▄.▀·
▐█▐█•▐█· ▐█.▪▐▀▀▪▄▄▀▀▀█▄▄▀▀▀█▄▐▀▀▪▄    ▐█· ▐█▌▐▀▀▪▄    ██ ▄▄ ▄█▀▄ █▌▐█▌ ██▀·▐▀▀▪▄
 ███ ▐█▌ ▐█▌·▐█▄▄▌▐█▄▪▐█▐█▄▪▐█▐█▄▄▌    ██. ██ ▐█▄▄▌    ▐███▌▐█▌.▐▌▐█▄█▌▐█▪·•▐█▄▄▌
. ▀  ▀▀▀ ▀▀▀  ▀▀▀  ▀▀▀▀  ▀▀▀▀  ▀▀▀     ▀▀▀▀▀•  ▀▀▀     ·▀▀▀  ▀█▄▀▪ ▀▀▀ .▀    ▀▀▀ 
 ▄▄▄·     ▄▄▌   ▄▄▄·     ▄▄▄▄▄      ▄• ▄▌ ▄▄▄·▪  ▄▄▄ .                           
▐█ ▀█     ██•  ▐█ ▀█     •██  ▪     █▪██▌▐█ ▄███ ▀▄.▀·                           
▄█▀▀█     ██▪  ▄█▀▀█      ▐█.▪ ▄█▀▄ █▌▐█▌ ██▀·▐█·▐▀▀▪▄                           
▐█ ▪▐▌    ▐█▌▐▌▐█ ▪▐▌     ▐█▌·▐█▌.▐▌▐█▄█▌▐█▪·•▐█▌▐█▄▄▌                           
 ▀  ▀     .▀▀▀  ▀  ▀      ▀▀▀  ▀█▄▀▪ ▀▀▀ .▀   ▀▀▀ ▀▀▀                                                              
                                                                                                                                                                        ░                ░                                          
     ''')


def calculer_vitesse_coupe():
    # Demander à l'utilisateur de saisir le diamètre de l'outil
    diametre_input = input("Entrez le diamètre de l'outil en mètres : ")
    # Convertir la saisie en un nombre flottant (float)
    diametre_outil = float(diametre_input)

    # Convertir le diamètre de l'outil en millimètres et centimètres
    diametre_outil_mm = diametre_outil * 1000
    diametre_outil_cm = diametre_outil * 100
    print(f"Le diamètre de l'outil est de {diametre_outil_mm} mm.")
    print(f"Le diamètre de l'outil est de {diametre_outil_cm} cm.")

    # Demander à l'utilisateur de saisir la vitesse de rotation de la toupie en tr/min
    vitesse_input = input(
        "Entrez la vitesse de rotation de la toupie en tr/min : ")
    # Convertir la saisie en un nombre flottant (float)
    vitesse_rotation = float(vitesse_input)

    # Calculer la vitesse de coupe en utilisant la formule V_c = π * D * N
    vitesse_coupe = math.pi * diametre_outil * vitesse_rotation

    # Afficher le résultat avec une précision de deux décimales en mètres par minute
    print(f"La vitesse de coupe est de {vitesse_coupe} m/min.")

    # convertir la vitesse de coupe en km/h
    vitesse_coupe_kmh = vitesse_coupe * 60 / 1000
    print(f"La vitesse de coupe est  de {vitesse_coupe_kmh} km/h.")


# Appeler la fonction pour exécuter le code
calculer_vitesse_coupe()
