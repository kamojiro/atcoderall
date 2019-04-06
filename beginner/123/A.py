A = [ int( input()) for _ in range(5)]
k = int( input())
ans = "Yay!"
if A[4] - A[0] > k:
    ans = ":("
print(ans)
        
