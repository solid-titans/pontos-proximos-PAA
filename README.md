# Pontos próximos em PAA

Trabalho de Projeto e Análise de Algoritmos de pontos próximos

## Objetivos

- [ ] Criar uma solução O(n*log(n)) 
- [ ] Criar uma solução O(n*log(n)²)
- [ ] Criar uma solução O(n²) 

# Soluções:

### Divisão e conquista:

- Complexidade: O(n*log(n)²).

- Entrada: Uma matriz de n pontos P []

- Saída: a menor distância entre dois pontos em uma determinada matriz.

- Como uma etapa de pré-processamento, a matriz de entrada é classificada de acordo com as coordenadas x.
1) Encontre o ponto médio na matriz classificada, podemos tomar P [n / 2] como ponto médio.
2) Divida a matriz dada em duas metades. O primeiro subarray contém pontos de P [0] a P [n / 2]. O segundo subarray contém pontos de P [n / 2 + 1] a P [n-1].
3) Encontre recursivamente as menores distâncias em ambos os subarrays. Sejam as distâncias dl e dr. Encontre o mínimo de dl e dr. Seja o mínimo d.

![comparison](img/comparison.jpg)
