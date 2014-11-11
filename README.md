Autor: Christian M. T. Takagi
Disciplina: Laboratório de Programação II       
Prof. Alfredo Goldman
Mini EP 5
Arquivo: README.md



1. Introdução
--------------------------------------------------------------------------------
Esse programa utiliza-se do pacote PLY para a análise léxica e sintática das
entradas do programa, como diz no enunciado.

Não passaremos instruções sobre a instalação do PLY, que é a única dependência,
pois ela é mencionada do enunciado. Também não mencionaremos mais o uso do
unittest, já que este pacote vêm sido utilizado desde que pedido no curso.

Não há outras dependências externas.



2. Execução
--------------------------------------------------------------------------------
Para executar o programa, utilize o comando

    $ python3 miniep5.py

Quando surgir o console interativo, digite a expressão em notação posfixa, e.g.

    calc > 3 (-2) (-2) + +

Observe o uso de parênteses para explicitar o uso de números negativos.
Nesse caso, poderíamos reescrever a expressão sem o uso do parêntese, tomando
as devidas precauções:

    calc > -2 -2 + 3 +

Porém, para expressões mais complexas, recomendamos o uso de parênteses para
evitar possíveis erros de interpretação.



3. Dificuldades
--------------------------------------------------------------------------------
A única dificuldade foi em tratar os números negativos, já que se não escrito
corretamente, ele irá identificar o sinal de negativo como um operando de
subtração, tornando um ou mais operandos obsoletos e, assim, gerando um erro
de sintaxe. O problema foi resolvido utilizando parênteses.



4. Testes
--------------------------------------------------------------------------------
Como o programa é uma calculadora, os testes foram comparações com valores
fixos. A única exceção ficou para o caso de números negativos, onde precisamos
verificar o caso mencionado no item acima (3. Dificuldades)
