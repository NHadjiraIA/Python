"""
Nom du projet:apprendre Python 3
Date de la derniere revision :03/08/2020
Ateur :Hadjira Haya
Revision :reviion numero 1
Client E-learning
Fichiers du projet :
       -Fonction avec parametre
"""

# ---------------------programme principal----------------------

# -------------------------------------
# -----------------------------Improte de modules---------------------
import math
# -------------------------------------------------------------------

# -----------------------Variables globals-------------------------------

# ----------------------------------------------------------------------------------------

# ----------------------------Modules et fonctions ----------------------------------------
#----------------------------------Fonction avec paramètres--------------------------------
def volume(longueur, largeur, hauteur, rayon):
    print("le volume du cube est de : %.2f"%(longueur ** 3), "m3.")
    print("Le volume du parallélépipède est de : %.2f" % (longueur * largeur * hauteur), "m3.")
    print("Le volume de la sphère est de : %.2f" % (4 / 3 * math.pi * rayon ** 3), "m3.")

#--------------------------------------------------------------------------------------------
#-----------------------Fonction avec paramètres->avec valeur retourné-----------------------
def volumesFigures():

    valeur_saisie=input("Entrez la longueur du parallélépipède :")
    ma_longueur=float(valeur_saisie)

    valeur_saisie=input("Entrez la largeur du parallélépipède :")
    ma_largeur=float(valeur_saisie)

    valeur_saisie=input("Entrez la hauteur du parallélépipède :")
    ma_hauteur=float(valeur_saisie)

    valeur_saisie=input("Entrez le rayon de la sphère :")
    mon_rayon=float(valeur_saisie)

    return print("Le volume du cube est de : %.2f"%(ma_longueur**3),"m3, Le volume du parallélépipède est de : %.2f"%(ma_longueur*ma_largeur*ma_hauteur),
             "m3 le volume de la sphère est de : %.2f" % (4 / 3 * math.pi * mon_rayon ** 3),"m3.")
#--------------------------------------------------------------------------------------------------
# -----------------------Programme-----------------------------------------------------------------
#-------------------------------Exemple N 1--------------------------------------------------------
print("Exemple 1")
valeur_saisie =input("Entrez la longueur du parallélépipède :")
ma_longueur=float(valeur_saisie)
valeur_saisie =input("Entrez la largeur du parallélépipède :")
ma_largeur=float(valeur_saisie)
valeur_saisie=input("Entrez la hauteur du parallélépipède :")
ma_hauteur=float(valeur_saisie)

valeur_saisie=input("Entrez le rayon de la sphère :")
mon_rayon=float(valeur_saisie)
volume(ma_hauteur ,ma_largeur ,ma_hauteur ,mon_rayon)
print("Fin exemple N°1\n")

#----------------------------------------------------------------------------------------------
#-----------------------------------------------Exemple N2-------------------------------------
print("Exemple 2 - Les paramètres sont inclus dans la fonction !")
volumesFigures()
print("Fin exemple N°2\n")