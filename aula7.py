"""
Variáveis são usadas para armazenar valores que podem mudar durante a execução do programa. Os dados são armazenados na memória do computador e podem ser acessados e modificados conforme necessário.
PEP 8 - recomendações para nomes de variáveis:
- Use letras minúsculas e underscores para separar palavras (snake_case).
- Nomes de variáveis devem ser descritivos e significativos.
- Evite usar palavras reservadas do Python como nomes de variáveis.

O sinal de igual (=) é usado para atribuir valores às variáveis.
Uso: nome_da_variavel = valor
"""

# Exemplos de nomes de variáveis:
nome_completo = "João Silva"
idade = 25
eh_maior_de_idade = idade >= 18

print('Nome:', nome_completo, 'Idade:', idade)
print('É maior de idade?', eh_maior_de_idade)

"""
Constantes em Python
Constantes em programação são valores fixos que não podem ser alterados após a sua declaração, ao contrário das variáveis, cujo valor pode ser modificado durante a execução do programa.  

Ao contrário de algumas linguagens que possuem palavras-chave específicas para definir constantes, Python não possui um mecanismo dedicado para declarar valores constantes. No entanto, a comunidade de programadores Python segue uma convenção para indicar que uma variável é considerada uma constante, utilizando letras maiúsculas e separando palavras com underscores (snake_case). 

Exemplos:
"""

# Constantes matemáticas
PI = 3.14159
EULER_NUMBER = 2.71828
GRAVIDADE = 9.8

# Constantes de configuração
MAX_TENTATIVAS = 3
TEMPO_LIMITE = 60

# Constantes de mensagens
MENSAGEM_BOAS_VINDAS = "Bem-vindo ao programa!"

# Constantes de status
STATUS_ATIVO = "ativo"
STATUS_INATIVO = "inativo"