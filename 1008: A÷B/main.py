# https://www.acmicpc.net/problem/1008

# [input]
# 1 3

# [output]
# 0.33333333333333333333333333333333

print((lambda a, b: a / b)(*map(int, input().split(','))))