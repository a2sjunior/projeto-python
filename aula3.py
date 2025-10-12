"""
Tipo de tipagem em Python
- Dinâmica: não precisa declarar o tipo da variável
- Forte: não permite operações entre tipos diferentes
str = string (texto)
"""
print("Olá, Mundo!") # aspas duplas
print('Olá, Mundo!') # aspas simples
print('''Olá, Mundo!''') # aspas triplas
print("""Olá, Mundo!""") # aspas triplas

# A função type mostra o tipo da variável
print(type("Olá, Mundo!")) 

# Escape characters
print("Olá,\nMundo!") # quebra de linha
print("Olá,\tMundo!") # tabulação
print("Olá, \"Mundo\"!") # aspas duplas dentro de aspas duplas
print('Olá, \'Mundo\'!') # aspas simples dentro de aspas

# r de raw (crua)
print(r"Olá,\nMundo!") # não interpreta o \n

# Aspas simples dentro de aspas duplas
print("Olá, 'Mundo'!")
# Aspas duplas dentro de aspas simples
print('Olá, "Mundo"!')