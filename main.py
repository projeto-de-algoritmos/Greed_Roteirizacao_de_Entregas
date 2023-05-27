import heapq
import math
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
#   Obs: A função nativa do python, o "sorted()" utiliza o Timsort, que é um algoritmo de ordenação
#    de complexidade O(n logn) que combina o Mergesort com o Insertionsort.
def knapsack(caminhoes, produtos):
    caminhoes = sorted(caminhoes, key=lambda x: x.capacidade, reverse=True)
    produtos = sorted(produtos, key=lambda x: (x.prioridade, x.valor/x.peso), reverse=True)

    for i, produto in enumerate(produtos):
        added = False
        for caminhao in caminhoes:
            if caminhao.capacidade >= produto.peso:
                caminhao.adicionar_produto(produto)
                caminhao.capacidade -= produto.peso
                produtos.remove(produto)
                added = True
                break
            elif caminhao.capacidade > 0:
                # Dividir o peso do produto para caber no caminhão
                peso_restante = caminhao.capacidade
                proporcao = peso_restante / produto.peso
                produto_restante = Produto(produto.nome,
                    produto.peso * proporcao,
                    produto.valor * proporcao,
                    produto.prioridade)
                produtos[i] = Produto(produto.nome, # ARRUMAR SUBSTITUIÇÃO DO VETOR
                    produto.peso - (produto.peso * proporcao),
                    produto.valor - (produto.valor * proporcao),
                    produto.prioridade)
                caminhao.adicionar_produto(produto_restante)
                caminhao.capacidade = 0
                added = True
                break

        if not added:
            break

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
    notas.sort()
    select_notas = []
    while(troco != 0): 
        nota, k = binary_search(notas, 0, len(notas)-1, troco)
        if(k==0): 
            return -1
        troco = troco - nota 
        select_notas.append(nota)
    return select_notas

    # quantidade_notas = [0] * len(notas)

    # for i in range(len(notas)):
    #     quantidade = troco // notas[i]
    #     quantidade_notas[i] = quan;;tidade
    #     troco -= quantidade * notas[i]

    # return quantidade_notas

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

    # Algoritmo do Knapsack


    distancia = []
    numero_postos = int(input("Existem quantos postos no caminho?\n"))
    for i in range(numero_postos): 
        n = int(input(f"Qual a distância do posto {i+1} do ponto inicial?\n"))
        distancia.append(n)

    # Dados de exemplo:
    
    caminhoes = [
        Caminhao(10, 30),
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

    # Imprimir caminhões e seus produtos
    for i, caminhao in enumerate(caminhoes):
        print(f"Caminhão {i+1}:")
        print(f" Capacidade: {caminhao.capacidade}")
        for produto in caminhao.produtos:
            print(f"  Produto: {produto.nome}, Peso: {produto.peso}, Valor: {produto.valor}, Prioridade: {produto.prioridade}")

    # Imprimir produtos restantes
    print("Produtos restantes:")
    for produto in produtos:
        print(f"  Produto: {produto.nome}, Peso: {produto.peso}, Valor: {produto.valor}, Prioridade: {produto.prioridade}")

    print('-----------------------------------------')

    caminhoes, produtos = knapsack(caminhoes, produtos)

    print('-----------------------------------------')

    # Imprimir caminhões e seus produtos
    for i, caminhao in enumerate(caminhoes):
        print(f"Caminhão {i+1}:")
        print(f" Capacidade: {caminhao.capacidade}")
        for produto in caminhao.produtos:
            caminhao.valor_total += produto.valor
            print(f"  Produto: {produto.nome}, Peso: {produto.peso}, Valor: {produto.valor}, Prioridade: {produto.prioridade}")

    # Imprimir produtos restantes
    print("Produtos restantes:")
    for produto in produtos:
        print(f"  Produto: {produto.nome}, Peso: {produto.peso}, Valor: {produto.valor}, Prioridade: {produto.prioridade}")
   
    # Algoritmo do Caminhoneiro
    notas = [200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.25, 0.1]
    for i, caminhao in enumerate(caminhoes): 
        result = calcular_abastecimento(caminhao, distancia)
        print("--------------------- Abastecimento --------------------\n")
        if(result != -1):
            print(f"O caminhao {i+1} vai ter que parar nos kilometros: ")
            for posto in result: 
                print(f"{posto} km")
        else: 
            print("O caminhão não tem automonia para chegar ao destino")

        print("-------------------- Melhor troco ----------------------\n")

        valor_pago = float(input(f"Qual o valor que o cliente pagou pelo caminhão {i+1}?\n"))
        troco = valor_pago - caminhao.valor_total

        if not troco: 
            print("O valor informado não precisa de troco.")

        troco_notas = coin_changing(troco, notas)
        troco_notas = Counter(troco_notas)
        if(troco_notas!=-1):
            for chave in troco_notas: 
                if(chave>=2):
                    print(f"{troco_notas[chave]} notas de {chave} reais")
                else: 
                    print(f"{troco_notas[chave]} moedas de {chave} reais")
        else: 
            print("Não existe troco para o valor informado")

    # Algoritmo da Moeda
    # troco = 100
    # Assume que o caminhoneiro possui todos os tipos de notas em quantidades suficientes.
    # troco_notas = coin_changing(troco, notas)
    # print("Quantidade de notas:", quantidade_notas)


if __name__ == '__main__':
    main()
