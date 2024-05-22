# Condicional

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
