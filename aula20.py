"""
Operadores lógicos
OP      Significado         Exemplo (True)
and     e                   True and True
or      ou                  True or False
not     não                 not True

and - Retorna True se todas as condições forem Verdadeiras
or - Retorna True se uma das condições for Verdadeira
not - Inverte o resultado, ou seja, se for True vira False e vice-versa

and
Se qualquer valor for considerado False, a expressão inteira será avaliada naquele valor.
São considerados falsy: None, False, 0, 0.0, '', [], (), {}

*falsy - significa falso, ou seja, não tem valor

None - significa nada, vazio, sem valor
[] - lista vazia
() - tupla vazia
{} - dicionário vazio
"""

entrada = input('[E]ntrar ou [S]air: ')
senha_digitada = input('Senha: ')
senha_permitida = '123456'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrou')
else:
    print('Saiu')

"""
Avaliação de curto circuito
É quando o Python para de avaliar uma expressão lógica, assim que ele sabe o resultado final dela.
Exemplos:  
True and False and True and True  -> False
True and 1 and 'a' -> 'a' retorna o último valor avaliado, já que todos são verdadeiros
True and 0 and False  -> 0 retorna o primeiro valor avaliado como falso, no caso 0
False and True and True  -> False
True and '' and True  -> '' retorna o primeiro valor avaliado como falso, no caso ''
"""

"""
Exercícios:
1. Crie um programa que ler um número e informa se ele é divisível por 3 e por 7.

2. Crie um programa que ler três números e imprime se eles podem ser os lados de um triângulo.


"""