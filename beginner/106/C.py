S = list(input())
S = [ int(x) for x in S]
K = int(input())
ans = 1
for i in range(min(K,len(S))):
    if S[i] != 1:
        ans = S[i]
        break
print(ans)
        
    
    
