def gcd(a, b):
  while b > 0:
    a, b = b, a%b
  return a

def lcm(a,b):
    return (a*b)//gcd(a, b)

N = int( input())
T = [ int( input()) for _ in range(N)]
ans = T[0]
for i in range(1,N):
    ans = lcm(ans,T[i])
print(ans)
