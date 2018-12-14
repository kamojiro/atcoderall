n, a, b = map(int, input().split())
sum_n = 0
for i in range(n+1):
    I = list(str(i))
    I = [int(s) for s in I]
    sum_i = 0
    for j in I:
        j = int(j)
        sum_i += j
    if (sum_i >= a and sum_i <= b):
        sum_n += i
print(sum_n)


