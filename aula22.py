"""
Operador not
O operador not é uma negação, ou seja, ele inverte o valor booleano de uma expressão.
Exemplo:
not True -> False
not False -> True
"""

nome = input('Qual o seu nome? ')

if not nome:  # Se o nome for vazio, ou seja, False
    print('Você não informou o nome')

# print(not False)  # True
# print(not True)   # False
# print(not 0)     # True
# print(not 1)     # False
# print(not None)  # True
# print(not ' ')   # False
# print(not '')    # True