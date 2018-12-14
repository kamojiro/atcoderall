import itertools
n, m = map(int, input().split())
hyoka = [""] * n
for i in range(n):
    hyoka[i] = input().split()
for i in range(n):
    hyoka[i] = [int(s) for s in hyoka[i]]
hyou = [""]
for iroiro in list(itertools.combination(hyoka, m)):
    sum_1 = sum[beau[1] for beau in iroiro]
    sum_1 = abs(sum_1)
    sum_2 = sum[beau[2] for beau in iroiro]
    sum_2 = abs(sum_2)
    sum_3 = sum[beau[3] for beau in iroiro]
    sum_3 = abs(sum_3)
    som = sum_1 + sum_2 + sum_3
    hyou = hyou.append(som)
print(max(hyou))
    

