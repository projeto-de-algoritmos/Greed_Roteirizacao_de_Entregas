import heapq
import math

# Classe para representar os produtos
#   Nome: nome do produto
#   Peso: peso do produto em kg
#   Valor: valor do produto em reais
#   Prioridade: taxa de prioridade do produto de 1 a 100
class Produto:
    def __init__(self, nome, peso, valor, prioridade):
        self.nome = nome
        self.peso = peso
        self.valor = valor
        self.prioridade = prioridade

# Classe para representar os caminhões
#   Capacidade: capacidade de carga do caminhão
#   Aproveitamento: distância máxima percorrida com o caminhão de tanque cheio
#   Produtos: produtos que estão sendo levados pelo caminhão
class Caminhao:
    def __init__(self, capacidade, aproveitamento):
        self.capacidade = capacidade
        self.aproveitamento = aproveitamento
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

# Algoritmo da mochila (Knapsack)
#   Recebe todos os caminhões e produtos e calcula quais caminhões irão levar quais produtos,
#    baseado principalmente em suas prioridades e valores. O que não couber no primeiro caminhão
#    será colocado no segundo, e assim por diante. Caso não seja possível colocar todos os produtos
#    em todos os caminhões, irá continuar no vetor de produtos.
def knapsack(caminhoes, produtos):
    tabela = [[0] * (len(produtos) + 1) for _ in range(len(caminhoes) + 1)]

    for i in range(1, len(caminhoes) + 1):
        for j in range(1, len(produtos) + 1):
            produto = produtos[j - 1]
            if produto.peso > caminhoes[i - 1].capacidade:
                tabela[i][j] = tabela[i - 1][j]
            else:
                valor_incluido = produto.prioridade + tabela[i - 1][j - 1]
                valor_excluido = tabela[i - 1][j]
                tabela[i][j] = max(valor_incluido, valor_excluido)

    return tabela[len(caminhoes)][len(produtos)]

# Algoritmo da Moeda
#   Recebe o troco que deverá ser entregue ao cliente e quais notas estão disponíveis, irá
#    calcular a melhor forma de dividir o troco pelas notas, com a menor quantidade de notas.
def encontrar_notas(troco, notas):
    notas.sort(reverse=True)
    quantidade_notas = [0] * len(notas)

    for i in range(len(notas)):
        quantidade = troco // notas[i]
        quantidade_notas[i] = quantidade
        troco -= quantidade * notas[i]

    return quantidade_notas

# Algoritmo do Caminhoneiro
#   Recebe o endereco da entrega e todos os caminhoes, calcula a menor quantidade de vezes que
#    cada caminhão precisará abastecer.
def calcular_rota(enderecos):
    # Simulação de distâncias entre os endereços
    # Substitua essa parte com uma biblioteca de mapas
    # distancia_entre_enderecos = {
    #     ('Endereco1', 'Endereco2'): 10,
    #     ('Endereco1', 'Endereco3'): 15,
    #     ('Endereco2', 'Endereco3'): 12,
    #     # Adicione outras distâncias aqui
    # }

    # # Função heurística para estimar o custo do caminho restante
    # def estimativa(endereco_atual, endereco_destino):
    #     if (endereco_atual, endereco_destino) in distancia_entre_enderecos:
    #         return distancia_entre_enderecos[(endereco_atual, endereco_destino)]
    #     else:
    #         return math.inf

    # fila_prioridade = []
    # heapq.heappush(fila_prioridade, (0, enderecos[0]))
    # visitados = set()
    # distancias = {endereco: math.inf for endereco in enderecos}
    # distancias[enderecos[0]] = 0

    # while fila_prioridade:
    #     distancia_atual, endereco_atual = heapq.heappop(fila_prioridade)
    #     visitados.add(endereco_atual)

    #     if endereco_atual == enderecos[-1]:
    #         break

    #     for vizinho in enderecos:
    #         if vizinho != endereco_atual and vizinho not in visitados:
    #             distancia = distancia_entre_enderecos.get((endereco_atual, vizinho), math.inf)
    #             novo_custo = distancias[endereco_atual] + distancia
    #             if novo_custo < distancias[vizinho]:
    #                 distancias[vizinho] = novo_custo
    #                 estimativa_custo = novo_custo + estimativa(vizinho, enderecos[-1])
    #                 heapq.heappush(fila_prioridade, (estimativa_custo, vizinho))
    # return distancias[enderecos[-1]]
    return x

# Função principal
#   O usuário insere a quantidades e dados dos caminhões, produtos, pagamento do cliente e
#    a distância a ser percorrida, retorna os dados da entrega.
def main():
    # Dados de exemplo
    caminhao1 = Caminhao(50)
    caminhao2 = Caminhao(70)

    # Nome do produto, quantidade, valor, prioridade.
    produtos = [
        Produto('Trigo', 10, 5, 15),
        Produto('Parafuso', 20, 8, 5),
        Produto('Lã', 15, 6, 10),
        Produto('Carne', 30, 10, 20),
    ]

    caminhoes = [caminhao1, caminhao2]

    # Algoritmo do Knapsack
    for produto in produtos:
        max_valor = knapsack(caminhoes, [produto])
        caminhao = caminhoes[max_valor - 1]
        caminhao.adicionar_produto(produto)

    # Algoritmo da Moeda
    troco = 100
    notas = [50, 20, 10, 5, 1]
    quantidade_notas = encontrar_notas(troco, notas)
    print("Quantidade de notas:", quantidade_notas)

    # Algoritmo do Caminhoneiro
    endereco = 1
    menor_distancia = calcular_rota(endereco)
    print("Menor distância:", menor_distancia)

if __name__ == '__main__':
    main()
