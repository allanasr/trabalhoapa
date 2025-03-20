import sys

def read_input(filename):
    # Abre o arquivo e lê os números, convertendo-os para uma lista de inteiros
    with open(filename, 'r') as file:
        data = list(map(int, file.readline().strip().split()))
    return data

def counting_sort(arr):
    # Encontra o valor máximo e mínimo no array
    max_val = max(arr)
    min_val = min(arr)
    range_of_elements = max_val - min_val + 1
    
    # Inicializa os arrays de contagem e de saída
    count_arr = [0] * range_of_elements
    output_arr = [0] * len(arr)
    
    # Conta a ocorrência de cada elemento no array
    for num in arr:
        count_arr[num - min_val] += 1
    
    # Modifica o array de contagem para armazenar as posições dos elementos
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]
    
    # Constrói o array de saída
    for num in reversed(arr):
        output_arr[count_arr[num - min_val] - 1] = num
        count_arr[num - min_val] -= 1
    
    return output_arr

def main():
    # Verifica se o nome do arquivo foi passado como argumento
    if len(sys.argv) != 2:
        print("Uso: python counting_sort.py <nome_do_arquivo>")
        return
    
    filename = sys.argv[1]
    data = read_input(filename)
    sorted_data = counting_sort(data)
    
    # Imprime o array ordenado
    print("Array ordenado:", sorted_data)

if __name__ == "__main__":
    main()
