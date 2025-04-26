from math import sqrt
# Lidando com exceções em Python
# Exceções são eventos que ocorrem durante a execução de um programa e interrompem o fluxo normal do código.

numero1 = 5
numero2 = 0

try:
  resultado = numero1 / numero2
except ZeroDivisionError:
  print("Erro: Você não pode dividir por zero.")


try:
  num = int(input("Digite um número: "))

  if num < 0:
    raise ArithmeticError()
  else:
    raiz = sqrt(num)
    print(f"A raiz quadrada de {num} é {raiz}.")
except ArithmeticError:
  print("Erro: Número negativo não permitido.")

