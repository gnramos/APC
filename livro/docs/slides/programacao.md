---
template: reveal.html
---

# Programação

#### Algoritmos e Programação de Computadores

---

## Programação

Processo de expressar um algoritmo como instruções em uma linguagem de programação.

--

> Programação de computadores é muito divertida. Como música, é uma habilidade originada em um talento desconhecido e prática constante.

**Larry O’Brien & Bruce Eckel**

---

### Linguagens

| Animal | Humana <!-- .element: class="fragment" data-fragment-index="1" --> | Programação <!-- .element: class="fragment" data-fragment-index="2" --> |
|:------:|:------------:|:-----------:|
| 👁      | Português <!-- .element: class="fragment" data-fragment-index="1" -->    | Python <!-- .element: class="fragment" data-fragment-index="2" --> |
| 👋      | English <!-- .element: class="fragment" data-fragment-index="1" -->      | C / C++ <!-- .element: class="fragment" data-fragment-index="2" --> |
| 👃      | 日本語 <!-- .element: class="fragment" data-fragment-index="1" --> | Assembly <!-- .element: class="fragment" data-fragment-index="2" --> |
| 👂      | اَلْعَرَبِيَّةُ <!-- .element: class="fragment" data-fragment-index="1" --> ا  | Haskell <!-- .element: class="fragment" data-fragment-index="2" --> |
| 🗲      | русский язык <!-- .element: class="fragment" data-fragment-index="1" --> | LISP <!-- .element: class="fragment" data-fragment-index="2" -->    |

--

## Linguagem de Programação

* Vocabulário
* Gramática:
  * regras sintáticas
  * regras semânticas

--

### Código-Fonte

Um algoritmo expresso como instruções para o computador.

--

## Linguagem de Máquina

Aquela que o hardware [específico] entende (código binário).

--

### Código Binário

```bash
0111 1111 0100 0101 0100 1100 0100 0110
0000 0010 0000 0001 0000 0001 0000 0000
0000 0000 0000 0000 0000 0000 0000 0000
0000 0000 0000 0000 0000 0000 0000 0000
0000 0010 0000 0000 0011 1110 0000 0000
0000 0001 0000 0000 0000 0000 0000 0000
0100 0000 0000 0100 0100 0000 0000 0000
0000 0000 0000 0000 0000 0000 0000 0000
(continua por mais 2120 linhas)
```

--

## Linguagem de Baixo Nível

Usam instruções mnemônicas para tentar facilitar a programação.

--

### Assembly

```
{! ../assets/src/ola_mundo.asm !}
```

--

## Linguagem de Alto Nível

Usa um vocabulário mais rico para facilitar programação.

--

### C

```C
{! ../assets/src/ola_mundo.c !}
```

### Python <!-- .element: class="fragment" data-fragment-index="2" -->

```
{! ../assets/src/ola_mundo.py !}
```
<!-- .element: class="fragment" data-fragment-index="2" -->

---

![Python](slides/images/python-logo-generic.svg "Python") <!-- .element width="50%" -->

--

## Python

* Fácil de aprender
* Gratuita e de código livre
* Linguagem de alto nível​
* Interpretada​
* Portabilidade​

--

![UnB 'Real'](slides/images/python_os.svg) <!-- .element width="50%" -->

--

## Interpretador Python

