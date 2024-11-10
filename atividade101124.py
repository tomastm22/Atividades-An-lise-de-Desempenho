class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None


class ListaEncadeada:
    def __init__(self):
        self.cabeca = None

    def adicionar_no_final(self, dado):
        novo_no = No(dado)
        if not self.cabeca:
            self.cabeca = novo_no
            return
        ultimo_no = self.cabeca
        while ultimo_no.proximo:
            ultimo_no = ultimo_no.proximo
        ultimo_no.proximo = novo_no

    def inserir_na_posicao(self, dado, posicao):
        novo_no = No(dado)
        if posicao == 0:
            novo_no.proximo = self.cabeca
            self.cabeca = novo_no
            return
        atual = self.cabeca
        for _ in range(posicao - 1):
            if atual is None:
                return
            atual = atual.proximo
        if atual is None:
            return
        novo_no.proximo = atual.proximo
        atual.proximo = novo_no

    def remover_na_posicao(self, posicao):
        if self.cabeca is None:
            return
        atual = self.cabeca
        if posicao == 0:
            self.cabeca = atual.proximo
            return
        anterior = None
        for _ in range(posicao):
            if atual is None:
                return
            anterior = atual
            atual = atual.proximo
        if atual is None:
            return
        anterior.proximo = atual.proximo

    def exibir(self):
        elementos = []
        atual = self.cabeca
        while atual:
            elementos.append(atual.dado)
            atual = atual.proximo
        print(" -> ".join(map(str, elementos)))


def processar_arquivo(nome_arquivo):
    lista_encadeada = ListaEncadeada()

    with open(nome_arquivo, 'r') as arquivo:
        
        valores_iniciais = map(int, arquivo.readline().strip().split())
        for valor in valores_iniciais:
            lista_encadeada.adicionar_no_final(valor)
        
       
        num_acoes = int(arquivo.readline().strip())
        
       
        for _ in range(num_acoes):
            linha = arquivo.readline().strip().split()
            acao = linha[0]
            
            if acao == 'A':  
                valor = int(linha[1])
                posicao = int(linha[2])
                lista_encadeada.inserir_na_posicao(valor, posicao)
            elif acao == 'R': 
                posicao = int(linha[1])
                lista_encadeada.remover_na_posicao(posicao)
            elif acao == 'P': 
                lista_encadeada.exibir()

    return lista_encadeada

nome_arquivo = 'exemplo.txt'

lista_encadeada = processar_arquivo(nome_arquivo)