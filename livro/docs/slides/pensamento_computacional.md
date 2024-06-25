---
template: reveal.html
---

# Pensamento Computacional

#### Algoritmos e Programação de Computadores

---

> Não podemos resolver um problema usando o mesmo tipo de pensamento que usamos quando os criamos.

**Albert Einstein**

![Albert Einstein](images/slides/people/einstein.png "Albert Einstein") <!-- .element width="15%" -->

---

## Pensamento Computacional

Processos de pensamento envolvidos em:
* formular problemas, e
* formular soluções realizáveis.

--

1. Descrever o problema.
1. Dividir o problema em uma sequência lógica de pequenas tarefas.
1. Identificar os detalhes relevantes para a solução.
1. Elaborar um processo de resolução de cada tarefa (algoritmo).
1. Avaliar este processo.

---

## Decomposição

Redefinição do problema como partes menores e mais fáceis (ou possíveis) de se lidar.

--

**Faça um bolo.**
1. Junte os ingredientes. <!-- .element: class="fragment" data-fragment-index="1" -->
1. Misture. <!-- .element: class="fragment" data-fragment-index="1" -->
1. Unte a forma. <!-- .element: class="fragment" data-fragment-index="1" -->
1. Despeje a massa na forma. <!-- .element: class="fragment" data-fragment-index="1" -->

---

## Reconhecimento de Padrões

Perceber similaridades entre problema (ou partes) para criar uma solução adequada à classe do problema ( e não só a uma ocorrência).

--

#### Números Primos <!-- .element: class="fragment" data-fragment-index="1" -->

2, 3, 5, 7, 11, ...

..., 13, 17, 19 <!-- .element: class="fragment" data-fragment-index="1" -->

--

### Generalização de Padrões

Criar modelos/regras/princípios genéricos a partir de padrões observados em instâncias específicas do problema.

--

#### par + 1 = ímpar <!-- .element: class="fragment" -->


`0 + 1   = 1`

`2 + 1   = 3`

`4 + 1   = 5`

`     ⋮`

---

## Abstração

Identificar e focar nos aspectos fundamentais do problema, ignorando as especificidades.

--

###### Realidade → Abstração

![UnB "Real"](images/unb_mapa.png "Mapa da UnB") <!-- .element width="40%" --> ![Abstração do mapa da UnB](images/unb_modelo.png "Abstração do mapa da UnB") <!-- .element width="40%" -->

---

## Pensamento Algorítmico

Processo de criar algoritmos (como soluções).

> Um algoritmo é a descrição dos passos para realizar uma tarefa.

--

> Se tiver um mapa e os pontos de origem e destino, posso decompor o trajeto entre eles em trechos menores e definir rotas entre eles, e depois juntá-las numa rota final. Posso usar este processo para traçar uma rota entre quaisquer origem/destino!

--

### Automação

Uso de mecanismos para realização de um algoritmo.

--

!["Braço robótico"](images/slides/manufacturing.png "Braço robótico") <!-- .element width="20%" -->

Produção, produtividade, eficiência, uniformidade, qualidade, liberação de recurso humano, etc.

--

### Avaliação

Dentre as possíveis soluções, considere:
- Qual a mais adequada?
- Em que contextos ela funciona (ou não)?
- Como é seu desempenho?

--

#### Encontrar a página P em um livro

😫 Feche os olhos.<!-- .element: class="fragment" -->

😐 Enquanto não encontrar a página P, escolha uma página qualquer.<!-- .element: class="fragment" -->

😌 Escolha a 1a página. Enquanto a escolhida não for P, escolha a página seguinte.<!-- .element: class="fragment" -->

😀 Escolha a página do meio. Se for P, pare. Se for maior que P, descarte-a e todas as páginas anteriores. Caso contrário, descarte-a e todas as posteriores. Repita este processo.<!-- .element: class="fragment" -->

---

## Resumo

* **Pensamento computacional** visa formular soluções para problemas para que possam ser realizadas por um agente.
* Envolve conceitos de  **decomposição**, **abstração**, **reconhecimento de padrões**, **pensamento algorítmico** e **avaliação**.
