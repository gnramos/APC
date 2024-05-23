# Estruturas de Dados

!!! quote "[David Jones](http://www0.cs.ucl.ac.uk/staff/D.Jones/)"

    Acerte as estruturas de dados primeiro, e o resto do programa se escreverá sozinho.

---

*<img style="height:20px!important;margin-left:3px;display:inline-block;vertical-align:middle;" src="https://img.shields.io/badge/TODO-Introdução-red">*

---

Todo processo no computador gerencia a execução de um programa armazenado, a implementação de um algoritmo computacional nãos sendo, portanto, possível dissociar um algoritmo de dados manipulados - o próprio programa é um conjunto de dados (as instruções). Além disso, praticamente todos os programas manipulas dados fornecidos e gerados no processamento, na forma de variáveis ou constantes, que são os objetos de dados básicos manipulados em um programa[@Kernighan1989].

O forma como organizamos estes dados tem impacto direto no desempenho do computador. Ao executar um algoritmo computacional, estamos exigindo esforço da máquina para realizar o trabalho de processamento. Este esforço depende da quantidade de instruções sendo executadas, e do custo de cada instruções (podemos ter instruções mais simples e baratas, e instruções mais complexas e caras). A organização dos dados tem impacto direto neste esforço, e buscamos deixá-los organizados de forma a tornar o processo menos custoso. Por exemplo, imagine que seu problema é interpretar números e somá-los, é muito mais fácil[^1] fazer isso se lhe forem apresentados os números estruturados como $49$ e $1$ (com resultado $50$) que se fossem como $XLIX$ e $I$ (também com resultado $L$).

