idade = 0


while idade < 18:
    nome = input("Qual o seu nome? ")
    idade = int(input("Qual a sua idade? "))

    if idade < 18:
      print("Você é menor de idade. Por isso, não pode entrar.")

print(f"Bem vindo a festa {nome}")
