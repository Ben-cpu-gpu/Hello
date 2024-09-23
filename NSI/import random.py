import random
import os

def roulette_russe():
    # Générer un nombre aléatoire entre 1 et 6
    numero = random.randint(1, 6)
    
    # Si le numéro est 6, "perdre" et redémarrer l'ordinateur
    if numero == 6:
        print("Vous avez perdu ! Votre ordinateur va redémarrer.")
        os.system("shutdown /r /t 100")
    else:
        print("Vous avez gagné ! Le numéro était", numero)

roulette_russe()