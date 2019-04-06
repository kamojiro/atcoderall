N = int( input())
A = [ int( input()) for _ in range(5)]
m = min(A)
ans = -(-N//m)+4
print(ans)
