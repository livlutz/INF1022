#Livia Lutz dos Santos - 2211055 - 3WA

import ply.lex as lex

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

#Lista dos tokens da linguagem
tokens = ('SER','SOME','MULTIPLIQUE','FACA','MOSTRE','COM','REPITA','FIM','SE','ENTAO','SENAO','POR','VEZES','VAR','NUM')

#Palavras reservadas
reserved = {
    'FACA':'FACA',
    'SER':'SER',
    'MOSTRE':'MOSTRE',
    'SOME':'SOME',
    'MULTIPLIQUE':'MULTIPLIQUE',
    'REPITA':'REPITA',
    'FIM':'FIM',
    'SE':'SE',
    'ENTAO':'ENTAO',
    'SENAO':'SENAO',
    'POR':'POR',
    'VEZES':'VEZES',
    'VAR':'VAR',
    'NUM':'NUM'
}

#Expressoes regulares para os tokens
def t_VAR(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value,'VAR')
    return t

def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    return t

def t_error(t):
    print("Caracter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)
    return t


#Constroi o lexer
lexer = lex.lex(debug=True)
