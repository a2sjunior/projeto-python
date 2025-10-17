"""
if aninhados (if dentro de ifs)
Explicação: if aninhados são estruturas condicionais dentro de outras estruturas condicionais. 
Muitas vezes, precisamos fazer verificações mais detalhadas, e para isso, podemos usar ifs dentro de ifs.
Exemplo: Um programa que recebe tres números e mostra qual é o maior.
"""

n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))
n3 = int(input('Informe o terceiro número: '))
maior = 0

if (n1 > n2):
    if (n1 > n3):
        maior = n1
    else:
        maior = n3
else:
    if (n2 > n3):
        maior = n2
    else:
        maior = n3

print(f'O maior número é {maior}')

"""
Exercícios

1. Crie um programa que ler um número e imprime se ele é positivo, negativo ou nulo.

2. Crie um programa que ler três números e imprime-os em ordem crescente.

3. Crie um programa que ler três números e imprime-os em ordem decrescente.

4. Crie um programa que ler cinco números inteiros diferentes e imprime o maior e o menor deles.
"""


# # Recebe os três números do usuário
# num1 = float(input("Digite o primeiro número: "))
# num2 = float(input("Digite o segundo número: "))
# num3 = float(input("Digite o terceiro número: "))

# print("Os números em ordem crescente são: ", end="")

# # Lógica para encontrar o menor, o do meio e o maior número
# if num1 <= num2 and num1 <= num3:
#     # num1 é o menor
#     if num2 <= num3:
#         print(num1, num2, num3)
#     else:
#         print(num1, num3, num2)
# elif num2 <= num1 and num2 <= num3:
#     # num2 é o menor
#     if num1 <= num3:
#         print(num2, num1, num3)
#     else:
#         print(num2, num3, num1)
# else:
#     # num3 é o menor
#     if num1 <= num2:
#         print(num3, num1, num2)
#     else:
#         print(num3, num2, num1)

# num1 = int(input("Digite o 1º número: "))
# num2 = int(input("Digite o 2º número: "))
# num3 = int(input("Digite o 3º número: "))
# num4 = int(input("Digite o 4º número: "))
# num5 = int(input("Digite o 5º número: "))
# maior = 0
# menor = 0

# if (num1 == num2 or num1 == num3 or num1 == num4 or num1 == num5 or
#         num2 == num3 or num2 == num4 or num2 == num5 or
#         num3 == num4 or num3 == num5 or
#         num4 == num5):
#     print("Números iguais não são permitidos.")
# else:
#     if num1 > num2:
#         maior = num1
#         menor = num2
#     else:
#         maior = num2
#         menor = num1
#     if(num3 > maior):
#         maior = num3
#     elif(num3 < menor):
#         menor = num3
#     if(num4 > maior):
#         maior = num4
#     elif(num4 < menor):
#         menor = num4
#     if(num5 > maior):
#         maior = num5
#     elif(num5 < menor):
#         menor = num5
    
#     print(f'O maior número é {maior}')
#     print(f'O menor número é {menor}')
