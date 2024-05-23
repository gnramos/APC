# Fluxo de Controle

!!! quote "[](http://www)"

    <img style="height:20px!important;margin-left:3px;display:inline-block;vertical-align:middle;" src="https://img.shields.io/badge/TODO-Quote-red">

---

*<img style="height:20px!important;margin-left:3px;display:inline-block;vertical-align:middle;" src="https://img.shields.io/badge/TODO-Introdução-red">*

---

## Sequencial

# Funções

!!! quote "[Joe Sondow](https://www.linkedin.com/in/joesondow)"

    *Um computador é como um gênio travesso. Te dá exatamente o que você pede dele, mas nem sempre o que você quer.*


Programas de computadores geralmente usam procedimentos que especificam como fazer algo[@Cormen2013]. Nas linguagens de programação, estes são chamados de funções (ou métodos), e são chamados para serem executados. Ao chamar um procedimento, pode-se fornecer informações necessárias para a computação ao definir parâmetros, e receber (ou não) resultados como um valor de retorno.

## Condicional

exemplo do imc (implicações matemáticas de se não é < x, necessariamente é >= x)

``` python title="Índice de Massa Corporal"
--8<-- "imc.py:5:16"
```

O uso de condicionais é baseado no valores booleanos $verdadeiro$ e $falso$. Estes são os valores verdade da lógica matemática, e indicam o grau de verdade de uma proposição. Por exemplo, considerando os números inteiros 42 e 100, podemos a propor que $42 < 100$ e verificar que isto é verdadeiro.
As linguagens de programação podem oferecer um tipo de dado específico para estes valores ou interpretar outros tipos de dados como um dos dois resultados possíveis. Por exemplo, a linguagem C não tem um tipo primitivo e interpreta o valor numérico zero como o valor booleano $falso$, e qualquer valor diferente disso como $verdadeiro$. Já Python tem o tipo [bool](https://docs.python.org/pt-br/3/c-api/bool.html), mas também interpreta uma série de outros tipos de dados.

`<expr>` é uma expressão cujo valor resultante tem um significado booleano, ou seja, é **verdadeiro** ou **falso**.

Se `<expr>` é **verdadeiro** ("truthy"), então `<instr>` é executada; caso contrário, `<instr>` é ignorada.

=== "Python"

    ``` python title="Estrutura condicional"
    if <expr>:
    	<instr>
    ```

=== "C"

    ``` C title="Estrutura condicional"
    if (<expr>) {
    	<instr>;
    }
    ```

## Repetição

<h2>Resumo</h2>

<img style="height:20px!important;margin-left:3px;display:inline-block;vertical-align:middle;" src="https://img.shields.io/badge/TODO-Resumo-red">

??? llm "Chat-bot Fluxo de Controle"

    * O que é o fluxo de controle de um programa?

??? llm "Chat-bot Funções"

    * O que é uma função em programação?
    * Quais as vantagens de usar funções em um programa?
    * O que é o escopo de uma função?
    * Quais os componentes de uma função em Python?
    * Quais as funções mais úteis em Python?
    * O que são módulos em Python?

??? llm "Chat-bot Condicionais"

    * Explique a estrutura condicional no fluxo de controle de um programa.
    * Explique os operadores lógicos em Python.
    * Como portas lógicas compõem uma CPU?
    * O que é curto-circuito em Python?

??? llm "Chat-bot Repetição"

    * Explique as estruturas de repetição no fluxo de controle de um programa.
    * Quais as diferenças entre while e for em Python?
    * Dê um exemplo de código em que while seja preferível ao for.
    * Dê um exemplo de código em que for seja preferível ao while


<h2>Exercícios</h2>

??? question "Implemente o código que leia a quantidade máxima N de elefantes e apresente a letra da música até que N (≥1) elefantes incomodem muita gente. Por exemplo, para N = 4: **1 elefante incomoda muita gente... 2 elefantes incomodam, incomodam muito mais! 2 elefantes incomodam muita gente... 3 elefantes incomodam, incomodam, incomodam muito mais! 3 elefantes incomodam muita gente... 4 elefantes incomodam, incomodam, incomodam, incomodam muito mais!**"

    Uma possível solução é:
    ```python title="Elefantes"
    --8<-- "exercicios/programacao/fluxo_de_controle/repeticao/elefantes.py:14"
    ```

??? question "Considerando um comprimento *L*, implemente o código que desenha um quadrado de lado *L*."

    Uma possível solução é:
    ```python title="Quadrado"
    --8<-- "exercicios/programacao/fluxo_de_controle/repeticao/quadrado.py:10:15"
    ```