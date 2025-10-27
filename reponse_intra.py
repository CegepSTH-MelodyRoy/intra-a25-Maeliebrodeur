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