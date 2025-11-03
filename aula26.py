"""
Estruturas de Repetição em Python
Definição: Estruturas de repetição são usadas para executar um bloco de código várias vezes, com base em uma condição ou um número específico de iterações.
Tipos principais:
1. for: Usado para iterar sobre uma sequência.
2. while: Executa um bloco de código enquanto uma condição for verdadeira.
"""


# Exemplo sem usar for/while: pedindo 3 valores separadamente
n1 = float(input("Digite o 1º número: "))
n2 = float(input("Digite o 2º número: "))
n3 = float(input("Digite o 3º número: "))
soma = n1 + n2 + n3
print(f"Soma (sem repetição): {soma}")


# Exemplo usando estrutura de repetição (for) para somar N valores
total = 0.0
n = int(input("Quantos números você quer somar? "))
for i in range(1, n + 1):
    valor = float(input(f"Digite o {i}º número: "))
    total += valor
    print(f"Soma (com repetição): {total}")


"""
Loop infinito: Um loop que nunca termina, geralmente causado por uma condição que nunca se torna falsa.
Exemplo de loop infinito com while:
while True:
    print("Este loop nunca termina!")

Bloco unreachable: Código que nunca será executado devido à lógica do programa.
Exemplo:
def exemplo_unreachable():
    return
    print("Esta linha nunca será executada.")

Exemplo de loop infinito corrigido:
contador = 0
while contador < 5:
    print(contador)
    contador += 1

Exemplo de bloco unreachable corrigido:
def exemplo_reachable():
    print("Esta linha será executada.")
    return

"""

"""
1. Soma e média até zero
Descrição: Leia números (float) do usuário até que o valor 0 seja digitado. Ao final, mostre a soma, a quantidade de números lidos (excluindo o zero) e a média.
Entradas: sequência de números, termina com 0.
Saída: soma, quantidade, média.
Observação: trate divisão por zero.

2. Validação de senha
Descrição: Solicite que o usuário digite uma senha até que ela seja igual a uma senha pré-definida (por exemplo "python123"). Conte e mostre o número de tentativas.
Entradas: tentativas de senha.
Saída: mensagem de sucesso e número de tentativas.

3. Jogo de adivinhação
Descrição: Gere um número aleatório entre 1 e 100. Peça palpites ao usuário até acertar. Após cada palpite informe "mais alto" ou "mais baixo" e, ao final, mostre a quantidade de tentativas.
Entradas: palpites inteiros.
Saída: dica a cada palpite, mensagem final com tentativas.

4. Fatorial com while
Descrição: Leia um inteiro não-negativo n e calcule n! usando um laço while. Mostre o resultado.
Entradas: inteiro n >= 0.
Saída: valor de n!.

5. Fibonacci até limite
Descrição: Leia um número inteiro positivo limite e gere a sequência de Fibonacci (0,1,1,2,3,...) enquanto os termos forem <= limite. Imprima os termos gerados.
Entradas: inteiro limite > 0.
Saída: lista/valores da sequência até o limite.

6. Contagem pares/ímpares até negativo
Descrição: Leia números inteiros repetidamente. Pare quando for digitado um número negativo. Ao final, informe quantos números pares e quantos ímpares foram digitados (excluindo o negativo).
Entradas: sequência de inteiros, termina com número negativo.
Saída: contagem de pares e ímpares.

7. Inversão de palavra até vazio
Descrição: Peça ao usuário que digite palavras e mostre cada palavra invertida. O programa termina quando o usuário pressiona Enter sem digitar nada (string vazia).
Entradas: palavras (strings).
Saída: palavra invertida a cada entrada.

8. Calculadora com menu
Descrição: Implemente um menu em loop com opções: 1) somar dois números, 2) subtrair, 3) multiplicar, 4) dividir, 5) sair. Após executar uma operação, volte ao menu até escolher sair.
Entradas: opção do menu e números para operação.
Saída: resultado da operação ou mensagem de erro (ex.: divisão por zero).

9. Primeiros N primos usando while
Descrição: Leia um inteiro N >= 1 e imprima os primeiros N números primos, gerando e verificando números com um laço while.
Entradas: inteiro N.
Saída: lista/valores dos N primeiros primos.

10. Contador de vogais em frases
Descrição: Leia frases do usuário em loop até a frase "sair" (case-insensitive). Para cada frase (exceto "sair"), conte e mostre quantas vogais (a,e,i,o,u) existem. Ao final, mostre o total de frases processadas.
Entradas: frases (strings).
Saída: número de vogais por frase e total de frases processadas.
"""