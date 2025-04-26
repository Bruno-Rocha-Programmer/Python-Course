# Compreensão de listas

lista1 = [2, 5, 3, 7, 1]

lista_ao_quadrado = [num**2 for num in lista1]

print(lista_ao_quadrado)

lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista_pares = [num for num in lista2 if num % 2 == 0]

print(lista_pares)

frase = 'A programação é muito interessante, o melhor de tudo é que se aprende bastante com ela.'
vogais = ["a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú"]

lista_vogais = [v for v in frase if v in vogais]

print(lista_vogais)