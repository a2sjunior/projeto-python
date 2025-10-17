"""
Fatiamento de strings e formatação em Python
  0 1 2 3 4 5 6 7 8 9 10
  P R O G R A M A C A O 
-11 10 9 8 7 6 5 4 3 2 1 

Fatiamento [i:f:p] onde:
i = índice inicial (inclusivo), caso não seja especificado, o padrão é 0.
f = índice final (exclusivo), ou seja, o caractere no índice f não é incluído, caso não seja especificado, o padrão é o tamanho da string.
p = passo (opcional, padrão é 1)

Exemplos:
texto = "PROGRAMAÇÃO"
print(texto[0:5])    # Saída: PROGR
print(texto[5:])     # Saída: AMAÇÃO
print(texto[:5])     # Saída: PROGR
print(texto[-5:])    # Saída: MAÇÃO
print(texto[::2])    # Saída: PORMO
print(texto[::-1])   # Saída: OÃMACARGORP
print(texto[-8:-3:]) # Saída: GRAM
"""

"""
Função len(): Retorna o comprimento (número de caracteres) de uma string.
Exemplo:
texto = "PROGRAMAÇÃO"
print(len(texto))  # Saída: 11
"""

"""
Exercícios
Crie um programa que leia o nome e a idade de uma pessoa e exiba as seguintes informações
Seu nome é {nome}
Seu nome invertido é {nome invertido}
Seu nome contém espaços ou Seu nome não contém espaços
Seu nome tem {n} caracteres
A primeira letra do seu nome é {primeira letra}
A última letra do seu nome é {última letra}

Se nada for informado em nome ou idade exiba uma mensagem dizendo que os dados são obrigatórios e finalize o programa.
"""

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

if nome and idade:
    print(f"Seu nome é {nome}")
    print(f"Seu nome invertido é {nome[::-1]}")

    if ' ' in nome:
        print("Seu nome contém espaços")
    else:
        print("Seu nome não contém espaços")

    print(f"Seu nome tem {len(nome)} caracteres")
    print(f"A primeira letra do seu nome é {nome[0]}")
    print(f"A última letra do seu nome é {nome[-1]}")
else:
    print("Dados obrigatórios!")