"""
Formatacao de strings
Em Python, existem várias maneiras de formatar strings para incluir variáveis e expressões.

str.format(): Usa chaves {} como marcadores de posição que são substituídos pelos valores passados ao método format(). Exemplo:
print("{} tem {} anos.".format(nome, idade))

Interpolação básica com %
Operador %: Usa especificadores de formato dentro da string. Exemplo:
print("%s tem %d anos." % (nome, idade))

Operador %:
%s - string
%d ou %i - inteiro
%f - ponto flutuante
%.2f - ponto flutuante com 2 casas decimais %
%x e %X - hexadecimal (minúsculo e maiúsculo)

print("Hexadecimal: %x" % 255)  # saída: ff
print("Hexadecimal: %08X" % 255)  # saída: 000000FF
print("Hexadecimal: %04x" % 255)  # saída: 00ff
"""

nome = 'Seu nome'
altura = 1.75
peso = 70
imc = peso / (altura * altura)

"""
Baseado nos valores acima, calcule o IMC e mostre na tela.
Saída esperada:
Antonio Junior tem 1.75 de altura e pesa 70 kg.
Seu IMC é de 22.86
Use as três formas de formatação de strings para exibir a saída.
"""

print(f"{nome} tem {altura} de altura e pesa {peso} kg.")
imc = peso / (altura * altura)
print(f"Seu IMC é de {imc:.2f}")

print("{} tem {} de altura e pesa {} kg.".format(nome, altura, peso))
print("Seu IMC é de {:.2f}".format(imc))

print("%s tem %.2f de altura e pesa %d kg." % (nome, altura, peso))
print("Seu IMC é de %.2f" % imc)

a = 'A'
b = 'B'
c = 1.15

print("a={} b={} c={}".format(a, b, c))
print("a={0} b={1} c={2}".format(a, b, c))
print("a={2} b={1} c={0}".format(c, b, a))
print("a={valor1} b={valor2} c={valor3}".format(valor1=a, valor2=b, valor3=c))

