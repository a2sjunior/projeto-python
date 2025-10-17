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
Para mostrar o separador de milhares, use {:,.2f}. Este formato usa vírgula como separador de milhares e ponto como separador decimal, seguindo o padrão americano. Para formatar numeros em ponto flutuante no padrão brasileiro o Python bibliotecas que serão vistas mais a frente.

Exemplo:
valor = 3.14159
print(f"Valor formatado: {valor:.2f}")  # Saída: Valor formatado: 3.14
imc = peso / (altura * altura)
print(f"Seu IMC é de {imc:.2f}")

numero_grande = 1234567.89
print(f"Número formatado com separador de milhares: {numero_grande:,.2f}")  # Saída: Número formatado com separador de milhares: 1,234,567.89
"""

"""
F-strings podm ser usadas para alinhar texto e números em colunas.
Caracteres de alinhamento:
< : Alinha à esquerda
> : Alinha à direita
^ : Centraliza
Exemplo:
nome = "Ana"
print(f"{nome:<10} é um nome.")  # Alinha à esquerda em um campo de 10 caracteres
print(f"{nome:>10} é um nome.")  # Alinha à direita em um campo de 10 caracteres
print(f"{nome:^10} é um nome.")  # Centraliza em um campo de 10 caracteres  

Sinal de + e - para números:
Você pode usar o sinal de + para sempre mostrar o sinal de um número, e o sinal de - para mostrar apenas números negativos.
Exemplo:
numero = 5
print(f"Número com sinal: {numero:+d}")  # Saída: Número com sinal: +5
numero_negativo = -3
print(f"Número negativo: {numero_negativo:-d}")  # Saída: Número negativo: -3

Use qualquer simbolo para preencher o espaço vazio:
Exemplo:
numero = 42
print(f"Número preenchido com zeros: {numero:0>5d}")  # Saída: Número preenchido com zeros: 00042
print(f"Número preenchido com asteriscos: {numero:*^8d}")  # Saída: Número preenchido com asteriscos: ***42***

Exemplo de prenchimento com str: 
texto = "Hi"
print(f"Texto preenchido com hífens: {texto:-<10}")  # Saída: Texto preenchido com hífens: Hi--------
print(f"Texto preenchido com pontos: {texto:.^10}")  # Saída: Texto preenchido com pontos: ....Hi....
print(f"Texto preenchido com espaços: {texto: >10}")  # Saída: Texto preenchido com espaços:         Hi

print(f"{"JUNIOR":*^20}")  # Saída: **********JUNIOR**********
print(f"{12345:0>10d}")    # Saída: 0000012345
print(f"{3.14159:.3f}")    # Saída: 3.142
print(f"{-42:+d}")         # Saída: -42
print(f"{42:+d}")          # Saída: +42

"""

"""
Convertion flags em f-strings:
Definidas após o nome da variável, as flags de conversão forçam a conversão do valor antes da formatação.

!s : Converte o valor em string usando str()
!r : Converte o valor em string usando repr()
!a : Converte o valor em string usando ascii()

str(): Converte o valor em uma string legível.
repr(): Retorna uma representação oficial da string, útil para depuração, mostrando caracteres especiais.
ascii(): Retorna uma representação da string com caracteres não ASCII escapados.

Exemplo:

valor = "Olá\nMundo"
print(f"Usando !s: {valor!s}")  # Saída: Usando !s: Olá
                                                    Mundo
print(f"Usando !r: {valor!r}")  # Saída: Usando !r: 'Olá\nMundo'
print(f"Usando !a: {valor!a}")  # Saída: Usando !a: 'Ol\xE1\nMundo'

"""