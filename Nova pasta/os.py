import os

# getcwd() retorna o caminho do diretório atual
print(os.getcwd())

# mkdir() cria um diretório

pasta_nova = "teste"
pasta_pai = "C:\\"
diretorio_completo = os.path.join(pasta_pai, pasta_nova)
os.mkdir(diretorio_completo)

# rmdir() remove um diretório
os.rmdir(diretorio_completo)

# listdir() retorna uma lista com os arquivos do diretório
print(os.listdir())

# os.basename() retorna o nome do diretório
print(os.path.basename(os.getcwd()))

# os.dirname() retorna o diretório pai
print(os.path.dirname(os.getcwd()))

# Verificar se um path existe
print(os.path.exists("C:\\"))

# Verificar se é diretório
print(os.path.isdir("C:\\"))

# Verificar se é arquivo
print(os.path.isfile("C:\\"))

# Renomear vários arquivos de uma vez

os.mkdir(diretorio_completo)
