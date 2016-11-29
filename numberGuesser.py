"""Simple Guess The Number Application"""
import random

def main():
    print ("Em que número estou 'pensando'?! (1..100)")

    randomNumber = random.randint(1,100)
    found = False
    guesses = 0
    
    while not found:
        guesses+=1
        try:
            userGuess = int(input("Tentativa {}: ".format(guesses)))
            if userGuess == randomNumber:
                print ("Acertou em {} tentativas! \o/".format(guesses))
                found = True
            elif userGuess < randomNumber:
                print ("Mais!")
            else:
                print ("Menos!")
        except:
            print("Informe um número válido.")

main()
