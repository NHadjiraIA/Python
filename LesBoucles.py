"""
Nom du projet:apprendre Python 3
Date de la derniere revision :02/08/2020
Ateur :Hadjira Haya
Revision :reviion numero 1
Client E-learning
Fichiers du projet :
       - Les Boucles
"""

# ---------------------programme principal----------------------

# -------------------------------------
# -----------------------------Improte de modules---------------------

# -------------------------------------------------------------------

# -----------------------Variables globals-------------------------------
valeur_mystere = 8
increment = 1
increment = 2
# -------------------------------------------------------------------------

# ----------------------------Modules et fonctions -------------------------

# ---------------------------------------------------------------------------
# -----------------------Programme-------------------------------------------
# -------------------Boucle If Else------------------------------------------
donne_saisie=input("entrer une valeur entre 0 et 10 ")
valeur_test=int(donne_saisie)
if valeur_test<0:
    print("votre valeur est negative ")
else:
    print("votre valeur est positive")
    if (valeur_test==8):
        print("bravo vous avez trouve la valeur mystere")
    else:
        print("vous n'avez pas trouve la valeur mystere")
        print("\n c'est la fin de la boucle if")


# #----------------------------------------------------------------------------
# #----------------------bocle while--------------------------------------------
valeur_saisi= input("donne la table de multiplication que vous veullez calculer\n")
table_multip= int(valeur_saisi)
valeur_saisi=input("donner la valeur maximale de votre calcul\n")
valeur_max=int(valeur_saisi)
valeur_saisi=input("donne le pas de votre calcul\n")
valeur_pas= int(valeur_saisi)
while increment is not valeur_max:
    print(increment,"*" ,table_multip, "=" ,increment*table_multip ,";")
    increment=increment+valeur_pas

print("\n c'est la fin de la boucle while")
# -------------------------------------------------------------------------------
# ---------------bocle for-------------------------------------------------------
message="Python 3.6 est genial"
for lettre  in message :
    if lettre in "6":
     print("x")
    else:
        print(lettre)
        print("\n")

# -------------------------------instruction break et continue--------------------


for increment in range(12):
    if increment==7:   # On affiche tout sauf le 7.
       continue
    print(increment)

for increment in range(12):
    if increment==7:  #  On arrête la boucle lorsque increment vaut 7
        break
    print(increment)

#-----------------------------------------------------------------------------------