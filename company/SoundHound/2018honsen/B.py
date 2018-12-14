N, K = map(int, input().split())
B = [int(input()) for _ in range(N)]
sumb = [0]
for x in B:
    sumb.append(sumb[-1]+x)
for i in range(N-K+1):
    print(B)
    if B[i] > 0:
        pass
    elif sumb[i+K] - sumb[i] < 0:
        for j in range(i,i+K):
            B[j] = 0
            sumb = [0]
            for x in B:
                sumb.append(sumb[-1]+x)
            
print(sumb[-1])
        
