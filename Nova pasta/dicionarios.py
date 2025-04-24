valores = {
  'nome': "Bruno",
  'idade': 25
}
print(valores)

# Verificar quantos elementos existem no dicionário
print(f"O dicionário valores possui {len(valores)} elementos.")

# Adicionar um novo elemento ao dicionário
valores["trabalho"] = "programador"
print(valores)

# Excluir um elemento do dicionário
del valores['idade']

print(valores)

# Apagar todos os elementos do dicionário
valores.clear()

print(valores)

# Apagar o dicionário
del valores

frutas = {
  "vermelha": "maçã",
  "amarelo": "banana",
  "verde": "abacate",
  "roxa": "uva",
  "laranja": "laranja",
}

print(frutas)

# Iterar sobre o dicionário

for cor, fruta in frutas.items():
  print(f"A fruta {fruta} é da cor {cor}.")

print("\n")

# Imprimindo apenas as chaves do dicionário

for cor in frutas.keys():
  print(f"A cor {cor} é uma chave do dicionário.")

print("\n")
# Imprimindo apenas os valores do dicionário

for fruta in frutas.values():
  print(f"A fruta {fruta} é um valor do dicionário.")

