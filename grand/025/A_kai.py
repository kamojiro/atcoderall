def kakuwa(S):
    A = list(str(S))
    B = [int(x) for x in A]
    return sum(B)
    
N = int(input())
for i in range(1,5):
    if N%(10**i) == 0:
        ans = 10
        break
else:
    ans = kakuwa(N)
print(ans)










