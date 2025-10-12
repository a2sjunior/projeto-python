"""
Conversão de tipos (coercionamento)
Chamado também de coercion, convertion, type casting.
É o processo de transformar um valor de um tipo em outro.
tipos primitivos e imutáveis: 
int, float, str, bool
Funções de conversão:
int() -> converte para inteiro
float() -> converte para ponto flutuante
str() -> converte para string
bool() -> converte para booleano
"""
print(1 + 2)       # 3
print('a' + 'b')   # ab
# print(1 + '2')   # TypeError

# Conversão implícita (coercion)
print(1 + 2.5)     # 3.5
print(type(1 + 2.5)) # <class 'float'>
print(1 + True)    # 2
print(type(1 + True)) # <class 'int'>
print(1 + False)   # 1
print(type(1 + False)) # <class 'int'>  

# Conversão explícita (casting)
print(int(2.8))    # 2
print(float(2))    # 2.0
print(str(2))      # '2'
print(str(2) + '3') # '23'
print(int('2') + 3) # 5
print(float('2.5') + 3) # 5.5
print(int(True))   # 1
print(int(False))  # 0

# Conversão para booleano
print(bool(1))     # True
print(bool(0))     # False
print(bool(-1))    # True
print(bool(0.1))   # True
print(bool(''))    # False
print(bool(' '))   # True
print(bool('False')) # True