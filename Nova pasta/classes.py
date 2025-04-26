class Veiculo:
  def __init__(self, marca, modelo):
    self.__marca = marca
    self.__modelo = modelo
  
  def movimentar(self):
    print("Estou em movimento")
  
  def get_marca(self):
    return self.__marca
  
  def get_modelo(self):
    return self.__modelo
  

class Carro(Veiculo):
  def movimentar(self):
    print("Sou um carro em movimento")
  def __init__(self, marca, modelo, cor):
    self.__cor = cor
    super().__init__(marca, modelo)




carro1 = Carro("Fiat", "Uno", "Branco")

marca = carro1.get_marca()
modelo = carro1.get_modelo()

marca = "Volkswagen"
modelo = "Fusca"

print(carro1.get_marca())
print(marca)

print(carro1.get_modelo())
print(modelo)