numero1 = 2
numero2 = 3

print(numero1 + numero2)

def printar_ola(nome):
    print(f"Olá, {nome}!")
  
printar_ola("Bruno")

def multiplicar(numero1, numero2):
    return numero1 * numero2

# Parametros obrigatorios
def print_texto(texto):
    print(texto)

print_texto("Olá, Mundo!")

# Parametros opcionais
def print_dados_da_pessoa(nome, idade=18):
    print(f"Nome: {nome}, Idade: {idade}")

print_dados_da_pessoa("Bruno")