import sys
import platform
import psutil
import time

def heapify(array, n, i):
    largest = i  # Inicializa o maior como raiz
    left = 2 * i + 1  # Filho esquerdo
    right = 2 * i + 2  # Filho direito

    if left < n and array[left] > array[largest]:
        largest = left
    if right < n and array[right] > array[largest]:
        largest = right
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, n, largest)

def heap_sort(array):
    n = len(array)
    for i in range(n // 2 - 1, -1, -1):
        heapify(array, n, i)
    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)

def read_numbers_from_file(filename):
    with open(filename, 'r') as file:
        return [int(line.strip()) for line in file]

def write_numbers_to_file(filename, numbers):
    with open(filename, 'w') as file:
        file.writelines(f"{num}\n" for num in numbers)

# Caminho dos arquivos
input_filename = 'entrada-100k.txt'
output_filename = 'saida-100k.txt'

# Lê os números do arquivo
numbers = read_numbers_from_file(input_filename)

# Medir tempo de execução
start_time = time.time()
heap_sort(numbers)
end_time = time.time()
execution_time = (end_time - start_time) * 1000  # Tempo em milissegundos

# Escrever os números ordenados no arquivo de saída
write_numbers_to_file(output_filename, numbers)

# Exibir métricas
print(f"Tempo de Execução: {execution_time:.2f} ms")