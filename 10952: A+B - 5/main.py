# https://www.acmicpc.net/problem/10952

# [input]
# 1 1
# 2 3
# 3 4
# 9 8
# 5 2
# 0 0

# [output]
# 2
# 5
# 7
# 17
# 7

input_data = []

while True:
    a, b = map(int, input().split(' '))
    if not (a and b):
        break
    
    input_data.append((a, b))

print(*[(lambda a, b: a + b)(a, b) for a, b in input_data], sep='\n')
