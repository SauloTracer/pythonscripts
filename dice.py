import random

def roll(qtd, size=6):
    for i in range(qtd):
        print("Dice {} rolls {}.".format(i+1,random.randrange(1,size+1)))
    
