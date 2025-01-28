import random

numero_secreto=random.randint(0,100)
intento=int(input("Adivina el numero entre 1 al 100"))

while intento != numero_secreto:
    if intento 