import sys
import platform
import psutil
import time

# Função para ordenar a lista (Merge Sort)
def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2  # Ponto médio do array
        left_half = array[:mid]  # Divide o array em duas metades
        right_half = array[mid:]

        merge_sort(left_half)  # Ordena a metade esquerda
        merge_sort(right_half)  # Ordena a metade direita

        # Intercala as duas metades ordenadas
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                array[k] = left_half[i]
                i += 1
            else:
                array[k] = right_half[j]
                j += 1
            k += 1

        # Adiciona os elementos restantes da metade esquerda (se houver)
        while i < len(left_half):
            array[k] = left_half[i]
            i += 1
            k += 1

        # Adiciona os elementos restantes da metade direita (se houver)
        while j < len(right_half):
            array[k] = right_half[j]
            j += 1
            k += 1

# Função para ler números de um arquivo .txt
def read_numbers_from_file(filename):
    with open(filename, 'r') as file:
        numbers = [int(line.strip()) for line in file]  # Lê cada linha, converte para int e armazena na lista
    return numbers

# Função para escrever os números ordenados em um novo arquivo
def write_numbers_to_file(filename, numbers):
    with open(filename, 'w') as file:
        for number in numbers:
            file.write(f"{number}\n")

# Função para pegar informações do sistema
def get_system_info():
    # Informações do sistema
    python_version = sys.version
    system_info = platform.uname()
    cpu_info = psutil.cpu_percent(interval=1)  # Uso de CPU
    memory_info = psutil.virtual_memory()

    # Exibindo as informações
    print(f"Linguagem Python: {python_version}")
    print(f"Sistema: {system_info.system} {system_info.release} ({system_info.machine})")
    print(f"Processador: {system_info.processor}")
    print(f"Uso de CPU: {cpu_info}%")
    print(f"Memória Total: {memory_info.total / (1024 ** 2):.2f} MB")
    print(f"Memória Livre: {memory_info.available / (1024 ** 2):.2f} MB")
    print(f"Memória Usada: {memory_info.used / (1024 ** 2):.2f} MB")

# Caminho do arquivo
input_filename = 'arq-desafio.txt'
output_filename = 'arq-saida.txt'

# Lê os números do arquivo
numbers = read_numbers_from_file(input_filename)

# Medir o tempo de execução do algoritmo de ordenação
start_time = time.time()  # Inicia o contador de tempo
merge_sort(numbers)       # Chama a função de ordenação
end_time = time.time()    # Finaliza o contador de tempo
execution_time = (end_time - start_time) * 1000  # Tempo em milissegundos

# Escrever os números ordenados em um novo arquivo
write_numbers_to_file(output_filename, numbers)

# Exibe as informações do sistema
get_system_info()

# Exibe o tempo de execução e a memória RAM utilizada
process = psutil.Process()
memory_info = process.memory_info()
print(f"\nTempo de Execução: {execution_time:.2f} ms")
print(f"Memória RAM Utilizada: {memory_info.rss / 1024:.2f} KB")
