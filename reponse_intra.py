##########################################
# Brodeur, Maélie, <6242693>
##########################################
import random
# Question 1

def question1():
    for jour in range(1,11):
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


# Question 2
import numpy as np
import matplotlib.pyplot as plt
def question2():
#    heure = 0
    population_initiale=float(input("Entrez la population initiale de bactéries:"))
#    for heure in range(0,11):
    population= population_initiale + np.pi/1.5
    return population

# a) demande population initiale de bacteries (input)
# b) pendant 10h calcule population a chaque heure(compteur=0)
# augmentation population= np.pi / 1.5 a chaque heure
question2()
# c)
plt.xlabel("Heure")
plt.ylabel("Population")
plt.title("Croissance bactérienne")
# plt.plot([x],[y],"*b")
plt.plot([0,10],[50000,50000],"r--")
plt.grid()
plt.show()