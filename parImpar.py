import imp

parOImpar = input('INtroduce un numero ')
par = 'El numero que has introducido es par '
impar = 'El numero que has introducido es impar '
parOImpar = int(parOImpar)
def check (num):
    if num % 2  == 0:
        print(par)
    else:
        print(impar)

check(parOImpar)
for i in range(5):
    print('hola')
