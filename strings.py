
import random


def randomNumber(x):
    # Creamos el valor random 
    valorRandom = random.randint(0, x)
    #Pedimos al usuario que introduzca un numero para adivinar 
    guess = 0;
    while guess != valorRandom:
        guess = int(input(f'Introduce un numero entre el 0 y el {x}: '))     
        if guess < valorRandom: 
            print('Estas por debajo del numero')
        elif guess > valorRandom:
            print('Estas por encima del numero')
    print('Acertaste')
        
    
    
randomNumber(20)