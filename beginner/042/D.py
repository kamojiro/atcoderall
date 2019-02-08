Q = 10**9+7
def getInv(N):#Qはmod
    inv = [0] * (N + 1)
    inv[0] = 1
    inv[1] = 1
    for i in range(2, N + 1):
        inv[i] = (-(Q // i) * inv[Q%i]) % Q
    return inv
modfunctional = [1]*(2*10**5+1)
modinv = getInv(10**5+1)
modinvfunctional = [1]*(10**5+1)
for i in range(10**5):
    modinvfunctional[i+1] = (modinvfunctional[i]*modinv[i+1])%Q
for i in range(2*10**5):
    modfunctional[i+1] = (modfunctional[i]*(i+1))%Q
H, W, A, B = map( int, input().split())
ans = 0
for i in range(B+1, W+1):
    ans += (modfunctional[i+H-A-2]*modinvfunctional[i-1]*modinvfunctional[H-A-1]%Q)*(modfunctional[A+W-i-1]*modinvfunctional[A-1]*modinvfunctional[W-i]%Q)%Q
    ans %= Q
print(ans)
    
