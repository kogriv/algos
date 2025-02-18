# with open('input.txt', 'r') as f_inp, open('output.txt', 'w') as f_out:
#     n = int(f_inp.readline())
#     # print(range(n))
#     prev = int(f_inp.readline())
#     # print('prev:', prev)
#     f_out.write(str(prev) + '\n')
#     for _ in range(2,n):
#         curr = int(f_inp.readline())
#         # print('curr:', curr)
#         if curr > prev:
#             # print('curr > prev')
#             f_out.write(str(curr) + '\n')
#             prev = curr

#     a = [int(f.readline()) for i in range(n)]
#     print(a)

# r = [a[0]]

# for i in range(1,n):
#     if a[i] > a[i-1]:
#         r.append(a[i])
# print(r)

def remove_duplicates():
    # Read n
    n = int(input())
    
    # Handle first number separately
    if n > 0:
        prev = int(input())
        print(prev)
        
    # Process remaining numbers
    for _ in range(n - 1):
        current = int(input())
        if current != prev:
            print(current)
            prev = current

# Run the solution
remove_duplicates()

"""
 Legend

Дан упорядоченный по неубыванию массив целых 32-разрядных чисел. Требуется удалить из него все повторения.

Желательно получить решение, которое не считывает входной файл целиком в память, т.е., использует лишь константный объем памяти в процессе работы.
Input format

Первая строка входного файла содержит единственное число n, n ≤ 1000000.

На следующих n строк расположены числа — элементы массива, по одному на строку. Числа отсортированы по неубыванию.
Output format

Выходной файл должен содержать следующие в порядке возрастания уникальные элементы входного массива.
Sample 1
Input
Output

5
2
4
8
8
8

	

2
4
8

"""