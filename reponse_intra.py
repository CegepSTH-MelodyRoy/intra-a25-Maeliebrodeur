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
#def question2():
#    heure = 0
population_initiale=float(input("Entrez la population initiale de bactéries:"))
#def question2():
def question2():
    for heure in range(1,11):
        population_1= population_initiale * (np.exp(np.pi/1.5))
        population_2=population_1*(np.exp(np.pi/1.5))
        population_3 = population_2 * (np.exp(np.pi / 1.5))
        population_4 = population_3 * (np.exp(np.pi / 1.5))
        population_5 = population_4 * (np.exp(np.pi / 1.5))
        population_6 = population_5 * (np.exp(np.pi / 1.5))
        population_7 = population_6 * (np.exp(np.pi / 1.5))
        population_8 = population_7 * (np.exp(np.pi / 1.5))
        population_9 = population_8 * (np.exp(np.pi / 1.5))
        population_10 = population_9 * (np.exp(np.pi / 1.5))
#        population={population_1,population_2,population_3}
#        population_initiale=population
        print(heure,population_1,population_6)
        plt.plot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                 [100, population_1, population_2, population_3, population_4, population_5, population_6, population_7,
                  population_8, population_9, population_10], "*b")
question2()
# a) demande population initiale de bacteries (input)
# b) pendant 10h calcule population a chaque heure(compteur=0)
# augmentation population= np.pi / 1.5 a chaque heure

# c)
plt.xlabel("Heure")
plt.ylabel("Population")
plt.title("Croissance bactérienne")
#plt.plot([0,1,2,3,4,5,6,7,8,9,10],[100,population_1,population_2 ,population_3, population_4, population_5, population_6,population_7,population_8,population_9,population_10],"*b")
plt.plot([0,10],[50000,50000],"r--")
plt.grid()
plt.show()