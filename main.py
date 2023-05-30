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
    def __init__(self, capacidade, autonomia):
        self.capacidade = capacidade
        self.autonomia = autonomia
        self.produtos = []
        self.valor_total = 0

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

# Algoritmo da mochila (Knapsack)
#   Recebe todos os caminhões e produtos e calcula quais caminhões irão levar quais produtos,
#    baseado principalmente em suas prioridades e valores. O que não couber no primeiro caminhão
#    será colocado no segundo, e assim por diante. Caso não seja possível colocar todos os produtos
#    em todos os caminhões, irá continuar no vetor de produtos.
#   Obs: A função nativa do python, o "sorted()", utiliza o Timsort, que é um algoritmo de ordenação
#    de complexidade O(n logn) que combina o Mergesort com o Insertionsort.
def knapsack(caminhoes, produtos):
    caminhoes = sorted(caminhoes, key=lambda x: x.capacidade, reverse=True)
    produtos = sorted(produtos, key=lambda x: (x.prioridade, x.valor/x.peso), reverse=True)

    max_heap = [(-caminhao.capacidade, caminhao) for caminhao in caminhoes]
    # Utiliza fila de prioridades (heap) para realizar a inserção nos caminhões.
    heapq.heapify(max_heap)

    caminhoes_fim = []
    while len(produtos) and len(max_heap):
        produto = produtos[0]
        capacidade, caminhao = max_heap[0]

        if caminhao.capacidade >= produto.peso:
            caminhao.adicionar_produto(produto)
            caminhao.capacidade -= produto.peso
            caminhao.valor_total += produto.valor
            produtos.remove(produto)
            max_heap[0] = (capacidade, caminhao)
            if not len(produtos):
                caminhoes_fim.append(caminhao)
        elif caminhao.capacidade > 0:
            # Dividir o peso do produto para caber no caminhão
            peso_inserido = caminhao.capacidade
            vp = produto.valor / produto.peso
            valor_inserido = peso_inserido * vp
            produto_inserido = Produto(produto.nome,
                peso_inserido,
                valor_inserido,
                produto.prioridade)
            produtos[0].peso = produto.peso - peso_inserido
            produtos[0].valor = produto.valor - valor_inserido
            caminhao.adicionar_produto(produto_inserido)
            caminhao.valor_total += valor_inserido
            caminhao.capacidade = 0
            caminhoes_fim.append(caminhao)
        if (caminhao.capacidade == 0):
            heapq.heappop(max_heap)

    caminhoes[len(caminhoes_fim)-1:] = caminhoes_fim

    return caminhoes, produtos

def binary_search(notas, l, r, x):
    upper_bound = -1
    indice = -1
    while(l<=r): 
        m = (l+r)//2
        if notas[m] <= x:
            upper_bound = notas[m]
            indice = m
            l= m + 1
        else:
            r = m - 1
    return upper_bound, indice
    
# Algoritmo da Moeda
#   Recebe o troco que deverá ser entregue ao cliente e quais notas estão disponíveis, irá
#    calcular a melhor forma de dividir o troco pelas notas, com a menor quantidade de notas.
def coin_changing(troco, notas):
    notas.sorted(reverse=True)
    select_notas = []
    while(troco != 0):
        nota, k = binary_search(notas, 0, len(notas)-1, troco)
        if(k==0): 
            return -1
        troco -= nota 
        select_notas.append(nota)
    return select_notas

# Algoritmo do Caminhoneiro
#   Recebe o endereco da entrega e todos os caminhoes, calcula a menor quantidade de vezes que
#    cada caminhão precisará abastecer.

def calcular_abastecimento(caminhao, distancia):
    distancia.sort()
    abastecimento = []
    x = 0
    while x != distancia[-1]: 
        bp, p = binary_search(distancia, 0, len(distancia)-1, x + caminhao.autonomia)
        if bp == x:
            return -1
        x = bp
        abastecimento.append(bp)

    return abastecimento

