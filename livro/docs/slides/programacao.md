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

| Animal | Humana       | Programação |
| ------ | ------------ | ----------- |
| 👁      | Português    | Python |
| 👋      | English      | C / C++ |
| 👃      | 日本語 | Assembly |
| 👂      | اللغة العربية  | Haskell |
| 🗲      | русский язык | LISP    |

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

## Linguagem de Baixo Nível

Usam instruções mnemônicas para tentar facilitar a programação.

--

## Linguagem de Alto Nível

Usa um vocabulário mais rico para facilitar programação.

--

### Código Binário

```
<!-- { ! assets/src/ola_mundo.bin ! } -->
```

--

### Assembly

```
{! assets/src/ola_mundo.asm !}
```

--

### C

```
{! assets/src/ola_mundo.c !}
```

---

## Python

* Fácil de aprender
* Gratuita e de código livre
* Linguagem de alto nível​
* Interpretada​
* Portabilidade​

--

![UnB "Real"](slides/img/python_os.svg)<!-- .element width="75%" -->

--

```bash
Python 3.8.10 (default, Nov 22 2023, 10:22:35)
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

---

## Instruções

Unidades válidas de código.

--

## Expressões

Uma expressão é uma instrução que resulta em um **valor**.

--

```Python
>>> 2       # Expressão
2
>>> 2 + 40  # Expressão
42
>>> x = 2 + 3 / 5  # Instrução
>>>
```

---

## Python com números

```Python
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

```Python
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

```Python
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

```Python
>>> 42
42
>>> 3.14
3.14
>>> "Estou sendo oprimido!"
'Estou sendo oprimido!'
```

--

É possível armazenar um valor na memória associando-o a um nome.​

```Python
>>> resposta_do_universo = 42
>>> pi = 3.14
>>> status = "Estou sendo oprimido!"
```

--

É possível acessar um valor na memória pelo nome associado.​

```Python
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

```Python
>>> resposta_do_universo = 0
>>> resposta_do_universo
0
>>> resposta_do_universo = pi
>>> resposta_do_universo
3.14
```

--

## Variáveis

O **identificador** associado a cada valor faz muita diferença no entendimento do programa.

```Python
>>> salario = salario * bonus
>>> gastos = eletricidade + gas + internet + mercado
>>> f'Sobrou R${salario - gastos}!'
```

--

## Variáveis

O **identificador** associado a cada valor faz muita diferença no entendimento do programa.

```Python
>>> xwer87623 = 1000
>>> xwer87623 = xwer87623 * xwer37623
>>> xwer87632 = xwer37638 + xwer37623 + xwer87234 + xwer87888
>>> f'Sobrou R${xwer87623 - xwer87632}!'
```

---

## Atribuição ≠ Igualdade​

A expressão `x = 42` significa "atribua o valor 42 à variável x", e não "x é igual a 42".

```Python
>>> x = 42
>>> x
42
>>> 42 = x
  File "<stdin>", line 1
SyntaxError: cannot assign to literal
```

---

## Tipos de Valores

Cada valor representa uma informação, cujo significado depende do seu **tipo**.

<div style="font-family:Cinzel;font-size:15vw;color:#00822E;color:#000000;">X</div>

---

## Tipos de Valores

```Python
>>> type(42)
<class 'int'>
>>> type(3.14)
<class 'float'>
>>> type('Ni!')
<class 'str'>
```

--

## Tipos de Valores

```Python
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

```Python
21 vezes 2
  File "<stdin>", line 1
    21 vezes 2
       ^
SyntaxError: invalid syntax
```

---

## Erros de Semântica

Causados por uma instrução válida mas em um contexto logicamente incorreto.

```Python
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
