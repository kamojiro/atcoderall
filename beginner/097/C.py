s = input()
K = int(input())
S = set()
for i in range(1, K+1):
    S |= set([s[n:n+i] for n in range(0, max(len(s)-i+1, 0))])
print(sorted(list(S))[K-1])   
    
