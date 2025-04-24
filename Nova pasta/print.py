
nome = "Bruno"
sobrenome = "Rocha"

print("Programdor -", nome, end="") #end é usado para não pular linha
print("",sobrenome)

idade = 25

print("{0} tem {1} anos".format(nome, idade)) #Usando o format para formatar a string

#Delimitar casas decimais
valor = 10.123456789
print(f"O valor {valor} foi reduzido para {valor:.2f}")

#Caractere de espaço
print(f"{nome} {sobrenome}\t{idade} anos") #\t é usado para dar espaço entre os valores
print(f"Barra \\")