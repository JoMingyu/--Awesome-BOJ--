# https://www.acmicpc.net/problem/1000

# [input]
# 1 2

# [output]
# 3
print((lambda a, b: a + b)(*map(int, input().split(','))))