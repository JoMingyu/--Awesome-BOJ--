# https://www.acmicpc.net/problem/11021

# [input]
# 5
# 1 1
# 2 3
# 3 4
# 9 8
# 5 2

# [output]
# Case #1: 2
# Case #2: 5
# Case #3: 7
# Case #4: 17
# Case #5: 7

print(*[(lambda a, b: 'Case #{}: {}'.format(idx + 1, a + b))(*map(int, input().split(' '))) for idx in range(int(input()))], sep='\n')