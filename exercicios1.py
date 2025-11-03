"""
Algorítimos em python

Ler dois números inteiros e imprimi-los.

Ler um número inteiro e imprimir o seu sucessor e antecessor.

Ler nome, endereço e telefone e imprimi-los. 

Ler dois números inteiros e imprimir a soma. Antes do resultado, deverá aparecer
a mensagem: Soma. 

Ler dois números inteiros e imprimir o produto. Antes do resultado, deverá aparecer a mensagem: Produto.

Ler um numero real e imprimir a terça parte deste numero.

Escrever um programa que leia três notas e imprima a média aritmética.

Entrar com dois numeros inteiros e imprimir a seguinte saída:
dividendo
divisor:
quociente:
resto:

Entrar com quatro números e imprimir a média ponderada, sabendo-se que os pesos são respectivamente: 1, 2, 3 e 4. (Dica: média ponderada = (n1*p1 + n2*p2 + n3*p3 + n4*p4) / (p1 + p2 + p3 + p4))

Entrar com um número e imprimir a seguinte saída:
numero:
quadrado:
raiz quadrada: 

Entrar com a base e a altura de um retângulo e imprimir a seguinte saída:
perimetro:
area:

Entrar com o raio de um cfrculo e imprimir a seguinte saída:
perimetro: (dica: perímetro = 2 * π * raio; considere π = 3.14)
area: (dica: área = π * raio^2; considere π = 3.14)

Criar um programa que calcule e imprima a área de um triângulo, deve receber os valores da base e altura. 

Entrar com os valores dos catetos de um triângulo retângulo e imprimira hipotenusa do triângulo. (Dica: hipotenusa = √(cateto1^2 + cateto2^2))

Entrar com a razão de uma PA e o valor do 1 2termo. Calcular imprimiro 10 termo da série. 
(Dica: an = a1 + (n - 1) * r)

Entrar com a razão de uma PG e o valor do 1 2termo. Calcular e imprimir o 5 termo da série. 
(Dica: an = a1 * r^(n - 1))

Ler uma temperatura em graus centígrados e apresentá-la convertida em graus Fahrenheit. A fórmula de conversão é: F = (9 * C + 160) / 5, sendo F a temperatura em Fahrenheit e C a temperatura em centígrados.

Criar um algoritmo que leia o numerador e o denominador de uma fração e transformá-lo em um número decimal. 

Para vários tributos, a base de cálculo é o salário mínimo. Fazer um algoritmo que leia o valor do salário mínimo e o valor do salário de uma pessoa. Calcular e imprimir quantos salários mínimos ela ganha. 

Criar um algoritmo que leia um valor de hora e informe quantos minutos se passaram desde o início do dia. 

Fazer um algoritmo que possa entrar com o saldo de uma aplicação e imprima o
novo saldo, considerando o reajuste de 1%. 

Em épocas de pouco dinheiro, os comerciantes estão procurando aumentar suas
vendas oferecendo desconto. Faça um algoritmo que possa entrar com o valor de
um produto e imprima o novo valor tendo em vista que o desconto foi de 9%. 

Criar um algoritmo que efetue o cálculo do salário líquido de um professor. Os dados fornecidos serão: valor da hora aula, número de aulas dadas no mês e percentual de desconto do INSS. 

Efetuar o cálculo do valor de uma prestação em atraso, utilizando a fórmula:
prestação = valor + (valor*(taxa/100)*tempo). 

Todo restaurante embora por lei não possa obrigar o cliente a pagar, cobra 10%
para o garçom. Fazer um algoritmo que leia o valor gasto com despesas realizadas em um restaurante e imprima o valor total com a gorjeta. 

Escrever um programa que leia um valor em reais e a cotação do dólar, e converta esse valor para dólares.

Antes de o racionamento de energia ser decretado, quase ninguém falava em
quilowatts; mas, agora, todos incorporaram essa palavra em seu vocabulário. Sabendo-se que 100 quilowatts de energia custa um sétimo do salário mínimo,
fazer um algoritmo que receba o valor do salário mínimo e a quantidade de quilowatts gasta por uma residência e calcule. Imprima:
o valor em reais de cada quilowatt
m o valor em reais a ser pago
o novo valor a ser pago por essa residência com um desconto de 10%. 
(Dica: divide por 7 para achar o preço de 100 Kw e por 100 para achar de 1 Kw)

Escrever um programa que recebe um numero inteiro de 3 casas e imprime o algarismo da casa das dezenas. (Dica : use operadores de divisão inteira e módulo)

Entrar com uma data no formato ddmmaa e imprimir: dia, mês e ano separados. (Dica: use operadores de divisão inteira e módulo)

Entrar com um número no formato CDU e imprimir invertido: UDC. (Exemplo:
123, sairá 321.) O número deverá ser armazenado em outra variável antes de ser
impresso.

Ler dois valores para as variáveis A e B, efetuar a troca dos valores de forma que a
variávelA passe a ter o valor da variável B e que a variável B passe a ter o valor da variável A. Apresentar os valores trocados. 

"""

"""
Escrever um programa que recebe um numero inteiro de 3 casas e imprime o algarismo da casa das dezenas. (Dica : use operadores de divisão inteira e módulo)

"""

numero = int(input("Digite um número inteiro de 3 casas: "))
dezena = (numero // 10) % 10
print(f"O algarismo da casa das dezenas é: {dezena}")


"""
Entrar com uma data no formato ddmmaa e imprimir: dia, mês e ano separados. (Dica: use operadores de divisão inteira e módulo)
"""

data = int(input("Digite uma data no formato ddmmaa: "))
dia = data // 10000
mes = (data // 100) % 100
ano = data % 100
print(f"Dia: {dia}, Mês: {mes}, Ano: {ano}")

"""
Entrar com um número no formato CDU e imprimir invertido: UDC. (Exemplo:
123, sairá 321.) O número deverá ser armazenado em outra variável antes de ser
impresso.
"""

numero = int(input("Digite um número no formato CDU: "))
unidade = numero % 10
dezena = (numero // 10) % 10
centena = numero // 100 
numero_invertido = unidade * 100 + dezena * 10 + centena
print(f"Número invertido: {numero_invertido}")

