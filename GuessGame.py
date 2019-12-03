import random
pcchoise = int(random.randint(1, 10))
gamemode = 1
while gamemode == 1:
    guess = int(input("1-10?: "))
    if guess < pcchoise:
        print("Större!")
    elif guess > pcchoise:
        print("Lägre!")
    elif pcchoise == guess:
        print("Rätt! Spela igen!")
        pcchoise = int(random.randint(1, 10))