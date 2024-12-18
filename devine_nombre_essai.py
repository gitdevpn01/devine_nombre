# Importer la librairie random
import random

nb_min = 1
nb_max = 20
#essai = 0
nb_essai = 10

# Afficher la règle du jeu
print("Essaye de deviner le nombre que j'ai choisi entre {} et {} en {} essais. " . format(nb_min,nb_max,nb_essai))
print("=========")

nb_secret = random.randint(nb_min,nb_max)

#while True:
for i in range(nb_essai):
    nb_user = int(input("Entrer votre nombre: "))
    
    #essai += 1

    if nb_secret == nb_user:
        print(f"Bravo ! Tu as deviné le nombre {nb_secret} en {i} essai.")
        break
    elif nb_user < nb_secret:
        print("Trop petit !")
    else: 
        print("Trop grand !")

#print(f"Merci d'avoir joué en {essai} essai !")
print("Merci d'avoir joué !")































