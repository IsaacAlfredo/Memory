# Memory
## Busca Linear vs Busca Binária

Para o trabalho, comparei o desempenho da busca linear e da busca binária em uma lista ordenada com 10.000.000 de números. 

Busca Linear: o algortimo percorre a lista sequencialmente, comparando o item da lista com o item que deve ser encontrado.
Busca Binária: o algoritmo percorre a lista visitando o item no meio. Caso esse elemento não seja o item que deve ser encontrado, visita alguma das metades à esquerda ou à direita (a depender do item buscado ser maior ou menor que o item ao meio) e repete o processo até encontrá-lo

Implementei as funções "linear_search" e "binary_search" para as respectivas buscas. A função search percorre a lista e retorna outra lista, onde o primeiro elemento é uma lista dos itens percorridos, o segundo é uma lista dos tempos de execução da busca por cada item e o último é a média desses tempos. 

Para compará-las, utilizei ambas as buscas em 3 situações diferentes:

1- buscando um item a cada 2.000.000 da lista, resultando em 5 observações, que foram utilizadas para gerar o gráfico de barras a seguir:
![newplot (5)](https://github.com/IsaacAlfredo/Memory/assets/60722914/abce57cb-ff78-40e4-be5c-82c2863c23e7)

No gráfico, o eixo X é a observação (ou seja, o número buscado) e o Y é o tempo de execução (em nanossegundos). 

Note que a diferença é tão grande que a barra da busca binária quase não aparece no gráfico. Felizmente, como os gráficos foram gerados pelo Plotly, conseguimos dar um zoom nele para tentar visualizar melhor:
![Screenshot_1](https://github.com/IsaacAlfredo/Memory/assets/60722914/b688587a-2ad3-4f04-af07-135143d10353)

2- Buscando um item a cada 10.0000 da lista, resultando em 1.000 observações, que foram utilizadas para gerar os gráficos de dispersão a seguir:
![newplot (2)](https://github.com/IsaacAlfredo/Memory/assets/60722914/9fdd6562-a2b6-40e1-8bfc-a47db7c9de2b)
![newplot (3)](https://github.com/IsaacAlfredo/Memory/assets/60722914/490681b6-0864-495f-80d7-fa244ef472ea)
Nesses gráficos, o eixo X é o tempo do execução, enquanto o Y é a observação (ou seja, o número buscado). A cor também é a observação, que foi utilizada para ajudar na visualização dos dados.

No gráfico da busca binária, podemos perceber que o tempo de execução é relativamente parecido do pior ao melhor caso, independente se o elemento estar no começo ou final da lista. O mesmo não vale para a busca linear, que tem como um grande problema essa disparidade onde o pior caso (último item da lista) demora muito para ser encontrado.

Nesse experimento, a média de tempo de execução do algoritmo da busca binária foi Xns, enquanto a busca linear foi Yns

3- Buscando um item a cada 100 da lista, resultando em 100.000 observações, que foram utilizadas para gerar os gráficos de dispersão a seguir:
![newplot](https://github.com/IsaacAlfredo/Memory/assets/60722914/365ea851-b663-47ea-b0bc-c78f01cfc697)
![newplot (4)](https://github.com/IsaacAlfredo/Memory/assets/60722914/c20f9657-fb8e-4274-9716-6c2a428ef3cd)
Os resultados foram praticamente o mesmo do experimento anterior, porém com mais amostras — embora alguns itens na busca linear tenham ficado "tortos", talvez por alguma influencia no ambiente durante a execução, porém não é algo que eu saiba controlar.

Por fim, podemos observar a média de tempo de execução entre cada uma das situações na imagem a seguir, bem como o tempo total das execuções, dado pela barra de progresso da biblioteca alive_progress:
![Screenshot_2](https://github.com/IsaacAlfredo/Memory/assets/60722914/66dcd543-696d-4b64-8c67-50e4a34141ad)

Podemos, mais uma vez, constatar a diferença grotesca no tempo de execução dos algoritmos. Tanto em tempo médio quanto em tempo total, é simplesmente absurdo a diferença de eficiência de ambos em uma lista ordenada.
