#Listas no python
#Concatenar listas

#Concatenar listas com o operador de adição
lista1 = [2, 5, 3, 7, 1]
lista2 = [4, 6, 8, 9, 0]
lista3 = lista1 + lista2
print(lista3) # [2, 5, 3, 7, 1, 4, 6, 8, 9, 0]

#Acessando o último elemento da lista
print(lista3[-1])

#Tirando os primeiros elementos da lista
print(lista3[:2])

#Retirando um elemento da lista apartir de um elemento
print(lista3[3:4])

#Imprimindo a lista ao contrário
print(lista3[::-1])

#Imprimindo a lista de forma ordenada
print(sorted(lista3))

#Imprimindo a lista de forma ordenada ao contrário
print(sorted(lista3, reverse=True))

#Somando os elementos da lista
print(sum(lista3))

#Achando o valor minimo da lista
print(min(lista3))

#Achando o valor máximo da lista
print(max(lista3))

#Adicionando um elemento a lista
lista3.append(5)
print(lista3) # [2, 5, 3, 7, 1, 4, 6, 8, 9, 0, 5]

#Tirando o último elemento da lista
lista3.pop()
print(lista3) # [2, 5, 3, 7, 1, 4, 6, 8, 9, 0]

#Retirando um elemento em um determinado indice
print("O elemento {} será removido".format(lista3[3])) # 2
lista3.pop(3)

print(lista3) 


#Adicionando um elemento em uma determinada posição
lista3.insert(3, 7)
print(lista3) 

#Verificando se um elemento está na lista
print(f"O elemento 7 está na lista? {7 in lista3}")

#Exercicio 1
#Crie um script que peça ao usuário para digitar 5 das bebidas favoritas dele e armazene em uma lista. 
# Depois, imprima a lista na tela de forma alfabetica usando um laço for.

bebidasfavoritas = list()

while len(bebidasfavoritas) < 5:
    bebida = input("Digite uma bebida favorita: ")
    bebidasfavoritas.append(bebida)

for bebida in sorted(bebidasfavoritas):
    print(bebida)
