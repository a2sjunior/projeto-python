"""
Precedência de operadores
A precedência de operadores define a ordem em que as operações são realizadas em uma expressão. 
A ordem de precedência dos operadores em Python, do mais alto para o mais baixo, é a seguinte:
1. Parênteses: ()
2. Exponenciação: **
3. Multiplicação, Divisão, Divisão Inteira e Resto da Divisão: *, /, //, %
4. Adição e Subtração: +, - -
Operadores com a mesma precedência são avaliados da esquerda para a direita.
"""

resultado1 = 10 + 5 * 2
print('Resultado 1:', resultado1)

resultado2 = (10 + 5) * 2
print('Resultado 2:', resultado2)

resultado3 = 10 + 5 * 2 ** 2
print('Resultado 3:', resultado3)

resultado4 = (1 + int(0.5 + 0.5)) ** (5 + 5)
print('Resultado 4:', resultado4)

media = (8 + 9 + 7) / 3
print('Média:', media)
