O trabalho pode ser feito em dupla ou de forma individual. Neste trabalho
deve ser desenvolvido um analisador sint´atico para a linguagem Matem´agica. O
analisador sint´atico deve ser capaz de compilar programas escritos utilizando a
linguagem Matem´agica para uma outra linguagem a sua escolha (como ilustrado
na Figura 1). Ou seja, o analisador sint´atico recebe como entrada um programa
na linguagem Matem´agica e produz como sa´ıda um outro programa escrito em
uma outra linguagem. A linguagem do programa de sa´ıda pode ser escolhida
por vocˆe, ela pode ser qualquer linguagem a sua escolha. Por exemplo, mas n˜ao
restrita a essas: C, C++, Java, Lua, Pyhton ou Assembly

Para a implementa¸c˜ao do analisador sint´atico, deve-se usar um gerador de
analisador sint´atico que implemente o m´etodo LaLR(1) ou outro ascendente, por
exemplo, Yacc/Lex,Bison/Flex (usa LaLR(1)), JavaCC (que usa o descendente
LL(1)), etc

A sintaxe da linguagem Matem´agica ´e dada pela gram´atica abaixo:
programa −→ cmds
cmds −→ cmd cmds | cmd
cmd −→ atribuicao | impressao | operacao | repeticao
atribuicao −→ F ACA var SER num.
impressao −→ MOST RE var. | MOST RE operacao.
operacao −→ SOME var COM var. | SOME var COM num. |
SOME num COM num.
repeticao −→ REP IT A num V EZES : cmds F IM
• Todas as vari´aveis s˜ao do tipo inteiro e n˜ao negativo.
• var s´o pode ser formado por letras e precisa ter no m´ınimo uma letra.
• num representa um n´umero.
• O terminal SOME indica que deve ser feita uma soma.
• Perceba que o terminal . sinaliza o fim dos comandos atribuicao, impressao
e operacao.
• O terminal F IM sinaliza o fim de uma repeti¸c˜ao.
Al´em disso, a linguagem Matem´agica ser´a capaz de executar um loop que ´e
definido pela regra:
repeticao −→ REP IT A num V EZES : cmds F IM
A regra acima, que define o loop, diz para repetir num vezes a sequencia de
comandos que esta em cmds.
A gram´atica acima n˜ao esta completa, neste trabalho vocˆe vai precisar definir
algumas regras a mais para incluir algumas funcionalidades. Mais importante
que isso, fique a vontade para alterar a gram´atica caso ache necess´ario para
poder gerar a linguagem que esta sendo pedida. Por exemplo, vocˆe pode retirar recurs˜ao a esquerda, fatorar ou at´e alterar as regras acima. Desde que a
linguagem final gerada seja a mesma.
Al´em disso, a gram´atica descrita acima deve ser complementada para que a
linguagem Matem´agica seja capaz de executar comandos do tipo:
• SE-ENTAO e SE-ENTAO-SENAO: Comandos de sele¸c˜ao do tipo SEENTAO. Por exemplo: SE condicao ENTAO comando. Ou SE condicao ˜
ENTAO comando SENAO comando. A condi¸c˜ao deve ser representada
por um n´umero. O n´umero 0 significa FALSO e qualquer n´umero diferente de zero significa VERDADEIRO.
• Multiplique A por B: Funcao para multiplicar A por B. Deve ser implementada no formatos: MULT IP LIQUE A P OR B .
Onde A e B podem ser vari´aveis ou n´umeros.

