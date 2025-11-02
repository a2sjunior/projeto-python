"""
Estruturas de Repetição em Python
Definição: Estruturas de repetição são usadas para executar um bloco de código várias vezes, com base em uma condição ou um número específico de iterações.
Tipos principais:
1. for: Usado para iterar sobre uma sequência.
2. while: Executa um bloco de código enquanto uma condição for verdadeira.
"""

def sem_repeticao():
    # Exemplo sem usar for/while: pedindo 3 valores separadamente
    n1 = float(input("Digite o 1º número: "))
    n2 = float(input("Digite o 2º número: "))
    n3 = float(input("Digite o 3º número: "))
    soma = n1 + n2 + n3
    print(f"Soma (sem repetição): {soma}")


def com_repeticao():
    # Exemplo usando estrutura de repetição (for) para somar N valores
    total = 0.0
    n = int(input("Quantos números você quer somar? "))
    for i in range(1, n + 1):
        valor = float(input(f"Digite o {i}º número: "))
        total += valor
    print(f"Soma (com repetição): {total}")


if __name__ == "__main__":
    print("Exemplo 1: sem usar estruturas de repetição")
    sem_repeticao()
    print("\nExemplo 2: usando estrutura de repetição (for)")
    com_repeticao()


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