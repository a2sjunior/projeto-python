"""
A função print() em Python
- Imprime valores na tela
- Pode receber múltiplos argumentos separados por vírgula
- Parâmetros opcionais:
    - sep: define o separador entre os valores (padrão é espaço)
    - end: define o que é impresso no final (padrão é nova linha)
"""
print(1, 2, 3)
print(4, 5, 6, sep="-")
print(4, 5, 6, sep='#')

"""
CRLF (Carriage Return + Line Feed) e LF (Line Feed) 
são caracteres de controle que indicam o fim de uma linha num texto,  
Windows usa CRLF (\r\n), 
Unix/Linux e macOS usam LF (\n).
"""
print(4, 5, 6, sep='-', end=' FIM\n')