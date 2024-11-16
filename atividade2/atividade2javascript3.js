// Notas sobre a linguagem:
// Para manipular arquivos o JS usa o módulo fs/promises
// O JS é uma linguagem dinamica tipada, ou seja, não a necessidade de
// declarar tipos e as variaveis podem adicionar valores de qualquer tipo.
// O JS também tem uma estrutura mais simples se comparado a Java.
// Tem suporte a classes e métodos, mas sem modificadores de acesso.
// Classe Nó para representar cada nó da lista
// Também é interresante falar que em comparação a Java, no JS, a leitura
// do arquivo de texto é assincrona, ou seja, ela ocorre em segundo plano,
// isso permite que outras partes do programa continuem sendo executadas.
class No {
  constructor(dado) {
    this.dado = dado; // Valor armazenado no nó
    this.proximo = null; // Referência para o próximo nó
  }
}

// Classe ListaEncadeada para gerenciar a lista e suas operações
class ListaEncadeada {
  constructor() {
    this.cabeca = null; // Inicializa a lista com a cabeça como null (lista vazia)
  }

  // Método para adicionar um nó no final da lista
  adicionarNoFinal(dado) {
    const novoNo = new No(dado); // Cria um novo nó com o valor fornecido
    // const é uma declaração de varíavel que define uma constante
    if (!this.cabeca) {
      // Se a lista estiver vazia, o novo nó se torna a cabeça
      this.cabeca = novoNo;
      return;
    }
    // Caso contrário, percorre até o último nó
    // let -> declara uma variavel que pode ter seus valores reatribuidos
    let ultimoNo = this.cabeca;
    while (ultimoNo.proximo) {
      ultimoNo = ultimoNo.proximo;
    }
    // Define o próximo do último nó como o novo nó
    ultimoNo.proximo = novoNo;
  }

  // Método para inserir um nó em uma posição específica na lista
  inserirNaPosicao(dado, posicao) {
    const novoNo = new No(dado); // Cria um novo nó com o valor fornecido
    if (posicao === 0) {
      // Se a posição for 0, insere o novo nó no início
      novoNo.proximo = this.cabeca;
      this.cabeca = novoNo;
      return;
    }
    // Percorre a lista até a posição anterior à posição desejada
    let atual = this.cabeca;
    for (let i = 0; i < posicao - 1; i++) {
      if (!atual) {
        // Se a posição não existe, encerra a operação
        return;
      }
      atual = atual.proximo;
    }
    if (!atual) {
      // Verifica novamente se a posição é válida
      return;
    }
    // Insere o novo nó na posição especificada e ajusta os ponteiros
    novoNo.proximo = atual.proximo;
    atual.proximo = novoNo;
  }

  // Método para remover o primeiro nó que contém um valor específico
  remover(valor) {
    if (!this.cabeca) {
      // Se a lista estiver vazia, encerra a operação
      return;
    }
    if (this.cabeca.dado === valor) {
      // Caso o valor esteja no primeiro nó
      this.cabeca = this.cabeca.proximo;
      return;
    }
    // Percorre a lista para encontrar o nó com o valor desejado
    let atual = this.cabeca;
    let anterior = null;
    while (atual && atual.dado !== valor) {
      anterior = atual;
      atual = atual.proximo;
    }
    if (atual) {
      // Se o nó com o valor foi encontrado, remove-o
      anterior.proximo = atual.proximo;
    }
  }

  // Método para exibir todos os elementos da lista encadeada
  exibir() {
    let atual = this.cabeca; // Começa do primeiro nó
    const elementos = []; // Lista para armazenar os valores
    while (atual) {
      elementos.push(atual.dado); // Adiciona o valor atual à lista
      atual = atual.proximo;
    }
    console.log(elementos.join(" -> ") + " -> null"); // Exibe os valores separados por " -> "
  }
}

// Função para processar um arquivo de entrada e realizar operações na lista encadeada
const processarArquivo = async (nomeArquivo) => {
  const fs = require("fs/promises"); // Módulo para trabalhar com arquivos (assíncrono)
  const listaEncadeada = new ListaEncadeada();

  try {
    // Lê o arquivo inteiro e divide o conteúdo em linhas
    const conteudo = await fs.readFile(nomeArquivo, "utf8");
    const linhas = conteudo.trim().split("\n");

    // Primeira linha contém os valores iniciais da lista
    const valoresIniciais = linhas[0].trim().split(" ").map(Number);
    for (const valor of valoresIniciais) {
      listaEncadeada.adicionarNoFinal(valor);
    }

    // Segunda linha contém o número de ações a serem realizadas
    const numAcoes = parseInt(linhas[1]);

    // Processa cada ação subsequente
    for (let i = 2; i < 2 + numAcoes; i++) {
      const [acao, ...params] = linhas[i].trim().split(" ");

      if (acao === "A") {
        // Adiciona um valor em uma posição específica
        const [valor, posicao] = params.map(Number);
        listaEncadeada.inserirNaPosicao(valor, posicao);
      } else if (acao === "R") {
        // Remove o primeiro nó com o valor especificado
        const valor = parseInt(params[0]);
        listaEncadeada.remover(valor);
      } else if (acao === "P") {
        // Exibe a lista atual
        listaEncadeada.exibir();
      }
    }
  } catch (err) {
    console.error(`Erro ao processar o arquivo: ${err.message}`);
  }

  return listaEncadeada; // Retorna a lista encadeada final
};

// Código principal para rodar o programa
(async () => {
  const nomeArquivo = "testeatv2.txt"; // Nome do arquivo de entrada
  await processarArquivo(nomeArquivo);
})();