# Função principal
#   O usuário insere a quantidades e dados dos caminhões, produtos, pagamento do cliente e
#    a distância a ser percorrida, retorna os dados da entrega.
def main():
    # numero_caminhoes = int(input("Digite o número de caminhões: "))
    # caminhoes = []

    # for i in range(numero_caminhoes):
    #     capacidade = float(input(f"Digite a capacidade do caminhão {i+1}: "))
    #     distancia = float(input(f"Digite a distância percorrida pelo caminhão {i+1}: "))
    #     caminhao = Caminhao(capacidade, distancia)
    #     caminhoes.append(caminhao)
    
    # produtos = [
    #     Produto('Trigo', 10, 5, 15),
    #     Produto('Parafuso', 20, 8, 5),
    #     Produto('Lã', 15, 6, 10),
    #     Produto('Carne', 30, 10, 20),
    # ]

    # numero_produtos = int(input("Digite o número de produtos: "))

    # produtos = []
    # for i in range(numero_produtos):
    #     nome = input(f"Digite o nome do produto {i+1}: ")
    #     peso = float(input(f"Digite o peso do produto {i+1}: "))
    #     valor = float(input(f"Digite o valor do produto {i+1}: "))
    #     prioridade = input(f"Digite a prioridade do produto {i+1}: ")
    #     produto = Produto(nome, peso, valor, prioridade)
    #     produtos.append(produto)

    # distancia = []
    # numero_postos = int(input("Existem quantos postos no caminho?\n"))
    # for i in range(numero_postos): 
    #     n = int(input(f"Qual a distância do posto {i+1} do ponto inicial?\n"))
    #     distancia.append(n)

    # ----------------------------------------------
    # Dados de exemplo:
    caminhoes = [
        Caminhao(7, 30),
        Caminhao(15, 20),
        Caminhao(20, 10)
    ]

    produtos = [
        Produto("Produto 1", 5, 10, 1),
        Produto("Produto 2", 8, 15, 2),
        Produto("Produto 3", 12, 20, 2),
        Produto("Produto 4", 4, 8, 3),
        Produto("Produto 5", 6, 12, 3),
        Produto("Produto 6", 10, 16, 3)
    ]
    # ----------------------------------------------

    # Algoritmo do Knapsack
    caminhoes, produtos = knapsack(caminhoes, produtos)

    # Imprimir caminhões e seus produtos
    for i, caminhao in enumerate(caminhoes):
        print(f"Caminhão {i+1}:")
        for produto in caminhao.produtos:
            print(f"  Produto: {produto.nome}, Peso: {produto.peso}, Valor: {produto.valor}, Prioridade: {produto.prioridade}")

    # Imprimir produtos restantes
    print("Produtos restantes:")
    for produto in produtos:
        print(f"  Produto: {produto.nome}, Peso: {produto.peso}, Valor: {produto.valor}, Prioridade: {produto.prioridade}")
    
    # Algoritmo do Caminhoneiro junto ao Algoritmo da Moeda
    #   Assume que o caminhoneiro possui todos os tipos de notas em quantidades suficientes.
    #   Recebe um valor pago do usuário para todo o conteúdo de cada caminhão, e assim calcula
    #    seu troco a ser entregue ao cliente.
    # notas = [0.1, 50, 5, 100, 20, 1, 2, 0.25, 10, 200, 0.5]
    # for i, caminhao in enumerate(caminhoes):
    #     result = calcular_abastecimento(caminhao, distancia)
    #     print(result)
    #     print("--------------------- Abastecimento --------------------")
    #     if(result != -1):
    #         print(f"O caminhao {i} vai ter que parar nos kilometros: ")
    #         for posto in result: 
    #             print(posto)
    #     else: 
    #         print("O caminhão não tem automonia para chegar ao destino")
    
    #     valor_pago = float(input(f"Qual o valor que o cliente pagou pelo caminhão {i}?"))
    #     troco = valor_pago - caminhao.valor_total
    #     if troco < 0:
    #         print("Não foi pago o suficiente.")
    #         continue
    #     troco_notas = coin_changing(troco, notas)
    #     print(troco_notas)

    # print(result)

    # Algoritmo da Moeda
    # troco = 100
    # troco_notas = coin_changing(troco, notas)
    # print("Quantidade de notas:", quantidade_notas)


if __name__ == '__main__':
    main()
