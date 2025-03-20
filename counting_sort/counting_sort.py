import sys

def read_input(filename):
    with open(filename, 'r') as file:
        data = list(map(int, file.readline().strip().split()))
    return data

def counting_sort(arr):
    max_val = max(arr)
    min_val = min(arr)
    range_of_elements = max_val - min_val + 1
    
    count_arr = [0] * range_of_elements
    output_arr = [0] * len(arr)
    
    for num in arr:
        count_arr[num - min_val] += 1
    
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]
    
    for num in reversed(arr):
        output_arr[count_arr[num - min_val] - 1] = num
        count_arr[num - min_val] -= 1
    
    return output_arr

def main():
    if len(sys.argv) != 2:
        print("Uso: python counting_sort.py <nome_do_arquivo>")
        return
    
    filename = sys.argv[1]
    data = read_input(filename)
    sorted_data = counting_sort(data)
    
    print("Array ordenado:", sorted_data)

if __name__ == "__main__":
    main()
