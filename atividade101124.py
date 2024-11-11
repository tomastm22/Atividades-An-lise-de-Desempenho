# Criei uma classe Nó para representar cada nó da lista. 
# A classe tem como atributo o dado, que no caso dessa lista será um valor númerico
# e o atrubuto proxímo que é o endereço de para onde o nó aponta.
class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

# Criei a classe lista encadeada para representar a lista encadeada em si.
# Nesse classe serão encontrados os métodos dessa estrutura de dados.
class ListaEncadeada:
    # Método construtor que inicia a lista ligada com a cabeça, ou seja, o primeiro nó
    # como vazia.
    def __init__(self):
        self.cabeca = None

    # Médoto para adicionar no final da lista, esse método adiciona um novo nó no final da lista.
    def adicionar_no_final(self, dado):
        novo_no = No(dado) # Cria um novo nó com o valor fornecido.
        # Se a lista estiver vazia, o novo nó se torna o nó cabeça
        # ou seja, o primeiro nó.
        if not self.cabeca: 
            self.cabeca = novo_no
            return
        # Caso contrário vai percorrer a lista até o último nó.
        ultimo_no = self.cabeca
        while ultimo_no.proximo:
            ultimo_no = ultimo_no.proximo
        # Defini o próximo do último nó como sendo o novo nó, colocando ele no final da lista.
        ultimo_no.proximo = novo_no

    # Método Adicionar, esse método inseri um novo nó em uma posição especifica
    def inserir_na_posicao(self, dado, posicao):
        # Cria um novo nó com o valor fornecido pelo arquivo de texto
        novo_no = No(dado) 
        # Se a posição for 0, insere o novo nó no inicio(cabeça)
        if posicao == 0:
            novo_no.proximo = self.cabeca
            self.cabeca = novo_no
            return
        # Caso contrário, percorre a lista até a posição anterior a posição desejada
        atual = self.cabeca
        for _ in range(posicao - 1):
            # Se a posição não existe, encerra
            if atual is None: 
                return
            atual = atual.proximo
        if atual is None:
            return
        # Insere o novo nó na posição especifica e ajusta os ponteiros
        # [atual] -> [X]
        novo_no.proximo = atual.proximo
        atual.proximo = novo_no
        # [atual] -> [novo_no] -> [X]

    # Método Remover, esse método remove um nó em uma posição específica. 
    def remover_na_posicao(self, posicao):
        # Se a lista estiver vazia, encerra o código
        if self.cabeca is None:
            return
        atual = self.cabeca
        # Se a posição for 0, ajusta a cabeça para o próximo nó
        if posicao == 0:
            self.cabeca = atual.proximo
            return
        # Caso contrário, percorre a lista até o nó na posição desejada
        anterior = None
        for _ in range(posicao):
            # Se a posição não existe, encerra
            if atual is None: 
                return
            anterior = atual
            atual = atual.proximo
        # Verifica se o nó para a remoção existe
        if atual is None:
            return
        # Ajusta o ponteiro do nó anterior para pular o nó atual
        anterior.proximo = atual.proximo

    # Método Imprimir a lista, metodo que vai exibir os elementos da lista.
    def exibir(self):
        # Cria uma lista para armazenar os valores.
        elementos = []
        # Inicia do nó cabeça(primeiro nó)
        atual = self.cabeca
        # Percorre a lista e adiciona cada valor à lista 'elementos'
        while atual:
            elementos.append(atual.dado)
            atual = atual.proximo
        # Imprime os valores da lista separados por " -> "
        print(" -> ".join(map(str, elementos)))

# Método para processar um arquivo de entrada e realizar as operações da lista
def processar_arquivo(nome_arquivo):
    # Cria uma nova Lista Ligada vazia.
    lista_encadeada = ListaEncadeada()

    # Abre o arquivo para leitura
    with open(nome_arquivo, 'r') as arquivo:
        # Lê a primeira linha com os valores iniciais para a lista
        valores_iniciais = map(int, arquivo.readline().strip().split())
        for valor in valores_iniciais:
            lista_encadeada.adicionar_no_final(valor)
        
        # Lê o número deações a serem realizadas
        num_acoes = int(arquivo.readline().strip())
        
        # Para cada ação especifica no arquivo
        for _ in range(num_acoes):
            # Lê a linha e divide em partes
            linha = arquivo.readline().strip().split()
            # O primeiro item é o tipo de ação (A, R ou P)
            acao = linha[0]
            
            # Se a  ação for 'A', adiciona um valor na posição especificada
            if acao == 'A':
                # O valor a ser adicionado  
                valor = int(linha[1])
                # A posição onde será inserido
                posicao = int(linha[2])
                lista_encadeada.inserir_na_posicao(valor, posicao)
            # Se a ação for 'R', remove o valor na posição especifica
            elif acao == 'R': 
                # A posição a ser removida
                posicao = int(linha[1])
                lista_encadeada.remover_na_posicao(posicao)
            # Se a ação for 'P', imprime a lista atual
            elif acao == 'P': 
                lista_encadeada.exibir()

    return lista_encadeada # Retorna a lista encadeada final

# Testendo o código
nome_arquivo = 'exemplo.txt'

lista_encadeada = processar_arquivo(nome_arquivo)