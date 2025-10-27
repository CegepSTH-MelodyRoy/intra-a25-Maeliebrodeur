##########################################
# Brodeur, Maélie, <6242693>
##########################################
import random
# temperature_ideale entre 24 et 30°C
# a) aleatoirement 10 temperatures entre 20 et 35°C arrodies a 1 decimale (round)
# b) affiche chaque temperature avec so jour (compteur)
# c)
# print("OK") si dans temperature ideale
# print("Trop froid") si inferieure a borne inf de temperature ideale (24)
# print("Trop chaud" si superieure a borne sup de temperature ideale (30)
# quand 10 temperatures affichées print("Fin")

def question1():
    for jour in range(1,11):
#   random.seed(42)
        temperature=random.uniform(20,35)
        print("Jour",jour,":",round(temperature,1),"°C")
        if 24<=temperature<=30:
            print("OK")
        elif temperature < 24:
            print("Trop froid")
        elif temperature > 30:
            print("Trop chaud")

    print("Fin")

question1()
