# Roteirização de Entregas

**Número da Lista**: 3<br>
**Conteúdo da Disciplina**: Greed<br>

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 20/0013181  |  Adne Moretti Moreira |
| 20/0018205  |  Gabriel Moretti de Souza |

## Sobre
O objetivo deste projeto é criar um sistema de roteirização de entregas inteligente e eficiente para uma empresa de logística.

O projeto é baseado nas informações de uma só entrega, significando que os produtos que não podem ser entregues naquela leva de caminhões irão apenas ficar para trás.

O sistema recebe como entrada informações sobre:
- Produtos a serem entregues, junto a seus pesos, prioridades e valores;
- Caminhões a serem utilizados para a entrega dos produtos, com sua capacidade e autonomia;
- A distância a ser percorrida pelos caminhões, com o número de postos de combustível disponíveis a eles;
- O valor que o cliente irá pagar para cada caminhão.

Com base nessas informações, o sistema calcula a rota mais eficiente para os caminhões da empresa, levando em consideração as capacidades de carga dos veículos, a distância a serem percorridas e a prioridade de entrega dos produtos.

Por exemplo, para otimizar as entregas, o primeiro caminhão a sair será sempre o de maior autonomia para evitar viagens perdidas, e sempre possuindo os produtos de maior prioridade que caibam em sua capacidade. Produtos de prioridades iguais são avaliados por seu valor específico maior (valor por unidade).

É importante citar que os produtos devem ser divisíveis para a ideia do projeto, como trigo, parafusos ou carne, podendo ser divididos entre os caminhões sem problema. 

## Screenshots
Adicione 3 ou mais screenshots do projeto em funcionamento.

## Vídeo

[]()

## Instalação 
**Linguagem**: Python<br>
**Framework**: --<br>

Para rodar o projeto basta rodar o arquivo python com o comando: 

```python main.py```

ou

```python3 main.py```

E iniciar inserindo os seus valores. 

## Uso
O programa é baseado nas informações de uma só entrega, significando que os produtos que não podem ser entregues naquela leva de caminhões irão apenas ficar para trás.

O sistema recebe como entrada informações sobre:
- Produtos a serem entregues, com seu nome, seu peso, prioridade e valor;
- Caminhões a serem utilizados para a entrega dos produtos, com sua capacidade e autonomia;
- A distância a ser percorrida pelos caminhões, com o número de postos de combustível disponíveis a eles;
- O valor que o cliente irá pagar para cada caminhão.

Com base nessas informações, o sistema calcula a rota mais eficiente para os caminhões da empresa, levando em consideração as capacidades de carga dos veículos, a distância a serem percorridas e a prioridade de entrega dos produtos.

Levando isso em conta, o programa apresenta todas as informações de cada caminhão da entrega, com seus produtos, a quilometragem dos postos que o caminhão deverá passar para maior eficiência de sua autonomia, e seu troco recebido (com a quantidade de notas ou moedas).

Caso existam, o programa também retorna os produtos restantes, que não puderam ser levados por nenhum dos caminhões naquela entrega.