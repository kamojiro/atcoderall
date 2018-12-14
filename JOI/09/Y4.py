from itertools import permutations
n = int(input())
k = int(input())
X = [ int(input()) for _ in range(n)]
ANS = set([])
for x in permutations(range(n),k):
    comb = ''
    for i in range(k):
        comb += str(X[x[i]])
    ANS.add(int(comb))
print(len(ANS))










