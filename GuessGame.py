import random
import time

pccoise = int(random.randint(1, 10))
gamemode = 1

while gamemode == 1:
    guess = int(input("1-10?: "))
    if guess < pccoise:
        print("Större!")
    
    elif guess > pccoise:
        print("Lägre!")

    elif pccoise == guess:
        print("Rätt!")
        pccoise = int(random.randint(1, 10))

    else:
        gamemode = 0