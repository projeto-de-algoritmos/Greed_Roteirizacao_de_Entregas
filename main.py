import heapq
from collections import Counter

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
    def __init__(self, capacidade, autonomia, index):
        self.capacidade = capacidade
        self.autonomia = autonomia
        self.produtos = []
        self.valor_total = 0
        self.index = index

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
    caminhoes = sorted(caminhoes, key=lambda x: x.autonomia, reverse=True)
    produtos = sorted(produtos, key=lambda x: (x.prioridade, x.valor/x.peso), reverse=True)

    max_heap = [(-caminhao.autonomia, caminhao) for caminhao in caminhoes]
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
        elif caminhao.capacidade > 0 and len(produtos):
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

    if len(caminhoes) == len(caminhoes_fim): 
        caminhoes = caminhoes_fim
    else:
        caminhoes[len(caminhoes_fim)-1:] = caminhoes_fim

    return caminhoes, produtos

# Algoritmo de busca binária
# O algoritmo retorna o maior número menor do que o x, que é passado como parâmetro,
# por meio de uma busca binária, é utilizado no algoritmo da moeda e do caminhoneiro
def binary_search(notas, l, r, x):
    upper_bound = -1
    indice = -1
    while(l<=r): 
        m = (l+r)//2
        if notas[m] <= x:
            upper_bound = notas[m]
            indice = m
            l = m + 1
        else:
            r = m - 1
    return upper_bound, indice
    
# Algoritmo da Moeda
#   Recebe o troco que deverá ser entregue ao cliente e quais notas estão disponíveis, irá
#    calcular a melhor forma de dividir o troco pelas notas, com a menor quantidade de notas.
#   Obs: A função nativa do python, o "sort()", utiliza o Timsort, que é um algoritmo de ordenação
#    de complexidade O(n logn) que combina o Mergesort com o Insertionsort.
def coin_changing(troco, notas):
    notas.sort()
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

# ----------------------------------------------
    # Dados de exemplo:
    # caminhoes = [
    #     Caminhao(7, 30),
    #     Caminhao(15, 20),
    #     Caminhao(20, 10)
    # ]

    # produtos = [
    #     Produto("Produto 1", 5, 10, 1),
    #     Produto("Produto 2", 8, 15, 2),
    #     Produto("Produto 3", 12, 20, 2),
    #     Produto("Produto 4", 4, 8, 3),
    #     Produto("Produto 5", 6, 12, 3),
    #     Produto("Produto 6", 10, 16, 3)
    # ]
# ----------------------------------------------

# Função principal
#   O usuário insere a quantidades e dados dos caminhões, produtos, pagamento do cliente e
#    a distância a ser percorrida, retorna os dados da entrega.
def main():
    numero_caminhoes = int(input("Digite o número de caminhões: "))
    caminhoes = []

    for i in range(numero_caminhoes):
        capacidade = float(input(f"Digite a capacidade do caminhão {i+1}: "))
        autonomia = float(input(f"Digite a autonomia do caminhão {i+1}: "))
        caminhao = Caminhao(capacidade, autonomia, i+1)
        caminhoes.append(caminhao)

    numero_produtos = int(input("Digite o número de produtos: "))

    produtos = []
    for i in range(numero_produtos):
        nome = input(f"Digite o nome do produto {i+1}: ")
        peso = float(input(f"Digite o peso do produto {i+1}: "))
        valor = float(input(f"Digite o valor do produto {i+1}: "))
        prioridade = input(f"Digite a prioridade do produto {i+1}: ")
        produto = Produto(nome, peso, valor, prioridade)
        produtos.append(produto)

    distancia = []
    numero_postos = int(input("Existem quantos postos no caminho?\n"))
    for i in range(numero_postos): 
        n = int(input(f"Qual a distância do posto {i+1} do ponto inicial?\n"))
        distancia.append(n)
    
    # Algoritmo do Knapsack
    caminhoes, produtos = knapsack(caminhoes, produtos)

    # Algoritmo do Caminhoneiro junto ao Algoritmo da Moeda
    #   Assume que o caminhoneiro possui todos os tipos de notas em quantidades suficientes.
    #   Recebe um valor pago do usuário para todo o conteúdo de cada caminhão, e assim calcula
    #    seu troco a ser entregue ao cliente.
    notas = [0.1, 50, 5, 100, 20, 1, 2, 0.25, 10, 200, 0.5]
    for i, caminhao in enumerate(caminhoes):
        print(f"--------------------- Informações - Caminhão {caminhao.index} --------------------")

        # Mostra informações do caminhão 'i+1':
        print(f"Capacidade atual do caminhão: {caminhao.capacidade}")
        print(f"Autonomia do caminhão: {caminhao.autonomia}")

        # Mostra todos os produtos no caminhão 'i+1'
        print(f"Produtos no caminhão {caminhao.index}:")
        for produto in caminhao.produtos:
            print(f"  Produto: {produto.nome}, Peso: {produto.peso}, Valor: {produto.valor}, Prioridade: {produto.prioridade}")

        print(f"Valor total: {caminhao.valor_total}")

        # Calcula e mostra os postos que o caminhoneiro precisará passar dentro de sua autonomia, com o algoritmo do caminhoneiro.
        result = calcular_abastecimento(caminhao, distancia)
        if(result != -1):
            print(f"O caminhao {caminhao.index} vai ter que parar nos kilometros: ")
            
            for posto in result: 
                print(f"{posto} km")
        else: 
            print(f"O caminhão {caminhao.index} não tem autonomia para chegar ao destino.")

        # Pede o valor pago pelo cliente e calcula o troco e quais notas compõem o troco, pelo algoritimo da moeda.
        valor_pago = float(input(f"Qual o valor que o cliente pagou pelo caminhão {caminhao.index}?\n"))
        troco = valor_pago - caminhao.valor_total
    
        if not troco: 
            print("O valor informado não precisa de troco.")

        troco_notas = coin_changing(troco, notas)
        if(troco_notas!=-1):
            troco_notas = Counter(troco_notas)
            for chave in troco_notas: 
                if(chave>=2):
                    print(f"{troco_notas[chave]} notas de {chave} reais")
                else: 
                    print(f"{troco_notas[chave]} moedas de {chave} reais")
        else: 
            print("Não existe troco para o valor informado")

    print("Produtos restantes:")
    if len(produtos):
        for produto in produtos:
            print(f"  Produto: {produto.nome}, Peso: {produto.peso}, Valor: {produto.valor}, Prioridade: {produto.prioridade}")
    else:
        print("Não restou nenhum produto!")

if __name__ == '__main__':
    main()
