txa, tya, txb, tyb, T, V = map( int, input().split())
n = int( input())
X = [0]*n
Y = [0]*n
ans = "NO"
for i in range(n):
    x, y = map( int, input().split())
    if ((txa - x)**2 + (tya - y)**2)**(1/2) + ((txb - x)**2 + (tyb - y)**2)**(1/2) <= T*V:
        ans = "YES"
        break
print( ans)

