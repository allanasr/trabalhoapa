def rod_cutting(prices, n):
    # dp[i] armazena o lucro máximo obtido ao cortar uma haste de comprimento i
    dp = [0] * (n + 1)
    
    # Itera sobre todos os comprimentos de haste de 1 a n
    for i in range(1, n + 1):
        max_val = float('-inf')
        # Verifica todos os cortes possíveis para o comprimento atual
        for j in range(i):
            # Atualiza o lucro máximo para o comprimento atual
            max_val = max(max_val, prices[j] + dp[i - j - 1])
        dp[i] = max_val
    
    return dp[n]

def read_input(file_path):
    # Lê o arquivo de entrada
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # Primeira linha: comprimento da haste
    n = int(lines[0].strip())
    # Segunda linha: quantidade de cortes distintos
    num_cuts = int(lines[1].strip())
    prices = [0] * n
    
    # Linhas seguintes: tamanho e preço de venda de cada objeto
    for i in range(2, 2 + num_cuts):
        length, price = map(int, lines[i].strip().split())
        prices[length - 1] = price
    
    return prices, n

def main():
    input_file = 'input.txt'  # Caminho do arquivo de entrada
    prices, n = read_input(input_file)
    max_profit = rod_cutting(prices, n)
    print(f'Maximum profit: {max_profit}')

if __name__ == '__main__':
    main()
