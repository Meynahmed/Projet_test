# Exemple 1 :Ecriture dans un fichier
# Première méthode
file = open("eleves.txt", "w+")
file.write("Sophie M\n")
file.write("Amina C\n")
file.write("Azeddine A\n")
file.close()

# Deuxième méthode
eleve_liste = ["Sophie", "Amina", "Azeddine"]
with open("eleves.txt", "a+") as file:
    for student in eleve_liste:
        file.write(student + "\n")
    file.close()


# Exercice 1
# Créer un nouveau fichier text en écriture et le remplir
# d'articles avec les deux méthodes précedentes.
# Première méthode
file = open("articles.txt", "w+")
file.write("huile de colza\n")
file.write("huile de tournesol\n")
file.write("huile d'olive\n")
file.write("huile d'arachide\n")
file.close()

# Deuxième méthode
articles_liste = ["huile de colza", "huile de tournesol", "huile d'olive", "huile d'archide"]
with open("articles.txt", "a+") as file:
    for article in articles_liste:
        file.write(article + "\n")
    file.close()


# lecture dans un fichier
# Exemple 1
with open("Menus.txt", "r+") as file:
    print(file.readlines())
    file.close()

# Exemple 2
import os
import random
if os.path.exists("Menus.txt"):
    with open("Menus.txt", "r+") as file:
        menus_list = file.readlines()
        choix_menu_random = random.choice(menus_list)
        print(" On peut vous proposer aujourd'hui le menu suivant :", choix_menu_random)
        file.close()
else:
    print("Le document n'existe pas ")


# Exercice 2
# Jeu : créer un fichier text le remplir avec des chiffres de 1 à 20
# le parcourir aléatoirement et si vous tomber sur 10 vous avez gagné

import os
import random
if os.path.exists("nombres.txt"):
    with open("nombres.txt", "r+") as file:
        nombre_list = file.readlines()
        nb_random = random.choice(nombre_list)
        print(" Le nombre choisi est :", nb_random)
        if nb_random == 6:
            print(" Vous avez gagné !")
        else:
            print(" Vous avez perdu !")
        file.close()

else:
    print("Le document n'existe pas ")

#Exercices 3
# programme jeu de 10 tirages avec 2 et 9 gagnants
for i in range (1, 3):
    nb = int(input(" Entrer un nombre : "))
    if nb == 2 or nb ==9:
        print(" Vous avez gagné ")
    else:
        print(" Vous avez perdu ")
    i = i + 1


# Exemple de transfert de fichiers


# deplacement d'un fichier dans un autre dossier
# suppression de celui-ci
# deplacement de l'image logo.png
"""
import os
import shutil

source ="logo.png"
target = "Images/logo.png"

shutil.copy(source, target)
os.remove(source)
import os
import shutil


#deplacement de l'image R.png
source ="R.png"
target = "Images/R.png"

shutil.copy(source, target)
os.remove(source)


"""
# Résolution équation 2d degré
for i in range (1, 6):
    a = float( input(" Entrez la valeur de a : "))
    b = float( input(" Entrez la valeur de b : "))
    c = float( input(" Entrez la valeur de c : "))
    delta = pow(b, 2) - 4*a*c
    if delta > 0 :
      print (" On a deux solutions :", "x1", "=", (-b-pow(delta, 0.5))/(2*a), " et", "x2", "=", (-b+pow(delta, 0.5))/(2*a))
    elif delta == 0:
      print (" On a une solution :", "x0", "=", (-b)/(2*a))
    else :
      print(" Pas de solution ")
    i = i + 1

