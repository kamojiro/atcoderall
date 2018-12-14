def kakuwa(S):
    A = list(str(S))
    B = [int(x) for x in A]
    return sum(B)
    
N = int(input())
ans = 50
for i in range(1,N):
    ans = min(ans, kakuwa(i) + kakuwa(N-i))
print(ans)
    
    
