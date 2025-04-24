# Conseguimos adicionar elementos novos em um set, 
# mas não podemos adicionar elementos repetidos e não podemos alterar os elementos que já existem.
# Para adicionar elementos novos, utilizamos o método add()

jogadores_futebol = {'Neymar', 'Cristiano Ronaldo', 'Messi'}
print(jogadores_futebol) # {'Cristiano Ronaldo', 'Neymar', 'Messi'}

# Verificando o tipo do objeto
print(type(jogadores_futebol))

nome = "Bruno"

# Transformar string em set

nome_set = set(nome)

# O set mostra os valores embaralhados, mas não repetidos
print(nome_set)

# Ajuntar dois conjuntos

jogadores_real_madrid = {"Rodrygo", "Vinicius Junior"}
jogadores_brasil = {"Neymar", "Rodrygo"}
print(jogadores_real_madrid | jogadores_brasil) # {'Rodrygo', 'Vinicius Junior', 'Neymar'}

# Ou combinar com o método union()

print(jogadores_real_madrid.union(jogadores_brasil)) # {'Rodrygo', 'Vinicius Junior', 'Neymar'}

# Interseção de conjuntos

print(jogadores_real_madrid & jogadores_brasil)

print(jogadores_real_madrid.intersection(jogadores_brasil))

# Mostrar elementos que não aparecem em ambos os conjuntos

print(jogadores_real_madrid.symmetric_difference(jogadores_brasil))

# Adicionar elementos em um set
jogadores_brasil.add("Ronaldinho Gaúcho")
print(jogadores_brasil)

jogadores_brasil.add("Vinicius Junior")
print(jogadores_brasil)

# Remover elementos de um set
jogadores_brasil.remove("Ronaldinho Gaúcho")
print(jogadores_brasil)

# Remover um dos elementos no set aleatoriamente
jogadores_brasil.pop()
print(jogadores_brasil)

# Limpar o set
jogadores_brasil.clear()
print(jogadores_brasil)
