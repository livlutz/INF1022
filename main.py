#Livia Lutz dos Santos - 2211055 - 3WA

import ply.lex as lex
from ply.yacc import yacc

"""A sintaxe da linguagem Matem´agica ´e dada pela gram´atica abaixo:
programa −→ cmds
cmds −→ cmd cmds | cmd
cmd −→ atribuicao | impressao | operacao | repeticao
atribuicao −→ FACA var SER num.
impressao −→ MOSTRE var. | MOSTRE operacao.
operacao −→ SOME var COM var. | SOME var COM num. |
SOME num COM num. | MULTIPLIQUE var POR var. | MULTIPLIQUE var POR num. | MULTIPLIQUE num POR num. | MULTIPLIQUE num POR var.
repeticao −→ REPITA num VEZES : cmds FIM
selecao −→ SE num ENTAO cmds | SE num ENTAO cmds SENAO cmds | SE num ENTAO cmds SENAO cmds FIM

Alem disso, a gramatica descrita acima deve ser complementada para que a linguagem Matemagica seja capaz de executar comandos do tipo:

• SE-ENTAO e SE-ENTAO-SENAO: Comandos de selecao do tipo SE ENTAO. Por exemplo: 
SE condicao ENTAO comando. 
Ou SE condicao ENTAO comando SENAO comando. 
A condicao deve ser representada por um numero. O numero 0 significa FALSO e qualquer numero diferente de zero significa VERDADEIRO.

• Multiplique A por B: Funcao para multiplicar A por B. Deve ser implementada no formatos: MULTIPLIQUE A P OR B .
Onde A e B podem ser variaveis ou numeros"""

#tokens para os terminais da linguagem

tokens = ('FACA', 'SER', 'MOSTRE', 'SOME', 'COM', 'MULTIPLIQUE', 'POR', 'REPITA', 'VEZES', 'FIM', 'SE', 'ENTAO', 'SENAO', 'NUM', 'VAR','PONTO', 'DOISPONTOS')

#expressoes regulares para os tokens
t_FACA = r'FACA'
t_SER = r'SER'
t_MOSTRE = r'MOSTRE'
t_SOME = r'SOME'
t_COM = r'COM'
t_MULTIPLIQUE = r'MULTIPLIQUE'
t_POR = r'POR'
t_REPITA = r'REPITA'
t_VEZES = r'VEZES'
t_FIM = r'FIM'
t_SE = r'SE'
t_ENTAO = r'ENTAO'
t_SENAO = r'SENAO'
t_PONTO = r'\.'
t_DOISPONTOS = r':'

# Ignora espaços em branco e tabulações
t_ignore = ' \t'

# definindo regex para os numeros
def t_NUM(t):
    r'\d+'
    t.value = int(t.value)  # Converte o valor do token para inteiro
    return t

# definindo regex para as variaveis
def t_VAR(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_error(t): # nos dizer qual caractere ilegal e se tem erro
    print("Caracter ilegal: ", t.value[0])
    t.lexer.skip(1)

#Constroi o lexer
lexer = lex.lex(debug=True)

#fazer isso para todas as files
with open("file1.mag", "r") as file:
    data = file.read()

lexer.input(data)

# Imprime os tokens gerados
for tok in lexer:
    print(tok)



