"""
Operadores in e not in
in - Retorna True se o valor estiver presente na sequência
not in - Retorna True se o valor não estiver presente na sequência
Srtings (str), listas, tuplas, sets e dicionários são sequências
Iteráveis (iterables) - são sequências que podem ser iteradas, ou seja, percorridas

Strings são iteráveis
0 1 2 3 4 5 -> indices
P Y T H O N
-6-5-4-3-2-1
"""

# linguagem = 'Python'
# print(linguagem[2])  # T
# print(linguagem[-4])  # T
# print(20 * '=')
# print('t' in linguagem)  # True
# print('j' not in linguagem)  # True
# print('thon' in linguagem) 
# print('java' in linguagem ) # False


# palavra = input('Digite uma palavra: ')
# encontrar = input('Digite o que quer encontrar na palavra: ')

# if encontrar in palavra:
#     print(f'Encontrei {encontrar} na palavra {palavra}')
# else:
#     print(f'Não encontrei {encontrar} na palavra {palavra}')

"""
Exercícios:
1. Crie um programa que leia o nome e imprima-o se o primeiro caractere for a letra A (considerar maiúsculo e minúsculo).

2. Crie um programa que receba o nome completo de uma pessoa e verifique se ela tem Silva no nome.

3. A turma de Lógica de programação, por ter muitos alunos, será dividida em dias de provas.
Após um estudo feito pelo coordenador, decidiu-se dividi-la em três grupos.
Fazer um algoritmo que leia o nome do aluno e indicar a sala em que ele deverá
fazer as provas, tendo em vista a tabela a seguir e sabendo-se que todas as salas
se encontram no bloco F:
A - K:sala 101
L-N:sala 102
O - Z:sala 103 
"""


# resposta 1
# nome = input('Digite seu nome: ')
# if nome[0] == 'a' or nome[0] == 'A':
#     print(nome)


# resposta 3
# nome = input('Digite seu nome: ')
# primeira_letra = nome[0].upper()

# if 'A' <= primeira_letra and primeira_letra <= 'K':
#     print(f'{nome}, sua sala é a 101')
# elif 'L' <= primeira_letra <= 'N':
#     print(f'{nome}, sua sala é a 102')
# elif 'O' <= primeira_letra <= 'Z':
#     print(f'{nome}, sua sala é a 103')
# else:
#     print('Nome inválido')
