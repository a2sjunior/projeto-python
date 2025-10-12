import random
import unicodedata
import sys

#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Lista de (palavra, dica) em português
PALAVRAS = [
    ("python", "linguagem de programação"),
    ("cachorro", "animal de estimação"),
    ("computador", "máquina para calcular"),
    ("brasil", "país da américa do sul"),
    ("jardim", "lugar com plantas"),
    ("aviao", "meio de transporte voador"),
    ("chave", "usada para abrir portas"),
    ("teclado", "entrada de texto"),
    ("bicicleta", "meio de transporte não motorizado"),
    ("futebol", "esporte popular")
]

STAGES = [
r"""
  +---+
  |   |
      |
      |
      |
      |
=========
""",
r"""
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
r"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
r"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
r"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
r"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
r"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
"""
]

MAX_ERROS = len(STAGES) - 1

def normalize(s):
    s = s.lower()
    return ''.join(ch for ch in unicodedata.normalize('NFD', s) if unicodedata.category(ch) != 'Mn')

def escolher_palavra():
    return random.choice(PALAVRAS)

def mostrar_estado(palavra_orig, palavra_norm, letras_acertadas, erros, usadas, dica):
    print(STAGES[erros])
    exib = []
    for i, ch in enumerate(palavra_orig):
        if palavra_norm[i] in letras_acertadas:
            exib.append(ch)
        elif ch == " ":
            exib.append(" ")
        else:
            exib.append("_")
    print("Palavra: " + " ".join(exib))
    print(f"Dica: {dica}")
    print("Letras usadas:", " ".join(sorted(usadas)))
    print(f"Erros: {erros}/{MAX_ERROS}")
    print()

def jogo():
    palavra_orig, dica = escolher_palavra()
    palavra_norm = normalize(palavra_orig)
    letras_acertadas = set()
    usadas = set()
    erros = 0

    while True:
        mostrar_estado(palavra_orig, palavra_norm, letras_acertadas, erros, usadas, dica)

        entrada = input("Digite uma letra (ou tente a palavra inteira): ").strip()
        if not entrada:
            continue
        entrada = entrada.lower()
        # Normalizar entrada
        entrada_norm = normalize(entrada)

        if len(entrada_norm) == 1:
            letra = entrada_norm
            if letra in usadas:
                print("Você já tentou essa letra.\n")
                continue
            usadas.add(letra)
            if letra in palavra_norm:
                # adicionar todas as ocorrências
                letras_acertadas.add(letra)
                print("Boa! Letra correta.\n")
            else:
                erros += 1
                print("Letra incorreta.\n")
        else:
            # tentativa de adivinhar a palavra inteira
            if entrada_norm == palavra_norm:
                print("\nParabéns! Você adivinhou a palavra inteira!\n")
                # revelar todas as letras
                letras_acertadas.update(set(palavra_norm))
                mostrar_estado(palavra_orig, palavra_norm, letras_acertadas, erros, usadas, dica)
                break
            else:
                erros += 1
                print("Palavra incorreta.\n")

        # verificar vitória
        if all(ch in letras_acertadas or ch == " " for ch in palavra_norm):
            print("Parabéns! Você ganhou!\n")
            mostrar_estado(palavra_orig, palavra_norm, letras_acertadas, erros, usadas, dica)
            break

        if erros >= MAX_ERROS:
            print(STAGES[erros])
            print(f"Você perdeu! A palavra era: {palavra_orig}\n")
            break

def main():
    print("JOGO DA FORCA - CLI (Português)")
    try:
        while True:
            jogo()
            resp = input("Jogar novamente? (s/n): ").strip().lower()
            if resp != 's':
                print("Obrigado por jogar.")
                break
    except (KeyboardInterrupt, EOFError):
        print("\nSaindo. Até a próxima.")
        sys.exit(0)

if __name__ == "__main__":
    main()