def rod_cutting(prices, n):
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        max_val = float('-inf')
        for j in range(i):
            max_val = max(max_val, prices[j] + dp[i - j - 1])
        dp[i] = max_val
    
    return dp[n]

def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    n = int(lines[0].strip())
    num_cuts = int(lines[1].strip())
    prices = [0] * n
    
    for i in range(2, 2 + num_cuts):
        length, price = map(int, lines[i].strip().split())
        prices[length - 1] = price
    
    return prices, n

def main():
    input_file = 'input.txt'
    prices, n = read_input(input_file)
    max_profit = rod_cutting(prices, n)
    print(f'Maximum profit: {max_profit}')

if __name__ == '__main__':
    main()
