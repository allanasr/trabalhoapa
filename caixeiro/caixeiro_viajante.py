import sys
import itertools

def read_input(filename):
    with open(filename, 'r') as file:
        n = int(file.readline().strip())
        
        distance_matrix = []
        for _ in range(n):
            line = file.readline().strip().split()
            distance_matrix.append([int(x) for x in line])
    
    return n, distance_matrix

def tsp(n, distance_matrix):
    vertices = list(range(n))
    
    min_path_cost = sys.maxsize
    min_path = []
    
    for perm in itertools.permutations(vertices[1:]):
        current_path_cost = 0
        current_path = [0] + list(perm) + [0]
        
        for i in range(len(current_path) - 1):
            current_cost = distance_matrix[current_path[i]][current_path[i + 1]]
            if current_cost == 999:
                current_path_cost = sys.maxsize
                break
            current_path_cost += current_cost
        
        if current_path_cost < min_path_cost:
            min_path_cost = current_path_cost
            min_path = current_path
    
    return min_path_cost, min_path

def main():
    if len(sys.argv) != 2:
        print("Uso: python caixeiro_viajante.py <nome_do_arquivo>")
        return
    
    filename = sys.argv[1]
    n, distance_matrix = read_input(filename)
    min_path_cost, min_path = tsp(n, distance_matrix)
    
    if min_path_cost == sys.maxsize:
        print("Não é possível encontrar um caminho válido.")
    else:
        print(f"Custo mínimo: {min_path_cost}")
        print(f"Caminho: {' -> '.join(map(str, min_path))}")

if __name__ == "__main__":
    main()