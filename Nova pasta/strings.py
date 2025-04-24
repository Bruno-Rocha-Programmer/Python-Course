frase = "Vamos aprender Python hoje!"
palavras = frase.split()

for palavra in palavras:
  print(end=palavra + " ")

# Ache o arroba no email

email = "robert@gmail.com"
pos_arroba = email.find("@")

print("O arroba está na posição:", pos_arroba)

nome = "Bruno"

nome = "".join([nome[:3], "x", nome[3+1:]])

print(nome)

# Slice de elementos

print(f"Pegando apenas o nome do usuário: {email[:pos_arroba]}")

print(f"Pegando apenas o domínio do e-mail: {email[pos_arroba+1:]}")

print(f"Esse email possui arroba?", "@" in email)
print(f"Esse email não possui o nome Bruno?", "Bruno" not in email)

# Tornar maísculo, minisculo e capitalizar
print("Maísculo: " + "bruno RobeRT".upper())

print("Minúsculo: " + "bruno RobeRT".lower())

print("Capitalizado: " + "bruno RobeRt".capitalize())

# Capitalizar cada palavra
print("Capitalizado cada palavra: " + "bruno RobeRt".title())

# Replace valor
nome = "Bruno Robert"
print(f"Substituindo o nome: {nome} por {nome.replace("Robert", "Rocha")}")

#Remover espaços em branco
nome = "   Bruno Robert   "

# Removendo espaços da esquerda
print(f"Removendo os espaços da esquerda: {nome.lstrip()}")

# Removendo espaços da esquerda
print(f"Removendo os espaços da direita: {nome.rstrip()}")

# Removendo espaços da esquerda e direita
print(f"Removendo os espaços da esquerda e direita: {nome.strip()}")

# Alinhar a direita e esquerda
print(f"Alinhar a direita:", "Bruno Robert", "Programador".rjust(20))

# Alinhar no centro
print("Programador Python".center(50, "-"))

"""
Docstring é um tipo de comentário que pode ser utilizado para documentar funções, classes e módulos.
"""