# Variavel global

global variavel_global
variavel_global = "Curso de Python"

def escopo():
    # Variavel local
    global variavel_global
    variavel_local = "Curso de Python - Variavel Local"
    print(variavel_local)
    print(variavel_global)
    variavel_global = "Curso de Python - Variavel Global"

escopo()
print(variavel_global)
