"""
Formatacao de strings
Em Python, existem várias maneiras de formatar strings para incluir variáveis e expressões. 
As principais formas são:  f-strings (a partir do Python 3.6), o método str.format() e a formatação com o operador %.

1. f-strings: Permitem incluir expressões dentro de strings prefixadas com 'f'. Exemplo:
nome = "João"
idade = 30
print(f"{nome} tem {idade} anos.")
"""

nome = 'Seu nome'
altura = 1.75
peso = 70

"""
Baseado nos valores acima, calcule o IMC e mostre na tela.

Saída esperada:
Antonio Junior tem 1.75 de altura e pesa 70 kg.
Seu IMC é de 22.86

Use as três formas de formatação de strings para exibir a saída.
"""

"""
Formatar casas decimais com f-strings:
Para formatar números com um número específico de casas decimais usando f-strings, você pode usar a sintaxe {:.nf}, onde n é o número de casas decimais desejadas.
Exemplo:
valor = 3.14159
print(f"Valor formatado: {valor:.2f}")  # Saída: Valor formatado: 3.14
imc = peso / (altura * altura)
print(f"Seu IMC é de {imc:.2f}")
"""