```python
Python 3.8.10 (default, Nov 22 2023, 10:22:35)
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

---

## Instruções

Unidades válidas de código-fonte.

*(que **realizam** algo)*

<br>

```python
linguagem = 'Python'
```

--

## Expressões

Instruções que resultam em um **valor**.

*(que **são** algo)*

```python
>>> 2 + 40
42
```

```python
>>> ((16 - 1) + (12 / 2)) * 2
42.0
```
<!-- .element: class="fragment" -->

--

## Python com números

<br>


```python
>>> 2 + 2
4
>>> 50 - 5 * 6
20
>>> (50 - 5 * 6) / 4
5.0
>>> 8 / 5
1.6
```

--

## Python com números

<br>


```python
>>> 17 / 3
5.666666666666667
>>> 17 // 3
5
>>> 17 % 3
2
>>> 5 * 3 + 2
17
```

--

## Python com texto

<br>


```python
>>> ' Ni! '  # aspas simples
' Ni! '
>>>
>>> "Estou sendo oprimido!"  # aspas duplas
'Estou sendo oprimido!'
>>>
>>> 'É "só" um arranhão...'  # ambas
'É "só" um arranhão...'
```

---

## Constantes

Valores fixos, como números ou símbolos, que não são alterados ao longo da execução do programa.

<br>


```python
>>> 42
42
>>> 3.14
3.14
>>> "Estou sendo oprimido!"
'Estou sendo oprimido!'
```

--

É possível armazenar um valor na memória associando-o a um ~nome~ *identificador* único.​

<br>


```python
>>> resposta_do_universo = 42
>>> pi = 3.14
>>> status = "Estou sendo oprimido!"
```

--

É possível acessar um valor armazenado na memória pelo identificador associado.​

<br>


```python
>>> resposta_do_universo
42
>>> pi
3.14
>>> status
'Estou sendo oprimido!'
```

---

## Variáveis

É possível alterar valores armazenados.​

<br>


```python
>>> resposta_do_universo = pi
>>> resposta_do_universo
3.14
```

--

## Variáveis

O **identificador** associado a cada valor faz muita diferença no entendimento do programa.

```python
>>> xou87623 = xou87623 * xou37623
>>> xou87632 = xou37638 + xou37623 + xou87234 + xou87888
>>> f'Sobrou R${xou87623 - xou87632}!'
```

--

## Variáveis

O **identificador** associado a cada valor faz muita diferença no entendimento do programa.

```python
>>> salario = salario * bonus
>>> gastos = eletricidade + gas + internet + mercado
>>> f'Sobrou R${salario - gastos}!'
```

---

## Atribuição ≠ Igualdade​

A instrução `x = 42` significa "atribua o valor 42 à variável x", e não "x é igual a 42".

```python
>>> x = 42
>>> 42 = x
  File "<stdin>", line 1
SyntaxError: cannot assign to literal
```

---

## Tipos de Valores

Cada valor representa uma informação, cujo significado depende do seu **tipo**.

X <!-- .element style="font-family:Cinzel;font-size:15vw;color:#565656;" -->

---

## Tipos de Valores

<br>

```python
>>> type(42)
<class 'int'>
>>> type(3.14)
<class 'float'>
>>> type('Ni!')
<class 'str'>
```

--

## Tipos de Valores

<br>

```python
>>> type(1)
<class 'int'>
>>> type(1.0)
<class 'float'>
>>> type('1')
<class 'str'>
>>> type('1.0')
<class 'str'>
```

---

## Erros de Sintaxe

Causados por uma instrução inválida.

<br>

```python
21 vezes 2
  File "<stdin>", line 1
    21 vezes 2
       ^
SyntaxError: invalid syntax
```

---

## Erros de Semântica

Causados por uma instrução válida mas em um contexto logicamente incorreto.

<br>

```python
42 / 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
```

---

## Programa

Representação de um algoritmo como código-fonte.

>  **Algoritmo**: sequência finita de instruções bem definidas e não ambíguas para executar uma tarefa.

--

## Fluxo de Controle

Determina a ordem em que são executadas as instruções.

1. Sequencial
1. Condicional
1. Repetição

--

## Fluxo Sequencial

As instruções são executadas uma após a outra, na mesma ordem em que se encontram na representação.

> Necessário para garantir a corretude dos algoritmos.

--

* Bata as claras em neve.
* Reserve.
* Bata bem as gemas com a margarina e o açúcar.
* Acrescente o leite e a farinha aos poucos sem parar de bater. Por último agregue as claras em neve e o fermento.
* Coloque em forma grande de furo central untada e enfarinhada.
* Asse em forno médio, pré-aquecido, por aproximadamente 40 min.
* Quando espetar um palito e sair limpo estará assado.

---

## Resumo

* **Programação:** codificação do algoritmo.
* **Instrução:** unidade válida de código.
* **Expressão:** instrução que resulta em um valor.
* **Tipo de dado:** definição de como armazenar/processar um valor armazenado na memória​.
* **Variável:** nome de um valor armazenado na memória.
* As instruções de um algoritmo são executadas de forma **sequencial**.
