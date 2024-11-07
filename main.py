#Livia Lutz dos Santos - 2211055 - 3WA

import ply.lex as lex
import ply.yacc as yacc

"""A sintaxe da linguagem Matem´agica ´e dada pela gram´atica abaixo:
programa −→ cmds
cmds −→ cmd cmds | cmd
cmd −→ atribuicao | impressao | operacao | repeticao
atribuicao −→ FACA var SER num.
impressao −→ MOSTRE var. | MOSTRE operacao.
operacao −→ SOME var COM var. | SOME var COM num. |
SOME num COM num. | MULTIPLIQUE var POR var. | MULTIPLIQUE var POR num. | MULTIPLIQUE num POR num. | MULTIPLIQUE num POR var.
repeticao −→ REPITA num VEZES : cmds FIM
selecao --> SE VAR ENTAO cmds FIM| SE NUM ENTAO cmds FIM | SE VAR ENTAO cmds SENAO cmds FIM| SE NUM ENTAO cmds SENAO cmds FIM

Alem disso, a gramatica descrita acima deve ser complementada para que a linguagem Matemagica seja capaz de executar comandos do tipo:

• SE-ENTAO e SE-ENTAO-SENAO: Comandos de selecao do tipo SE ENTAO. Por exemplo: 
SE condicao ENTAO comando. 
Ou SE condicao ENTAO comando SENAO comando. 
A condicao deve ser representada por um numero. O numero 0 significa FALSO e qualquer numero diferente de zero significa VERDADEIRO.

• Multiplique A por B: Funcao para multiplicar A por B. Deve ser implementada no formatos: MULTIPLIQUE A P OR B .
Onde A e B podem ser variaveis ou numeros"""

#tokens para os terminais da linguagem

# Dicionário de palavras reservadas
reserved = {
    'FACA': 'FACA',
    'SER': 'SER',
    'MOSTRE': 'MOSTRE',
    'SOME': 'SOME',
    'COM': 'COM',
    'MULTIPLIQUE': 'MULTIPLIQUE',
    'POR': 'POR',
    'REPITA': 'REPITA',
    'VEZES': 'VEZES',
    'FIM': 'FIM',
    'SE': 'SE',
    'ENTAO': 'ENTAO',
    'SENAO': 'SENAO'
}

# Definindo o token VAR como qualquer palavra que não seja uma palavra reservada
tokens = ['NUM', 'VAR', 'PONTO', 'DOISPONTOS'] + list(reserved.values())

# Regex para variáveis e palavras-chave
def t_VAR(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'VAR')  # Se não for uma palavra reservada, é uma variável
    return t

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


def t_error(t):
    print(f"Caracter ilegal: '{t.value[0]}' na posição {t.lexpos}")
    t.lexer.skip(1)
    
# Ignora novas linhas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

#Constroi o lexer
lexer = lex.lex(debug=True)

# Definindo a gramatica

def p_programa(p):
    '''programa : cmds'''
    p[0] = p[1]

def p_cmds(p):
    '''cmds : cmd cmds
            | cmd'''
    if len(p) == 3:
        p[0] = p[1] + p[2]
    else:
        p[0] = p[1]

def p_cmd(p):
    '''cmd : atribuicao
              | impressao
              | operacao
              | repeticao
              | selecao'''
    p[0] = p[1]

#atribuicao −→ FACA var SER num. tem q virar var = num
def p_atribuicao(p):
    '''atribuicao : FACA VAR SER NUM PONTO'''
    p[0] = p[2] + " = " + str(p[4]) + "\n"

#impressao −→ MOSTRE var. | MOSTRE operacao. tem q virar print(var) ou print(operacao)
def p_impressao(p):
    '''impressao : MOSTRE VAR PONTO
                 | MOSTRE operacao PONTO'''
    p[0] = "print(" + str(p[2]) + ")\n"

#operacao −→ SOME var COM var. | SOME var COM num. | SOME num COM num. | MULTIPLIQUE var POR var. | MULTIPLIQUE var POR num. | MULTIPLIQUE num POR num. | MULTIPLIQUE num POR var.
#tem q virar var + var, var + num, num + num, var * var, var * num, num * num, num * var
def p_operacao(p):
    '''operacao : SOME VAR COM VAR PONTO
                | SOME VAR COM NUM PONTO
                | SOME NUM COM NUM PONTO
                | MULTIPLIQUE VAR POR VAR PONTO
                | MULTIPLIQUE VAR POR NUM PONTO
                | MULTIPLIQUE NUM POR NUM PONTO
                | MULTIPLIQUE NUM POR VAR PONTO'''
    if p[1] == "SOME":
        # Atribui o resultado da soma à primeira variável
        p[0] = f"{p[2]} = {p[2]} + {p[4]}\n"
    else:
        # Atribui o resultado da multiplicação à primeira variável
        p[0] = f"{p[2]} = {p[2]} * {p[4]}\n"


#repeticao −→ REPITA num VEZES : cmds FIM
def p_repeticao(p):
    '''repeticao : REPITA NUM VEZES DOISPONTOS cmds FIM'''
    p[0] = "for i in range(" + str(p[2]) + "):\n\t" + p[5].replace("\n", "\t") + "\n"


#selecao −→ SE VAR ENTAO cmds FIM | SE NUM ENTAO cmds FIM | SE VAR ENTAO cmds SENAO cmds FIM | SE NUM ENTAO cmds SENAO cmds FIM
def p_selecao(p):
    '''selecao : SE VAR ENTAO cmds FIM
               | SE NUM ENTAO cmds FIM
               | SE VAR ENTAO cmds SENAO cmds FIM
               | SE NUM ENTAO cmds SENAO cmds FIM'''
    if len(p) == 6:
        # Gerar apenas uma indentação para o bloco interno
        p[0] = f"if {p[2]}:\n    " + p[4].replace("\n", "\n    ")
    else:
        # Gerar apenas uma indentação para os blocos internos do if e else
        p[0] = f"if {p[2]}:\n    " + p[4].replace("\n", "\n    ") + "\nelse:\n    " + p[6].replace("\n", "\n    ")


def p_error(p):
    print("Erro de sintaxe!")

#fazer isso para todas as files
with open("file5.mag", "r") as file:
    data = file.read()

lexer.input(data)

# Imprime os tokens gerados
for tok in lexer:
    print(tok)

# Constroi o parser
parser = yacc.yacc()

# Faz o parsing do arquivo e imprime o código gerado
result = parser.parse(data)
if result:
    print("Código gerado:")
    print(result)
    # Executa o código
    exec(result)
else:
    print("Erro ao gerar o código.")


    