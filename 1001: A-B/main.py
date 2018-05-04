# https://www.acmicpc.net/problem/1001

# [input]
# 3 2

# [output]
# 1

print((lambda a, b: a - b)(*map(int, input().split(','))))