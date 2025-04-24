# Tuplas são imutáveis
# Tuplas são definidas com parênteses
# Tuplas podem ser usadas para armazenar diferentes tipos de dados em uma mesma variável

tupla = (3, 5, "Bruno", 5.5, True)

print(tupla)  
print(type(tupla))

# Acessando elementos da tupla
print(tupla[2])

tupla2 = (1, 2, 3, 4, 5)

# Concatenando tuplas
tupla3 = tupla + tupla2
print(tupla3)

# Achando o valor máximo e mínimo
print(f"Valor máximo da tupla2 é {max(tupla2)}") 

print(f"Valor mínimo da tupla2 é {min(tupla2)}")

# Contando o número de vezes que um elemento aparece na tupla
print(f"O número 5 aparece {tupla3.count(5)} vezes na tupla")

# Fazendo slice na tupla

print(tupla3[:2])

# Verificando se um elemento está na tupla
print(5 in tupla3)

# Operações não disponíveis para tuplas, sort(), append(), remove(), insert(), pop(), clear()
# Tuplas não suportam operações de modificação, como adicionar ou remover elementos

# Transformar tupla em lista
lista = list(tupla3)
print(lista)

nome = "Bruno"
nome_imutavel = tuple(nome)
letra = ""
resultado_nome = ""
index = 0
chances = 3

for letra in nome_imutavel:
  resultado_nome += "x"

while resultado_nome != nome:
  if chances == 0:
    resultado_nome = input("Digite o nome correto:  ")
    break
  letra = input("Digite uma letra: ")

  if(index < len(nome) and chances > 0 and letra == nome):
    print("Por favor, digite apenas uma letra")
  elif letra in nome_imutavel:
    for i, letter in enumerate(nome_imutavel):
      if letra == letter:
        resultado_nome = "".join([resultado_nome[:i], letra, resultado_nome[i+1:]]) # Usando o join para concatenar as strings
        print(resultado_nome)
  chances -= 1

if resultado_nome == nome:
  print("Você acertou o nome!")
else:
  print("Você não acertou o nome!")
  print(f"O nome correto é {nome}")


# Ordenar valores na tupla
print(sorted(tupla2)) # Retorna uma lista ordenada, não altera a tupla original





