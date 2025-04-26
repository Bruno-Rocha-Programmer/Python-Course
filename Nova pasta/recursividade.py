numero = int(input("Digite um número inteiro positivo: "))

def fatorial(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * fatorial(n - 1)

try:
  resultado = fatorial(numero)
except RecursionError:
  print("Erro: O número é muito grande ou negativo. Tente um número menor e positivo.")
else:
  print(f"O fatorial de {numero} é {resultado}.")