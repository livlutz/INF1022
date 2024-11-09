#Lívia Lutz dos Santos - 2211055 - 3WA

import ply.lex as lex
import ply.yacc as yacc

"""A sintaxe da linguagem Matemagica e dada pela gramatica abaixo:
programa −→ cmds
cmds −→ cmd cmds | cmd
cmd −→ atribuicao | impressao | operacao | repeticao
atribuicao −→ FACA var SER num.
impressao −→ MOSTRE var. | MOSTRE operacao. | MOSTRE num.
operacao −→ SOME var COM var. | SOME var COM num. | SOME num COM var. 
SOME num COM num. | MULTIPLIQUE var POR var. | MULTIPLIQUE var POR num. | MULTIPLIQUE num POR num. | MULTIPLIQUE num POR var.
repeticao −→ REPITA num VEZES : cmds FIM
selecao −→ SE VAR ENTAO cmds FIM | SE NUM ENTAO cmds FIM | SE VAR ENTAO cmds SENAO cmds FIM | SE NUM ENTAO cmds SENAO cmds FIM
"""

# Dicionário de palavras da linguagem Matemagica
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

# Definindo os tokens da linguagem Matemagica (terminais) e adicionando as palavras reservadas
tokens = ['NUM', 'VAR', 'PONTO', 'DOISPONTOS'] + list(reserved.values())

# Regex para variáveis (identificadores)
def t_VAR(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'VAR')  # Se não for uma palavra reservada, é uma variável
    return t

#Expressoes regulares para os tokens
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
    t.value = int(t.value) 
    return t

#Funcao para tratar erros
def t_error(t):
    print(f"Caracter ilegal: '{t.value[0]}' na posição {t.lexpos}")
    t.lexer.skip(1)
    
# Ignora newline
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Definindo a gramatica

#programa −→ cmds
def p_programa(p):
    '''programa : cmds'''
    p[0] = p[1]

#cmds −→ cmd cmds | cmd
def p_cmds(p):
    '''cmds : cmd cmds
            | cmd'''
    if len(p) == 3:
        p[0] = p[1] + "\n" + p[2]
    else:
        p[0] = p[1]

#cmd −→ atribuicao | impressao | operacao | repeticao | selecao
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
    p[0] = f"{p[2]} = {p[4]}"

#impressao −→ MOSTRE var. | MOSTRE operacao. | MOSTRE num. tem q virar print(var), print(operacao) ou print(num)
def p_impressao(p):
    '''impressao : MOSTRE VAR PONTO
                 | MOSTRE operacao PONTO
                 | MOSTRE NUM PONTO'''
    p[0] = f"print({p[2]})"

#operacao −→ SOME var COM var. | SOME var COM num. | SOME num COM num. | MULTIPLIQUE var POR var. | MULTIPLIQUE var POR num. | MULTIPLIQUE num POR num. | MULTIPLIQUE num POR var.
#tem q virar var + var, var + num, num + num, var * var, var * num, num * num, num * var
def p_operacao(p):
    '''operacao : SOME VAR COM VAR PONTO
                | SOME VAR COM NUM PONTO
                | SOME NUM COM NUM PONTO
                | SOME NUM COM VAR PONTO
                | MULTIPLIQUE VAR POR VAR PONTO
                | MULTIPLIQUE VAR POR NUM PONTO
                | MULTIPLIQUE NUM POR NUM PONTO
                | MULTIPLIQUE NUM POR VAR PONTO'''
                
    if p[1] == "SOME":
        p[0] = f"{p[2]} = {p[2]} + {p[4]}"
        
    else:
        p[0] = f"{p[2]} = {p[2]} * {p[4]}"


#repeticao −→ REPITA num VEZES : cmds FIM
def p_repeticao(p):
    '''repeticao : REPITA NUM VEZES DOISPONTOS cmds FIM'''
    p[0] = "for i in range(" + str(p[2]) + "):\n\t" + p[5].replace("\n", "\t")


#selecao −→ SE VAR ENTAO cmds FIM | SE NUM ENTAO cmds FIM | SE VAR ENTAO cmds SENAO cmds FIM | SE NUM ENTAO cmds SENAO cmds FIM
#no else tem q ter um \n para pular linha e voltar a identacao
def p_selecao(p):
    '''selecao : SE VAR ENTAO cmds FIM
               | SE NUM ENTAO cmds FIM
               | SE VAR ENTAO cmds SENAO cmds FIM
               | SE NUM ENTAO cmds SENAO cmds FIM'''

    num_ou_var = p[2] if isinstance(p[2], str) else (p[2] != 0)

    if len(p) == 6:
        p[0] = f"if {num_ou_var}:\n\t" + p[4].replace("\n", "\n\t")
    
    else:
        p[0] = f"if {num_ou_var}:\n\t" + p[4].replace("\n", "\n\t") + "\nelse:\n\t" + p[6].replace("\n", "\n\t")

# Função de erro
def p_error(p):
    if p:
        print(f"Erro de sintaxe no token '{p.value}', linha {p.lineno}")
    else:
        print("Erro de sintaxe: token inesperado no final do arquivo")
    
#Constroi o lexer
lexer = lex.lex(debug=True)

# Constroi o parser
parser = yacc.yacc(debug = True)

#contagem de testes realizados
contTestes = 0

# Realiza os testes para os arquivos file1.mag até file8.mag
for i in range(1, 9):
    
    #montando nomes para os arquivos de entrada e saida
    stringFileMag = "file" + str(i) + ".mag"
    stringFilePy = "file" + str(i) + ".py"
    
    #lendo a entrada
    with open(stringFileMag, "r") as file:
        data = file.read()

    # Realiza a análise léxica
    lexer.input(data)

    # Faz a analise sintatica do arquivo .mag
    result = parser.parse(data)
    
    #se nao houver erros
    if result:
        print("Código gerado para a file" + str(i) + ".mag:")
        
        #escreve o codigo gerado em um arquivo .py
        with open(stringFilePy, "w") as file:
            file.write(result)
        
        # Imprime o código gerado
        print(result)
        
        # Executa o código
        exec(result)
        
        contTestes += 1
        
    else:
        print("Erro ao gerar o código da file" + str(i) + ".mag")
        print("Tokens gerados:")
        
        for token in lexer:
            print(token)
            
        print(result)
        
if(contTestes == 8):
    print("Todos os testes foram realizados com sucesso!")

    