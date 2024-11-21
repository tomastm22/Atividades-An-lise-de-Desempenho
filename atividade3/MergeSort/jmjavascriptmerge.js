const fs = require("fs");
const os = require("os");

// Função para ordenar a lista (Merge Sort)
function mergeSort(array) {
  if (array.length <= 1) {
    return array;
  }

  const mid = Math.floor(array.length / 2); // Ponto médio do array
  const left = mergeSort(array.slice(0, mid)); // Ordena a metade esquerda
  const right = mergeSort(array.slice(mid)); // Ordena a metade direita

  return merge(left, right); // Intercala as duas metades ordenadas
}

function merge(left, right) {
  const result = [];
  let i = 0,
    j = 0;

  // Intercala os elementos de left e right
  while (i < left.length && j < right.length) {
    if (left[i] < right[j]) {
      result.push(left[i]);
      i++;
    } else {
      result.push(right[j]);
      j++;
    }
  }

  // Adiciona os elementos restantes de left (se houver)
  while (i < left.length) {
    result.push(left[i]);
    i++;
  }

  // Adiciona os elementos restantes de right (se houver)
  while (j < right.length) {
    result.push(right[j]);
    j++;
  }

  return result;
}

// Função para ler números de um arquivo .txt
function readNumbersFromFile(filename) {
  const data = fs.readFileSync(filename, "utf-8");
  return data
    .split("\n")
    .map((line) => parseInt(line.trim()))
    .filter((num) => !isNaN(num));
}

// Função para escrever os números ordenados em um novo arquivo
function writeNumbersToFile(filename, numbers) {
  const data = numbers.join("\n");
  fs.writeFileSync(filename, data);
}

// Função para pegar informações do sistema
function getSystemInfo() {
  console.log(`Linguagem: Node.js ${process.version}`);
  console.log(`Sistema: ${os.type()} ${os.release()} (${os.arch()})`);
  console.log(`Processador: ${os.cpus()[0].model}`);
  console.log(`Uso de CPU (não exato): ~${os.loadavg()[0].toFixed(2)}%`);
  console.log(`Memória Total: ${(os.totalmem() / 1024 ** 2).toFixed(2)} MB`);
  console.log(`Memória Livre: ${(os.freemem() / 1024 ** 2).toFixed(2)} MB`);
}

// Caminho do arquivo
const inputFilename = "arq.txt";
const outputFilename = "arq-saida.txt";

// Lê os números do arquivo
const numbers = readNumbersFromFile(inputFilename);

// Medir o tempo de execução do algoritmo de ordenação
const startTime = process.hrtime(); // Inicia o contador de tempo
const sortedNumbers = mergeSort(numbers); // Chama a função de ordenação
const endTime = process.hrtime(startTime); // Finaliza o contador de tempo
const executionTime = (endTime[0] * 1000 + endTime[1] / 1e6).toFixed(2); // Tempo em milissegundos

// Escrever os números ordenados em um novo arquivo
writeNumbersToFile(outputFilename, sortedNumbers);

// Exibe as informações do sistema
getSystemInfo();

// Exibe o tempo de execução e a memória RAM utilizada
const memoryUsage = process.memoryUsage().rss / 1024; // Memória usada em KB
console.log(`\nTempo de Execução: ${executionTime} ms`);
console.log(`Memória RAM Utilizada: ${memoryUsage.toFixed(2)} KB`);
