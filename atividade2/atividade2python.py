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
        # Verifica novamente se a posição é valida
        if atual is None:
            return
        # Insere o novo nó na posição especificada e ajusta os ponteiros.
        novo_no.proximo = atual.proximo
        atual.proximo = novo_no

    # Método Remover, remove o primeiro nó com um valor específico
    def remover(self, valor):
        # Se a lista estiver vazia, encerra a execução
        if self.cabeca is None:
            return
        
        # Caso o valor esteja no primeiro nó (cabeça), ajusta a cabeça para o próximo nó
        if self.cabeca.dado == valor:
            self.cabeca = self.cabeca.proximo
            return
        
        # Percorre a lista para encontrar o nó com o valor desejado
        atual = self.cabeca
        anterior = None
        while atual is not None and atual.dado != valor:
            anterior = atual
            atual = atual.proximo

        # Se o nó com o valor foi encontrado, remove-o
        if atual is not None:
            anterior.proximo = atual.proximo

    # Método para exibir todos os elementos da lista encadeada
    def exibir(self):
        # Lista para armazenar os valores dos nós
        elementos = []
        # Inicia do primeiro nó (cabeça)
        atual = self.cabeca
        # Percorre a lista e adiciona cada valor na lista 'elementos'
        while atual:
            elementos.append(atual.dado)
            atual = atual.proximo
        # Mostra os valores dos nós, separados por " -> "
        print(" -> ".join(map(str, elementos)))

# Função para processar o arquivo e executar as operações
def processar_arquivo(nome_arquivo):
    # Cria uma nova lista vazia
    lista_encadeada = ListaEncadeada()
    # Abre o arquivo para leitura
    with open(nome_arquivo, 'r') as arquivo:
        # Lê a primeira linha do arquivo com os valores iniciais para a lista
        valores_iniciais = map(int, arquivo.readline().strip().split())
         # Adiciona cada valor inicial ao final da lista
        for valor in valores_iniciais:
            lista_encadeada.adicionar_no_final(valor)
        
        # Lê o número de ações a serem realizadas a partir da segunda linha
        num_acoes = int(arquivo.readline().strip())

         # Para cada ação especificada no arquivo, executa o comando correspondente
        for _ in range(num_acoes):
            # Lê a linha da ação e divide em partes
            linha = arquivo.readline().strip().split()
            # O primeiro item da linha é o tipo de ação (A para adicionar, R para remover, P para exibir)
            acao = linha[0]

            # Ação para adicionar um valor em uma posição específica
            if acao == 'A':
                # Valor a ser adicionado
                valor = int(linha[1])
                # Posição onde o valor será inserido
                posicao = int(linha[2])
                lista_encadeada.inserir_na_posicao(valor, posicao)
            
            # Ação para remover o primeiro nó com o valor especificado
            elif acao == 'R':
                # Valor a ser removido 
                valor = int(linha[1]) 
                lista_encadeada.remover(valor)
            
            # Ação para exibir a lista atual
            elif acao == 'P': 
                lista_encadeada.exibir()
    # Retorna a lista encadeada final após todas as operações
    return lista_encadeada

# Testando o código com o arquivo fornecido
nome_arquivo = 'testeatv2.txt'
lista_encadeada = processar_arquivo(nome_arquivo)