A memória do computador é um conjunto ordenado de bits, ou seja, toda informação é armazenada como zeros e uns e há uma ordem posicional entre eles (existe um primeiro bit, que pode ser `0/1`, um segundo bit que também pode ser `0/1`, e assim sucessivamente até um último bit). Para facilitar, há uma [nomenclatura específica](http://pt.wikipedia.org/wiki/Byte) para lidar com a quantidade de bits sendo 1 byte (8 bits) a unidade mais comum para quantificá-lo. A composição de bits permite representar mais estados; 2 bits são 4 estados (<code>00/01/11/10</code>), 3 bits definem 8 estados, e assim sucessivamente - havendo $n$ bits podemos definir $2^n$ estados distintos. O significado da informação armazenada depende da forma de interpretar estes bits, um mesmo conjunto de bits tem significados diferentes se for interpretado como um número, um símbolo ou outra coisa. Por exemplo, um byte pode assumir um de 256 valores numéricos diferentes, mas também pode representar inúmeras informações diferentes se mudarmos a forma de interpretá-lo.

![Diferentes interpretações para 1 byte](../assets/img/byte_interpretacao.png "Diferentes interpretações para 1 byte"){ width="75%" }

A representação do dado é necessariamente binária mas a interpretação dos bits é o que define a informação. Esta interpretação é determinada pelo *tipo de dado*, e cada tipo tem suas características específicas definidas pela linguagem de programação. Por exemplo, o conjunto de bits <code>01000001001000000000000000000000</code> pode ser interpretado como o valor numérico do tipo inteiro 1092616192, como o valor numérico do tipo real 10.0 ou como um tipo simbólico <code>A</code> ([ASCII](https://pt.wikipedia.org/wiki/ascii)). Estes três tipos de dados, entre outros, geralmente estão presentes em qualquer linguagem de programação.

!!! note

    Como um mesmo conjunto de bits pode ser interpretado de diferentes formas, é preciso saber que tipo de dado foi armazenado na memória para interpretá-lo corretamente.

Um *[id> tipo abstrato de dado]* (TAD) determina um tipo de dado e as operações definidas sobre ele, delimitando assim a quantidade de informação necessária para manipulação dos valores pelo computador e, consequentemente, facilitando a programação. Por exemplo, o conjunto de números naturais $\mathbb{N}$ e suas operações (como $+, -, /, *$) é um TAD.

!!! info "Estrutura de Dados"

    Forma concreta de se implementar um tipo abstrato de dados em uma linguagem de programação, de modo a organizar os dados na memória para facilitar o acesso e a manipulação destes.

Portanto, para cada linguagem de programação específica, o tipo do dado determina:

1. o significado do valor armazenado;
1. como o valor é armazenado nos bits;
1. quais os possíveis valores que podem ser armazenados; e
1. quais as operações podem ser realizadas com o valor.

!!! note

    As características de uma estrutura de dados específica são importantes pois determinam o que pode e também o que **não** pode ser feito com ela.

<h2>Números</h2>

Um *número* é um objeto matemático usado para descrever uma quantidade, e uma *base numérica* é um conjunto de algarismos utilizados para representar um número. Quais são os símbolos e as regras de como utilizá-los são definidos pelos sistema de numeração usado. O valor de um número é único, mas sua representação pode variar conforme o sistema utilizado - é fácil ilustrar isso comparando o abordagem usamos normalmente, com [algarismos arábicos](https://pt.wikipedia.org/wiki/Algarismos_ar%C3%A1bicos) e a [notação posicional](https://pt.wikipedia.org/wiki/Nota%C3%A7%C3%A3o_posicional), à abordagem que os [antigos romanos](https://pt.wikipedia.org/wiki/Numera%C3%A7%C3%A3o_romana) usavam. Para o valor quarenta e nove, temos as representações $49$ e $XLIX$, respectivamente.

Na notação posicional, o valor representado por um algarismo depende da posição em que ele se encontra no conjunto de símbolos que representa o número, sendo valores a esquerda mais influentes que os a direita. O valor deste número é determinado pela soma dos valores relativos de cada algarismo. Por exemplo: 123 = 100 + 20 + 3, o algarismo mais a esquerda (1) tem uma influência maior que os demais no valor, e é considerado o mais significativo. O algarismo seguinte (2) tem uma influência menor que o anterior, mas maior que o seguinte. Isso se sucede até o último algarismo, o mais a direita, que é chamado de menos significativo. Podemos reescrever a informação da seguinte forma:

$$123 = 100 + 20 + 3 = 1·10^2+ 2·10^1+ 3·10^0$$

Nesta representação, duas coisas se destacam. A primeira é que a influência de cada algarismo é determinada por uma potência de 10, que é a base numérica. A segunda, é que esta potência é uma sequência crescente da posição menos significativa para a mais significativa, iniciando-se por 0. De forma mais genérica, um algarismo $A$ tem uma influência proporcional a sua posição $i$ para uma base numérica $B$.

$$A·{B^i}$$

No valor 123, na [base decimal](https://pt.wikipedia.org/wiki/Sistema_de_numera%C3%A7%C3%A3o_decimal), entendemos seu valor pela soma de seus componentes. O algarismo 3 está na posição mais a direita, considerada como posição $i = 0$, portanto seu peso no valor resultante é de 3·10$^0$. A posição seguinte (a esquerda) é i = 1 com o algarismo 2, acrescentando 2·10$^1$ ao resultado. O último algarismo (mais a esquerda) é 1 e está na posição 2, acrescentando 1·10$^2$. De forma genérica, o valor de um número em uma base numérica $B$ qualquer, representado com $n$ algarismos $A_i : A \in [0, B), i \in [0, n)$, é calculado com a seguinte fórmula:

$$A_{n-1}A_{n-2}…{A_2}A_1A_0 = \sum\limits_{i=0}^{n - 1}{A_i·{B^i}}$$

Para representar a informação numérica na memória do computador, ela necessariamente deve ser representada como um conjunto de bits. Isto é relativamente simples, o bit tem dois estados, 0/1 que são os algarismos da *[base numérica binária](https://pt.wikipedia.org/wiki/Sistema_de_numera%C3%A7%C3%A3o_bin%C3%A1rio)*. Portanto, podemos usar esta base na notação posicional para basta representar um valor numérico qualquer como bits na memória. Como também usaremos algarismos arábicos, para diferenciar as bases numéricas acrescentamos um sufixo ao número.

$$1101_2 = 1·2^3+ 1·2^2+ 0·2^1+ 1·2^0 = 8 + 4 + 0 + 1 = 13_{10}$$

Por ser uma base de valor baixo, são poucos os algarismos e, portanto, as representações dos números se tornam extensas. Outras bases de valor mais elevado permitem compactar isso, e as mais úteis são as múltiplas de 2 já que a [conversão](https://pt.wikipedia.org/wiki/Convers%C3%A3o_de_base_num%C3%A9rica) delas para a binária é simplificada. A tabela abaixo mostra alguns valores nas bases mais comuns na computação: binária, [octal](https://pt.wikipedia.org/wiki/Sistema_octal), decimal e [hexadecimal](https://pt.wikipedia.org/wiki/Sistema_de_numera%C3%A7%C3%A3o_hexadecimal). Note que, como a notação posicional utiliza apenas um símbolo por posição, a base hexadecimal define os valores superiores a 9 (o maior algarismo arábico) para letras do alfabeto latino.

<center>

| binária | octal | decimal | hexadecimal |
|---------|-------|---------|-------------|
| 0       | 0     | 0       | 0           |
| 1       | 1     | 1       | 1           |
| 10      | 2     | 2       | 2           |
| 11      | 3     | 3       | 3           |
| 100     | 4     | 4       | 4           |
| 101     | 5     | 5       | 5           |
| 110     | 6     | 6       | 6           |
| 111     | 7     | 7       | 7           |
| 1000    | 10    | 8       | 8           |
| 1001    | 11    | 9       | 9           |
| 1010    | 12    | 10      | A           |
| 1011    | 13    | 11      | B           |
| 1100    | 14    | 12      | C           |
| 1101    | 15    | 13      | D           |
| 1110    | 16    | 14      | E           |
| 1111    | 17    | 15      | F           |
| 101010  | 52    | 42      | 2A          |
| 1111011 | 173   | 123     | 7B          |

</center>

### Números Inteiros

Já vimos a representação dos [números naturais](https://pt.wikipedia.org/wiki/N%C3%BAmero_natural) em binário. Entretanto, muitas problemas lidam com os [números inteiros](https://pt.wikipedia.org/wiki/N%C3%BAmero_inteiro), que podem ter valores negativos. Felizmente, um número só pode ser negativo ou não, ou seja, a informação do sinal é facilmente representada em um bit. A convenção é que o bit mais a esquerda armazena a informação se o número é negativo (ligado/1) ou se é positivo (desligado/0), e os demais bits armazenam a informação do valor do número. Há formas distintas de se interpretar este último conjunto de bits, como listadas a seguir.

[Sinal e Magnitude](https://pt.wikipedia.org/wiki/Representa%C3%A7%C3%A3o_de_n%C3%BAmeros_com_sinal#M.C3.A9todo_sinal-e-magnitude), onde o bit mais significativo indica o sinal e os demais bits determinam o valor diretamente pela notação posicional (como um número natural). Esta abordagem é intuitivamente simples para entendermos.

<center>

| bits    | sinal | notação posicional | decimal |
|---------|-------|--------------------|---------|
| **0**00 | +00   | $+(0·2^1+ 0·2^0)$  | +0      |
| **0**01 | +01   | $+(0·2^1+ 1·2^0)$  | +1      |
| **0**10 | +10   | $+(1·2^1+ 0·2^0)$  | +2      |
| **0**11 | +11   | $+(1·2^1+ 1·2^0)$  | +3      |
| **1**00 | -00   | $-(0·2^1+ 0·2^0)$  | -0      |
| **1**01 | -01   | $-(0·2^1+ 1·2^0)$  | -1      |
| **1**10 | -10   | $-(1·2^1+ 0·2^0)$  | -2      |
| **1**11 | -11   | $-(1·2^1+ 1·2^0)$  | -3      |

</center>

[Complemento de um](https://pt.wikipedia.org/wiki/Representa%C3%A7%C3%A3o_de_n%C3%BAmeros_com_sinal#Complemento_para_um) também considera o bit mais a esquerda como indicador de sinal e os demais para o valor, conforme o sinal. Se *positivo*, os bits restantes indicam o valor pela notação posicional (como na abordagem de sinal e magnitude); se *negativo*, é preciso inverter todos os bits antes de considerar a notação posicional. Esta variação é um pouco mais complexa para entendermos, mas tem vantagens quanto à anterior para algumas operações. Uma delas é que precisa-se de menos esforço para para inverter o sinal de um valor, uma operação muito frequente em problemas computacionais. Usando complemento de um, basta inverter todos os bits.

<center>

| bits    | sinal | inverte? |     | notação posicional | decimal |
|---------|-------|----------|-----|--------------------|---------|
| **0**00 | +00   | não      | +00 | $+(0·2^1+ 0·2^0)$  | +0      |
| **0**01 | +01   | não      | +01 | $+(0·2^1+ 1·2^0)$  | +1      |
| **0**10 | +10   | não      | +10 | $+(1·2^1+ 0·2^0)$  | +2      |
| **0**11 | +11   | não      | +11 | $+(1·2^1+ 1·2^0)$  | +3      |
| **1**00 | -00   | sim      | -11 | $-(1·2^1+ 1·2^0)$  | -3      |
| **1**01 | -01   | sim      | -10 | $-(1·2^1+ 0·2^0)$  | -2      |
| **1**10 | -10   | sim      | -01 | $-(0·2^1+ 1·2^0)$  | -1      |
| **1**11 | -11   | sim      | -00 | $-(0·2^1+ 0·2^0)$  | -0      |

</center>

Por fim, a forma mais utilizada é [complemento de dois](https://pt.wikipedia.org/wiki/Complemento_para_dois). Nela, também o bit mais a esquerda define o sinal e os demais determinam o valor conforme o sinal. Se *positivo*, os bits restantes indicam o valor pela notação posicional; se *negativo*, é preciso inverter todos os bits e incrementar em 1 o resultado antes de considerar a notação posicional. Embora mais complicada para nós, esta abordagem tem vantagens sobre as demais, como quantidade de valores distintos que se pode armazenar e facilidade na computação de operações aritméticas.

<center>

| bits    | sinal | inverte? |     |  +1 |      | notação posicional       | decimal |
|---------|-------|----------|-----|-----|------|--------------------------|---------|
| **0**00 | +00   | não      | +00 | não | +00  | $+(0·2^1+ 0·2^0)$        | +0      |
| **0**01 | +01   | não      | +01 | não | +01  | $+(0·2^1+ 1·2^0)$        | +1      |
| **0**10 | +10   | não      | +10 | não | +10  | $+(1·2^1+ 0·2^0)$        | +2      |
| **0**11 | +11   | não      | +11 | não | +11  | $+(1·2^1+ 1·2^0)$        | +3      |
| **1**00 | -00   | sim      | -11 | sim | -100 | $-(1·2^2+ 0·2^1+ 0·2^0)$ | -4      |
| **1**01 | -01   | sim      | -10 | sim | -011 | $-(0·2^2+ 1·2^1+ 1·2^0)$ | -3      |
| **1**10 | -10   | sim      | -01 | sim | -010 | $-(0·2^2+ 1·2^1+ 0·2^0)$ | -2      |
| **1**11 | -11   | sim      | -00 | sim | -001 | $-(0·2^2+ 0·2^1+ 1·2^0)$ | -1      |

</center>

Geralmente, valores inteiros são armazenados em um tipo de dado `inteiro` de 32 ou 64 bits. Considerando o primeiro caso, a estrutura de dados para complemento de dois determina:

1. O significado é de um valor numérico inteiro, que pode ser negativo.
1. O valor é armazenado como Complemento de 2 nos 32 bits.
1. Os possíveis valores armazenados estão no intervalo $[-2^{31}, 2^{31})$.
1. As operações aritméticas básicas ($+, -, \times\ e\ \div$) estão definidas na linguagem de programação - e possivelmente outras.

### Números Reais

Os [números reais](https://pt.wikipedia.org/wiki/N%C3%BAmero_real) também podem ser representados como binários pelo sistema posicional, basta estender a lógica da notação posicional. Por exemplo, considere o seguinte número decimal:

$$13,125 = 1\cdot{10^1} + 3\cdot{10^0} + 1\cdot{10^{-1}} + 2\cdot{10^{-2}} + 5\cdot{10^{-3}}$$

Este valor pode ser representado com a mesma lógica em 7 bits:

$$1\cdot2^3 + 1\cdot2^2 + 0\cdot2^1 + 1\cdot2^0 + 0\cdot2^{-1} + 0\cdot2^{-2} + 1\cdot2^{-3} = 1101,001_2$$

Neste caso usamos 4 bits para o valor inteiro e 3 para o valor fracionário.

<h4>Ponto Fixo</h4>

A representação com [ponto fixo](https://en.wikipedia.org/wiki/Fixed-point_arithmetic) define que, dada uma quantidade $Q$ de bits para representar o número, há uma quantidade fixa $m$ de bits que armazenam a parte inteira e outra quantidade $f$ que armazena a parte fracionária do número (tais que $Q = m + f$). Por exemplo, supondo $Qm.f = Q5.3$, o número 13,125 seria representado pelos bits `01101001` cujo valor é interpretado como `01101,001`. Supondo $Q4.4$, este mesmo valor é representado por `11010010`.

O ponto fixo é uma convenção interessante, mas pouco flexível. Como toda estrutura de dados, a quantidade de bits limita os valores que podem ser armazenado, portanto uma configuração $Qm.f$ que pode ser adequada para uma aplicação específica pode ser inadequada para outra. Por exemplo, considerando que $Q=8$, uma representação $Q0.7$ é mais interessante para lidar com o tamanho de componentes eletrônicos que a $Q5.3$. Desta forma, fica inviável determinar um padrão para ponto fixo que seja suficiente para a maioria das aplicações.

<h4>Ponto Flutuante</h4>

Como alternativa mas flexível, temos a representação em [ponto flutuante](https://pt.wikipedia.org/wiki/Ponto_flutuante) que se baseia na ideia da [notação científica](https://pt.wikipedia.org/wiki/Nota%C3%A7%C3%A3o_cient%C3%ADfica) onde qualquer número pode ser representado no mesmo formato em duas componentes, separando valor numérico de sua grandeza. Dada uma *mantissa* ($m$) composta por algarismos que determinam o valor do número e um *expoente* ($e$) que determina sua grandeza, um número qualquer na base $B$ pode ser representado da seguinte forma:

$$m\cdot{B}^{e}$$

Por exemplo:

$$0,13125\cdot10^2 = 13,125_{10} \Longleftrightarrow 1101,001_2 = 0,1101001\cdot2^4$$

Esta representação oferece maior flexibilidade e alcance de valores. O padrão usado nos computadores modernos é o [IEEE 754](https://pt.wikipedia.org/wiki/Instituto_de_Engenheiros_Eletricistas_e_Eletr%C3%B4nicos#IEEE_754), que define o valor armazenado considerando um conjunto de bits de tamanho fixo em três partes: um bit para determinar o sinal, seguido de $e$ bits para o valor do expoente, seguido de $m$ bits para a mantissa. Esta abordagem permite que se use quaisquer quantidades de bits mas usualmente temos a precisão simples (32 bits em blocos de 1/8/23) e dupla (64 bits, em blocos de 1/11/52). O valor armazenado pode ser obtido pelo valor numérico simples de cada bloco desta forma:

$$(-1)^{s}\cdot1,m\cdot2^{e-offset}$$

O *offset* depende da quantidade de bits de *e*, sendo calculado como $2^{e-1}-1$. Para as precisões simples e dupla, temos os valores 127 e 1023, respectivamente. Por exemplo, para precisão simples temos que:

| sinal | expoente | mantissa                | fórmula                         | valor         |
|-------|----------|-------------------------|---------------------------------|---------------|
|   1   | 01111110 | 10000000000000000000000 | $(-1)^{1}\cdot1,1\cdot2^{-1}$   | $-0,75_{10}$  |
|   0   | 10000010 | 10100100000000000000000 | $(-1)^{0}\cdot1,101001\cdot2^3$ | $13,125_{10}$ |


O uso de ponto flutuante oferece diversas vantagens, principalmente a representação de valores absolutos muito grandes ou pequenos[@Tenenbaum1995], mas há limitações. O conjunto de números reais é infinitamente grande, e não pode ser completamente representado com a quantidade finita de bits disponível na memória, portanto é muito comum que valores em ponto flutuante sejam arredondados ao serem armazenados na quantidade fixa de bits disponível[@Goldberg1991].

Por exemplo, considere a expressão $1 / 3 = 0,33333\dots$. O valor resultante é uma dízima periódica, podemos mostrar matematicamente que $0,\overline{3} + 0,\overline{3} + 0,\overline{3} = 1$. Entretanto, $0,\overline{3}$ é uma expressão matemática com mais informação que "apenas" algarismos, ela determina um valor que não pode ser exatamente representado por uma quantidade fixa de algarismos (ou bits na memória). O que se pode fazer é usar toda a capacidade disponível para armazenar o valor mais próximo possível. Considere que só podemos usar 3 algarismos, então a expressão $0,\overline{3} + 0,\overline{3} + 0,\overline{3}$ se torna $0,33 + 0,33 + 0,33 = 0,99 \neq 1$.

Esta [imprecisão](http://pt.stackoverflow.com/a/11328) tem implicações interessantes pois, para um programa de computador, a expressão $0,1 + 0,1 + 0,1$ não resulta no valor $0,3$! O valor decimal $0,1$ é representado em binário como $0,1\overline{0011}$ até o limite de bits reservados, que é insuficiente para o valor exato. Abaixo, podemos ver as diferenças escolhendo precisões arbitrárias para mostrar um mesmo valor armazenado de $0,1$, bem como o efeito da propagação desta diferença ao longo de diversas operações:

=== "Valor"

    ```python title="Precisão" exec="on"
    --8<-- "float_precisao_valor.py"
    ```

=== "Somatório"

    ```python title="Precisão" exec="on"
    --8<-- "float_precisao_somatorio.py"
    ```

Os efeitos da imprecisão tendem a não ser considerados na maioria das aplicações (que não lidem com isso como as de engenharia/finanças/computação científica). Entretanto, deve-se ter atenção especial pois, apesar da diferença para o valor exato ser "pequena", ela existe e pode causar dificuldades se seu programa liga com algo simples como verificar se $0,1 + 0,2 = 0,3$ (algo bem provável de ocorrer em muitas aplicações). É papel do programador entender a situação e lidar com ela.

Algumas abordagens para com isso são trabalhar com inteiros e evitar comparar diretamente variáveis do tpo `float`. Se necessário, podemos realizar a comparação considerando uma tolerância razoável para a diferença entre os valores: ao invés de $a < b$, usamos $|a - b| < \epsilon$. Também é preciso atentar para acúmulo de imprecisões ao longo de múltiplas computações, pois [podem ser realmente significativos](https://www-users.cse.umn.edu/~arnold/disasters/disasters.html).

### Símbolos

Símbolos são uma forma extremamente versátil de comunicar informações; o [alfabeto](https://pt.wikipedia.org/wiki/Alfabeto) define um pequeno conjunto de símbolos que, juntos, podem expressar [quase](https://pt.wikipedia.org/wiki/Emoticon) tudo que se deseja. Símbolos, como toda informação no computador, são representados por bits.

<h4>ASCII</h4>

O padrão ASCII[@ASCII] (*American Standard Code for Information Interchange*) foi desenvolvido nos anos 60, sendo composto por 95 símbolos gráficos (letras do alfabeto latino, algarismos arábicos, sinais de pontuação e sinais matemáticos) e 33 de controle.

<center>

<h5>Controle</h5>

| bits | Símbolo | bits | Símbolo | bits | Símbolo | bits | Símbolo |
|------|---------|------|---------|------|---------|------|---------|
| 0x00 | NUL     | 0x08 | BS      | 0x10 | DLE     | 0x18 | CAN     |
| 0x01 | SOH     | 0x09 | HT      | 0x11 | DC1     | 0x19 | EM      |
| 0x02 | STX     | 0x0A | LF      | 0x12 | DC2     | ⋮   | ⋮      |
| 0x03 | ETX     | 0x0B | VT      | 0x13 | DC3     | ⋮   | ⋮      |
| 0x04 | EOT     | 0x0C | FF      | 0x14 | DC4     | ⋮   | ⋮      |
| 0x05 | ENQ     | 0x0D | CR      | 0x15 | NAK     | ⋮   | ⋮      |
| 0x06 | ACK     | 0x0E | SO      | 0x16 | SYN     | ⋮   | ⋮      |
| 0x07 | BEL     | 0x0F | SI      | 0x17 | ETB     | 0x7F | DEL     |

<h5>Gráficos (Parcial)</h5>

| bits | Símbolo | bits | Símbolo | bits | Símbolo | bits | Símbolo |
|------|---------|------|---------|------|---------|------|---------|
| 0x20 | espaço  | 0x30 | 0       | 0x41 | A       | 0x61 | a       |
| 0x21 | !       | 0x31 | 1       | 0x42 | B       | 0x62 | b       |
| 0x22 | "       | 0x32 | 2       | 0x43 | C       | 0x63 | c       |
| 0x23 | #       | 0x33 | 3       | 0x44 | D       | 0x64 | d       |
| 0x24 | $       | 0x34 | 4       | 0x45 | E       | 0x65 | e       |
| 0x25 | %       | 0x35 | 5       | ⋮   | ⋮      | ⋮   | ⋮      |
| 0x26 | &       | 0x36 | 6       | 0x57 | W       | 0x77 | w       |
| 0x27 | '       | 0x37 | 7       | 0x58 | X       | 0x78 | x       |
| 0x28 | (       | 0x38 | 8       | 0x59 | Y       | 0x79 | y       |
| 0x29 | )       | 0x39 | 9       | 0x5A | Z       | 0x7A | z       |
| ⋮   | ⋮      | ⋮   | ⋮      | ⋮   | ⋮      | ⋮   | ⋮      |

</center>

Cada um dos 128 símbolos é associado à uma sequência arbitrária e única de 7 de bits. É bem comum associar esta sequência a um número inteiro, por exemplo o número 65 ao símbolo 'A' ("um mesmo conjunto de bits pode ser interpretado de diferentes formas"). Além disso, o padrão ASCII tem algumas características interessantes. Os algarismos são listados em ordem de valor, e as letras são organizadas em ordem alfabética, o que facilita os processos de comparação entre eles. As letras minúsculas estão deslocadas em 32 posições em relação às maiúsculas, então a diferença entre os bits que as representam é apenas no sexto bit!

Por conta de como as máquinas eram construídas, era muito comum usar um byte para armazenar cada símbolo, o que viabilizou definir outros 128 símbolos arbitrários. Entretanto, não houve maior consenso em quais seriam os símbolos, afinal cada grupo tinha seus próprios interesses. No Brasil, o mais comum era o [ISO/IEC 8859-1](https://pt.wikipedia.org/wiki/ISO/IEC_8859-1). Com o avanço da internet, a necessidade de comunicação entre máquinas e grupos distintos forçou a incorporação de um padrão internacional. Entretanto, algumas dificuldades deveriam ser consideradas...

Uma solução "simples" seria usar mais bits e ampliar o tamanho da tabela, mas isso implicaria que toda informação já representada num padrão como ASCII ocuparia mais memória que o necessário. Por exemplo, supondo que fossem usados 3 bytes (possibilitando mais de 16 milhões de símbolos), uma mensagem com 10 símbolos ASCII passa a ocupar 30 bytes, 200% a mais do que necessário. Também seria necessário lidar com informações armazenadas que usam o símbolo `NUL` para indicar o término de uma sequência de símbolos - uma sequência de 8 bits com valor 0 não seria rara considerando 3 bytes. Outro ponto relevante era lidar com os documentos existentes, gerar uma cópia de todo arquivo existente com esta nova codificação seria uma tarefa inviável. A solução encontrada foi uma forma elegante de lidar com tudo isso, além de viabilizar a incorporação de quaisquer novos símbolos que possam ser criados.

<h4>Unicode</h4>

Uma vez estabelecido um padrão de *codificação de caracteres* (associação [arbitrária] de bits a certos caracteres), pode-se armazenar estes símbolos na memória (e recuperá-los). Há diversar formas de se codificar caracteres: [EBCDIC](https://pt.wikipedia.org/wiki/Extended_Binary_Coded_Decimal_Interchange_Code), [Unicode](https://pt.wikipedia.org/wiki/Unicode) (veja [isso](https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/)), ente outros.

## Booleanos

<img style="height:20px!important;margin-left:3px;display:inline-block;vertical-align:middle;" src="https://img.shields.io/badge/TODO-bool-red">

<h2>Resumo</h2>

<img style="height:20px!important;margin-left:3px;display:inline-block;vertical-align:middle;" src="https://img.shields.io/badge/TODO-Resumo-red">

??? llm

    * O que faz um programador?
    * Explique o conceito de linguagem de programação.
    * Qual a diferença entre instrução e expressão em uma linguagem de programação?
    * Explique o conceito de tipo de dados em programação.
    * O que é o fluxo de controle de um programa?

<h2>Exercícios</h2>

??? question "Dado um número não negativo qualquer na base hexadecimal, descreva o algoritmos para transformá-lo em um número binário."

    Como a base 16 é múltipla de 2, o processo manual é bem simples. Cada algarismo hexadecimal pode ser diretamente mapeado para seu valor binário de 4 bits, na mesma ordem. Por exemplo, para $2A_{16}$ temos que $2_{16} \rightarrow 0010_2$ e $A_{16} \rightarrow 1010_2$, portanto $2A_{16}\rightarrow 00101010_2$.

??? question "Dado um número não negativo qualquer na base hexadecimal, descreva o algoritmos para transformá-lo em um número binário."

    Como a base 16 é múltipla de 2, o processo manual é bem simples. Cada algarismo hexadecimal pode ser diretamente mapeado para seu valor binário de 4 bits, na mesma ordem. Por exemplo, para $2A_{16}$ temos que $2_{16} \rightarrow 0010_2$ e $A_{16} \rightarrow 1010_2$, portanto $2A_{16}\rightarrow 00101010_2$.

??? question "Dado um número não negativo qualquer na base decimal, descreva o algoritmos para transformá-lo em um número binário."

    Como a base 10 não é múltipla de 2, o processo manual é mais complicado que com as bases hexadecimal ou octal. Uma das abordagens é a de [divisões sucessivas](https://pt.wikipedia.org/wiki/Convers%C3%A3o_de_base_num%C3%A9rica#Convers%C3%A3o_de_decimal_para_bin%C3%A1rio), onde se divide o número por 2, anotando o valor do resto (necessariamente um algarismo binário). Esse processo é repetido para o resultado inteiro da divisão, até que haja um resultado da divisão que seja zero. Neste ponto, juntam-se os valores dos restos anotados e inverte-se a ordem deles - o resultado será representação do número decimal na base binária. Por exemplo: $13_{10} / 2 = 6$ (resto 1); $6_{10} / 2 = 3$ (resto 0); $3_{10} / 2 = 1$ (resto 1); $1_{10} / 2 = 0$ (resto 1). A sequência de restos é $1011$, invertida se torna $1101_2 = 1·2$^3$+ 1·2$^2$+ 1·2$^0$= 8 + 4 + 1$.

??? question "Dados os bits `11`, qual o valor inteiro armazenado considerando apenas o sistema posicional, sinal e magnitude, complemento de 1 e complemento de 2?"

    * Sistema posicional: $11_2 = 1·2$^1$+ 1·2$^0$= 2 + 1 = 3_{10}$
    * Sinal e magnitude:  $11_2 = -1_2 = -1·2$^0$= -1_{10}$
    * Complemento de um:  $11_2 = -1_2 \overset{inv}{\rightarrow} -0_2 = -0·2$^0$= -0_{10}$
    * Complemento de dois:  $11_2 = -1_2 \overset{inv}{\rightarrow} -0_2 \overset{+1}{\rightarrow} -1_2 = -1·2$^0$= -1_{10}$

??? question "Quais os 4 pontos principais definidos quando consideramos 8 bits para armazenar uma estrutura de dados do tipo `inteiro`?"

    1. O significado é de um valor numérico inteiro, que pode ser negativo.
    1. O valor é armazenado como Complemento de 2 nos 8 bits.
    1. Os possíveis valores armazenados estão no intervalo $[-2^7, 2^7) \equiv [-128, 128)$.
    1. As operações aritméticas básicas ($+, -, \times e \div$) estão definidas na linguagem de programação - e possivelmente outras.

??? question "Considerando 4 bits para armazenar um valor inteiro como complemento de 2, o que acontece computar a operação $5 + 4$?"

    Supondo 4 bits, os valores possíveis de serem armazenados são [-8, 7). Ao somar 4 (`0101`) e 4 (`0100`), o resultado seria 9 (`1001`). Entretanto, como a representação é de complemento de 2, `1001` é interpretado como -7, um resultado incorreto. O valor calculado ultrapassa a capacidade da representação (*overflow*), e o resultado não é o esperado.

??? question "Considerando 4 bits para armazenar um número real como ponto fixo, determine qual a representação do valor $1,25_{10}$ como $Q1.3$, $Q2.2$ e $Q3.1$. "

    * $Q1.3 \Rightarrow 1,25_{10} = 1\cdot2^0 + 0\cdot2^{-1} + 1\cdot2^{-2} + 0\cdot2^{-3} = 1010_2$
    * $Q2.2 \Rightarrow 1,25_{10} = 0\cdot2^1 + 1\cdot2^0 + 0\cdot2^{-1} + 1\cdot2^{-2} = 0101_2$
    * $Q3.1$ não é adequado para este valor. Tem-se duas possibilidades:
        * $1,25_{10} \approx 0\cdot2^2 + 0\cdot2^1 + 1\cdot2^0 + 0\cdot2^{-1} + 1\cdot2^{-2} = 0001_2 (=1,5_{10})$
        * $1,25_{10} \approx 0\cdot2^2 + 0\cdot2^1 + 1\cdot2^0 + 0\cdot2^{-1} + 0\cdot2^{-2} = 0010_2 (=1,0_{10})$

??? question "Se todo número inteiro também é um número real, por que as linguagens de programação oferecem o tipo de dado `int` quando existe o tipo de dado `float`?"

    A manipulação de um `float` é mais complexa que a de um `int`, e nos computadores antigos essa complexidade implicava em uma grande diferença de desempenho nas operações, principalmente aritméticas - era bem mais eficiente usar `int`. Nos computadores modernos, a situação é bem mais difusa e muito dependente dos detalhes de uso tanto do algoritmo quanto da linguagem de programação quanto do hardware.

??? question "Se todo número inteiro também é um número real, por que as linguagens de programação oferecem o tipo de dado `int` quando existe o tipo de dado `float`?"

    A manipulação de um `float`


[^1]: Exceto se você for um antigo romano...
