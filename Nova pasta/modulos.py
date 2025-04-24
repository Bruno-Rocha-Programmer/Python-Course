from math import sqrt
import random

print(sqrt(16))

for i in range(5):
    print(random.randint(1, 50))


#Gerar numeros aleatórios de float entre 0 e 10

#Primeira forma de gerar numeros aleatórios de float entre 0 e 10
print(random.uniform(0, 10))

#Segunda forma de gerar numeros aleatórios de float entre 0 e 10
print(random.random() * 10)

#Gerar numeros aleatórios de float entre 0 e 10 com 2 casas decimais  
print(round(random.uniform(0, 10), 2))

#Escolhendo o número aleatório de uma lista
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numero_escolhido = random.choice(lista)

adivinhar_numero = int(input("Adivinhe o número escolhido entre 1 e 10: "))

if adivinhar_numero == numero_escolhido:
    print("Parabéns! Você acertou o número escolhido.")
else:
    print(f"Você errou! O número escolhido era {numero_escolhido}.")


#Escolher uma amostra aleatória de uma lista
amostra = random.sample(lista, 3)

print(f"Amostra aleatória: {amostra}")

#Embaralhar uma lista

print(f"Lista original: {lista}")

random.shuffle(lista)
print(f"Lista embaralhada: {lista}")
print(lista)