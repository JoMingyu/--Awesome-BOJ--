# https://www.acmicpc.net/problem/11022

# [input]
# 5
# 1 1
# 2 3
# 3 4
# 9 8
# 5 2

# [output]
# Case #1: 1 + 1 = 2
# Case #2: 2 + 3 = 5
# Case #3: 3 + 4 = 7
# Case #4: 9 + 8 = 17
# Case #5: 5 + 2 = 7

print(*[(lambda a, b: 'Case #{}: {} + {} = {}'.format(idx + 1, a, b, a + b))(*map(int, input().split(' '))) for idx in range(int(input()))], sep='\n')