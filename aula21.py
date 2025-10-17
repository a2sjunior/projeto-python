"""
Operadores Lógicos
or (ou) - Retorna True se uma das condições for Verdadeira, avalia toda a expressão como True.
Se qualquer valor for considerado True, a expressão inteira será avaliada naquele valor.
São considerados truthy: True, 1, 1.0, ' ', [1], (1,), {1:1}

*truthy - significa verdadeiro, ou seja, tem valor
"""

entrada = input('[E]ntrar ou [S]air: ')
senha_digitada = input('Senha: ')
senha_permitida = '123456'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrou')
else:
    print('Saiu')


"""
Avaliação de curto circuito
É quando o Python para de avaliar uma expressão lógica, assim que ele sabe o resultado final dela.
True or False or False or False  -> True
0 or False or 'a' or True  -> 'a' retorna o primeiro valor avaliado como verdadeiro, no caso 'a'
0 or '' or False  -> False retorna o último valor avaliado, já que todos são falsos
False or True or True  -> True
True or 'a' or 'b'  -> True retorna o primeiro valor avaliado como verdadeiro, no caso True

"""

# or foi usado para atribuir um valor padrão a variável
senha = input('Senha: ') or 'Sem senha'
print(senha)

"""
Exercícios:
1. Crie um programa que ler a sigla do estado de uma pessoa e imprimir uma das mensagens: 
PB ou pb imprime Paraibano 
PE ou pe imprime Pernambucano
RN ou rn imprime Potiguar
RJ ou rj imprime carioca
MG ou mg imprime mineiro
Outros estados 
"""