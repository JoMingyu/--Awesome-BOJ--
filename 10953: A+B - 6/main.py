# https://www.acmicpc.net/problem/10953

# [input]
# 5
# 1,1
# 2,3
# 3,4
# 9,8
# 5,2

# [output]
# 2
# 5
# 7
# 17
# 7

print(*[(lambda a, b: a + b)(*map(int, input().split(','))) for _ in range(int(input()))], sep='\n')