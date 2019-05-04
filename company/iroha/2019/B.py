S = input()
K = int( input())
K = K%len(S)
print(S[K:] + S[:K])
