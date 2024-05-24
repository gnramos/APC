# Computadores

!!! quote "[Joe Sondow](https://www.linkedin.com/in/joesondow)"

    *Um computador é como um gênio travesso. Te dá exatamente o que você pede dele, mas nem sempre o que você quer.*

---

*<img style="height:20px!important;margin-left:3px;display:inline-block;vertical-align:middle;" src="https://img.shields.io/badge/TODO-Introdução-red">*

---

A humanidade é engenhosa, e sempre buscou criar e aprimorar ferramentas para auxiliar nas realização de tarefas. Assim como o fogo e a roda, o computador é uma ferramenta que revolucionou o mundo, e hoje em dia é difícil encontrar algum tipo de atividade que não seja (ou possa ser) auxiliada por esta máquina que substituiu pessoas no esforço de processar dados e transformá-los em resultados. A [história da computação](https://pt.wikipedia.org/wiki/Hist%C3%B3ria_da_computa%C3%A7%C3%A3o) é antiga e está entrelaçada com as histórias dos [números](http://pt.wikipedia.org/wiki/N%C3%BAmero#Hist.C3.B3ria_dos_n.C3.BAmeros), do [hardware](http://pt.wikipedia.org/wiki/Hardware#Hist.C3.B3ria_do_Hardware), de [algoritmos](http://pt.wikipedia.org/wiki/Algoritmo) e [lógica](http://pt.wikipedia.org/wiki/L%C3%B3gica_matem%C3%A1tica), e da [programação](http://pt.wikipedia.org/wiki/Linguagem_de_programa%C3%A7%C3%A3o#Hist.C3.B3ria)

De forma simplificada, um computador é uma máquina que:

1. realiza cálculos [simples] rapidamente;
1. lembra de [muitos] resultados.

Um "cálculo" é a execução de uma operação primitiva pela máquina, e um "resultado" é uma informação resultante desta operação ou já conhecida. A *computação*, portanto, lida basicamente com dois elementos, as informações sendo manipuladas (*dados*) e as regras de manipulação delas (*procedimentos*)[@Abelson1996]. São tantas as aplicações e possibilidades que criou-se uma nova área de conhecimento: a *Ciência da Computação*, que estuda a fundamentação teórica das construções computacionais, bem como suas aplicações em dispositivos tecnológicos e sistemas de computação[@SBC2005].

A computação é muito abrangente, envolvendo diversas outras (lógica, matemática, etc.) e, apesar de não ser necessariamente focada nela, está intrinsecamente associada a uma ferramenta: *o computador*. Ao descrever soluções como procedimentos que manipulam (corretamente) dados, pode-se usar esta máquina para resolver inúmeros problemas.

A aplicação do pensamento computacional resulta em soluções representadas como etapas computacionais e algoritmos para execução pelo computador, focando nos dois elementos básicos: conhecimento *descritivo* (o que?) e, principalmente, *procedural* (como?). Por exemplo, resolver o problema "qual a raiz quadrada de um número $n$?" a solução deve definir um processo que encontre um valor $r$ tal que $r^2 = n$, que é um conhecimento descritivo. Uma abordagem é o método babilônico:

``` linguagem-natural title="Método Babilônico"
Inicie com um número positivo arbitrário r
Enquanto r² não for suficientemente próximo a n:
    Atualize o valor de r para a média entre r e n/r.
```

Considerando $n = 144$, uma estimativa inicial $r = 1$ e que "suficientemente próximo" signifique que $|n - r^2| \leq 0,5$, a aplicação das instruções acima resultam na construção da seguinte sequência de valores para $r$: 1, 72.5, 37.24, 20.55, 13.8 e, finalmente, 12.1. Uma descrição mais precisa destes algoritmo permite que o computador realize este processo mecânico para chegar à solução desejada. Para lidar com problemas diferentes, basta fornecer grupos diferentes de instruções!

!!! warning

    O computador interpreta as instruções no sentido de recebê-las em uma representação específica e traduzi-las em sua operações primitivas para execução, não no sentido de dar-lhes sentido para obter o resultado desejado. *Ele faz o que você manda, não o que você quer*.

Entender mais sobre esta máquina e como ela funciona é essencial para usá-la na resolução de problemas. O computador, além de processar e armazenar os dados, também precisa movimentá-los entre os dispositivos e controlar toda essa manipulação. Para tanto, é preciso que diversos componentes elétricos, eletrônicos e eletromecânicos (hardware) trabalhem em conjunto para realizar os processos definidos no algoritmo (software).

{! computadores/arquitetura.md. !}

{! computadores/hardware.md. !}

{! computadores/software.md. !}

<h2>Resumo</h2>

<img style="height:20px!important;margin-left:3px;display:inline-block;vertical-align:middle;" src="https://img.shields.io/badge/TODO-Resumo-red">

??? llm

    * Explique a arquitetura Von Neumann.
    * O que é hardware em um computador?
    * O que é software?
    * Explique os níveis de memória de um computador.
    * Explique as camadas de software de um computador.
    * Explique o conceito de linguagem de programação

{! computadores/exercicios.md. !}
