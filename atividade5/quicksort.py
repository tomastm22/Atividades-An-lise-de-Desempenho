import sys
import platform
import psutil
import time

def quick_sort(array, low, high):
    if low < high:
        pivot_index = partition(array, low, high) # Divide o array em 2
        quick_sort(array, low, pivot_index - 1) # Ordena o ladodireito
        quick_sort(array, pivot_index + 1, high) # Ordena o lado esquerdo

def partition(array, low, high):
    pivot = array[high]  # Escolhe o último elemento como pivô
    i = low - 1
    for j in range(low, high):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

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
quick_sort(numbers, 0, len(numbers) - 1)
end_time = time.time()
execution_time = (end_time - start_time) * 1000  # Tempo em milissegundos

# Escrever os números ordenados no arquivo de saída
write_numbers_to_file(output_filename, numbers)

# Exibir métricas
print(f"Tempo de Execução: {execution_time:.2f} ms")