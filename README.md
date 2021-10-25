# Pontos próximos em PAA

Trabalho de Projeto e Análise de Algoritmos de pontos próximos

## Objetivos

- [ ] Criar uma solução O(n*log(n)) 
- [ ] Criar uma solução O(n*log(n)²)
- [ ] Criar uma solução O(n²) 

# Soluções:

### Divisão e conquista:

``` 
python3 divide_and_conquer.py
``` 

- Complexidade: O(n*log(n)²).

1) Encontre o ponto médio na matriz classificada, podemos tomar P [n / 2] como ponto médio.

2) Divida a matriz dada em duas metades. O primeiro subarray contém pontos de P [0] a P [n / 2]. O segundo subarray contém pontos de P [n / 2 + 1] a P [n-1].

3) Encontre recursivamente as menores distâncias em ambos os subarrays. Sejam as distâncias dl e dr. Encontre o mínimo de dl e dr. Seja o mínimo d.

5) Ordene a faixa da matriz [] de acordo com as coordenadas y. Esta etapa é O (nLogn). Ele pode ser otimizado para O (n) classificando e mesclando recursivamente.

4) A partir das 3 etapas acima, temos um limite superior d de distância mínima. Agora precisamos considerar os pares de forma que um ponto do par venha da metade esquerda e o outro da metade direita. Considere a linha vertical passando por P [n / 2] e encontre todos os pontos cuja coordenada x está mais próxima do que d da linha vertical do meio. Construa um array strip [] de todos esses pontos.

6) Encontre a menor distância na faixa []. Isso é complicado. À primeira vista, parece ser uma etapa O (n ^ 2), mas na verdade é O (n). Pode-se provar geometricamente que, para cada ponto da faixa, só precisamos verificar no máximo 7 pontos após ele (observe que a faixa é classificada de acordo com a coordenada Y).

7) Por fim, retorne o mínimo de d e a distância calculada na etapa acima (etapa 6)

### Força Bruta

``` 
python3 brute_force.py
```

- Complexidade: O(n²)

### Divisão e conquista (otimizado)
(ainda há fazer)
```
python3 dc_optimized.py
```

- Complexidade: O(n*log(n))

Este algoritmo é basicamente o algoritmo anterior, porém com a otimização no passo 5.

![comparison](img/comparison.jpg)


