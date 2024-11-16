// Classe Nó para representer cada nó da lista
class No {
  int dado; // Atributo para armazenar o valor do nó
  No proximo; // Refêrencia para o próximo nó da lista

  // Construtor da classe que inicia o nó com um valor e aponta para null (o próximo nó)
  public No(int dado) {
    this.dado = dado;
    this.proximo = null;
  }
}

// Classe Lista Encadeada para gerenciar a lista e suas operações
class ListaEncadeada {
  No cabeca; // Atributo cabeça do tipo No que armazena o primeiro nó da lista

  // Construtor que inicia a lista com a cabeça apontando para null(lista vazia)
  public ListaEncadeada() {
    this.cabeca = null;
  }


// Método Adicionar, adiciona um nó no final da lista
public void adicionarNoFinal(int dado) {
  // Cria um novo nó com o valor fornecido
  No novoNo = new No(dado);
  // Se a lista estiver vazia, o novo nó se torna a cabeça
  if (cabeca == null) {
    cabeca = novoNo;
    return;
  }
  // Se não, percorre até o último nó
  No ultimoNo = cabeca;
  while (ultimoNo.proximo != null) {
    ultimoNo = ultimoNo.proximo;
  }
  // Definir o próximo do último nó como o novo nó
  ultimoNo.proximo = novoNo;
}

// Método para adicionar um nó numa posição especifica na lista
public void inserirNaPosicao(int dado, int posicao) {
  // Criar um novo nó com o valor fornecido
  No novoNo = new No(dado);
  // Se  a posição for 0, insere o novo nó no início
  if (posicao == 0) {
    novoNo.proximo = cabeca;
    cabeca = novoNo;
    return;
  }
  // Se não, percorre a lista até a posição anterior à posição desejada
  No atual = cabeca;
  for(int i = 0; i < posicao - 1; i++) {
    if (atual == null) {
      // Se a posição não existe, encerra a operação
      return;
    }
    atual = atual.proximo;
  }

  if (atual == null) {
    // Verifica novamente se a posição é valida
    return;
  }
  // Insere o nó e ajusta os ponteiros.
  novoNo.proximo = atual.proximo;
  atual.proximo = novoNo;
}

// Método para remover o primeiro nó que contém um valor específico
public void remover(int valor) {
  // Se a lista estiver vazia, encerra a operação
  if (cabeca == null) {
    return;
  }
  // Caso o valor esteja no primeiro nó, a cabeca vai apontar para o proximo
  if (cabeca.dado == valor) {
    cabeca = cabeca.proximo;
    return;
  }
  // Percorre a lista para encontrar o nó com o valor desejado
  No atual = cabeca;
  No anterior = null;
  while (atual != null && atual.dado != valor) {
    anterior = atual;
    atual = atual.proximo;
  }
  // Se o nó com o valor foi encontrado, remove=o e ajusta o ponteiro do nó anterior
  if (atual != null) {
    anterior.proximo = atual.proximo;
  }
}

// Método para exibir todos os elementos da lista
public void exibir() {
  // Começa do primeiro nó
  No atual = cabeca;
  while (atual != null) {
    System.out.print(atual.dado + " -> ");
    atual = atual.proximo;
  }
  System.out.println("null");
}
}

// Classe para processar o arquivo
public class ListaEncadeadaArquivo {

  // Método para processar um arquivo de entrada e realizar operações na lista 
  public static ListaEncadeada processarArquivo(String nomeArquivo) {
      // Cria uma nova lista encadeada
      ListaEncadeada listaEncadeada = new ListaEncadeada(); 
      try (java.util.Scanner scanner = new java.util.Scanner(new java.io.File(nomeArquivo))) {
          // Lê a primeira linha do arquivo com os valores iniciais para a lista
          if (scanner.hasNextLine()) {
              String[] valoresIniciais = scanner.nextLine().trim().split(" ");
              for (String valor : valoresIniciais) {
                  listaEncadeada.adicionarNoFinal(Integer.parseInt(valor));
              }
          }

          // Lê o número de ações a serem realizadas
          int numAcoes = scanner.nextInt();
          // Pula para a próxima linha após o número de ações
          scanner.nextLine(); 

          // Para cada ação, executa o comando correspondente
          for (int i = 0; i < numAcoes; i++) {
              String[] linha = scanner.nextLine().trim().split(" ");
              String acao = linha[0]; 
              // O tipo de ação (A, R ou P)
              if (acao.equals("A")) { // Ação para adicionar um valor em uma posição específica
                  int valor = Integer.parseInt(linha[1]); // Valor a ser adicionado
                  int posicao = Integer.parseInt(linha[2]); // Posição onde o valor será inserido
                  listaEncadeada.inserirNaPosicao(valor, posicao);

              } else if (acao.equals("R")) { // Ação para remover o primeiro nó com o valor especificado
                  int valor = Integer.parseInt(linha[1]); // Valor a ser removido
                  listaEncadeada.remover(valor);

              } else if (acao.equals("P")) { // Ação para exibir a lista atual
                  listaEncadeada.exibir();
              }
          }
      } catch (java.io.FileNotFoundException e) {
          System.out.println("Arquivo não encontrado: " + nomeArquivo);
      }

      return listaEncadeada; // Retorna a lista encadeada final após todas as operações
  }

  // Método para testar o código com o arquivo fornecido
  public static void main(String[] args) {
      String nomeArquivo = "testeatv2.txt"; // Nome do arquivo de entrada
      ListaEncadeada listaEncadeada = processarArquivo(nomeArquivo);
  }
}