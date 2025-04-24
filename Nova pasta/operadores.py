a = 5
b = 10
c = 15

# Operadores aritméticos

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
potencia = a ** b
divisao_inteira = a // b # É a divisão inteira, que retorna o quociente sem a parte decimal

print("Soma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)
print("Divisão:", divisao)
print("Resto:", resto)
print("Potência:", potencia)
print("Divisão inteira:", divisao_inteira)

# Operadores de comparação

print("\n")
print("Operadores de comparação:")

igual = a == b
diferente = a != b
maior = a > b
menor = a < b
maior_ou_igual = a >= b
menor_ou_igual = a <= b

print("Igual:", igual)
print("Diferente:", diferente)
print("Maior:", maior)
print("Menor:", menor)
print("Maior ou igual:", maior_ou_igual)

# Operadores lógicos

print("\n")
print("Operadores lógicos:")

and_logico = a and b # O operador and retorna o último valor avaliado se ambos forem verdadeiros
or_logico = a or b # O operador or retorna o primeiro valor avaliado que for verdadeiro
not_logico = not a # O operador not inverte o valor lógico

print("And lógico:", and_logico)
print("Or lógico:", or_logico)
print("Not lógico:", not_logico)

idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))

resultado = idade >= 18 and altura >= 1.70
print(resultado == True and "Você pode entrar")
print(resultado == False and "Você não pode entrar") 