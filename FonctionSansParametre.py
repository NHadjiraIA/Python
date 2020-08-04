"""
Nom du projet:apprendre Python 3
Date de la derniere revision :03/08/2020
Ateur :Hadjira Haya
Revision :reviion numero 1
Client E-learning
Fichiers du projet :
       -Fonction sans parametre
"""

# ---------------------programme principal----------------------

# -------------------------------------
# -----------------------------Improte de modules---------------------

# -------------------------------------------------------------------

# -----------------------Variables globals-------------------------------

# --------------------------------------------------------------------

# ----------------------------Modules et fonctions -------------------------
# Fonction sans paramètre-> () vide
def compteur3():
    increment = 0                   # Variable locale à la fonction, la portée de cette variable ne concerne que compteur3().
    while increment < 3:
        print("Compte",increment,"fois")
        increment = increment + 1

#-----------------------------------
#-------------------------------------------------------------------------------
# Fonction qui appelle une autre fonction

def doubleCompteur3():
    compteur3()
    print ("Compte encore une 2ème fois")
    compteur3()
#---------------------------Fonction qui calcule volume cube ---------------------------
def volumeCube():
    cote=10
    print("le volume cube de 10 m de cote est:",10*10*10, "m3")
    print("Normalement, on obtient 1000 m3.")
# ---------------------------------------------------------------------------------------

# -----------------------Programme-------------------------------------------------------
#-------------------------------Exemple N 1----------------------------------------------
print("Exemple 1")
compteur3()
print("Fin exemple N°1\n")

#-----------------------------------------------------------------------------------------
#-------------------------------Exemple N 2-----------------------------------------------
print("Exemple N 2")
doubleCompteur3()
print("Fin de exemple N2 \n")
#-----------------------------------------------------------------------------------------

#-------------------------------Exemple N 3-----------------------------------------------
print("Exemple N 3")
volumeCube()
print("Fin de exemple N3 \n")
#-----------------------------------------------------------------------------------------
