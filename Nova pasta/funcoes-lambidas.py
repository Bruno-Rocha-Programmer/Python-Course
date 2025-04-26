greetings = lambda text: f"Hello, {text}!"

print(greetings("Bruno"))

# Multiplicar todos os números de uma lista por 2
numeros = [2, 5, 7, 10, 20]

multiplicar = map(lambda valor: valor * 2, numeros)

print(list(multiplicar))

palavras = ["Python", "é", "uma", "linguagem", "de", "programação"]

# Função map

to_upper = map(lambda palavra: palavra.upper(), palavras)

print(list(to_upper))

def multiplica_por_dois(valor, quantidade=2):
  return valor * quantidade


numeros = [2, 5, 7, 10, 20]

multiplicar = list(map(lambda valor: multiplica_por_dois(valor, 10), numeros))

print(multiplicar)

# Função filter

def numeros_pares(valor):
  return valor % 2 == 0

numeros = [2, 5, 7, 10, 20]

pares = list(filter(numeros_pares, numeros))

print(pares)


# Função reduce

from functools import reduce

numeros = [2, 5, 7, 10, 20]

soma = reduce(lambda acc, valor: acc + valor, numeros)

print(soma)