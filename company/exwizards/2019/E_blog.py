Q = 10**9+7
def getInv(N):#Qはmod
    inv = [0] * (N + 1)
    inv[0] = 1
    inv[1] = 1
    for i in range(2, N + 1):
        inv[i] = (-(Q // i) * inv[Q%i]) % Q
    return inv

B, W = map( int, input().split())
Z = getInv(B+W)
I = [1]*(B+W+1)
for i in range(1,B+W+1):
    I[i] = (I[i-1]*Z[i])%Q

F = [1]*(B+W+1)
for i in range(1,B+W+1):
    F[i] = F[i-1]*i%Q
w = 0
b = 0
for i in range(1,B+W+1):
    if i - 1 < B and i - 1 < W:
        print(I[2])
    elif i - 1 >= W and i - 1< B: #i > B
        w += F[i-2]*I[i-1-W]%Q*I[W-1]%Q*pow(I[2],i-1,Q)%Q
        w %= Q
        print(((1 -  w)%Q*I[2]%Q + w)%Q)
    elif i - 1 >= B and i - 1 < W: #i > W
        b += F[i-2]*I[i-1-B]%Q*I[B-1]%Q*pow(I[2],i-1,Q)%Q
        b %= Q
        print((1-b)%Q*I[2]%Q)
    else:
        w += F[i-2]*I[i-1-W]%Q*I[W-1]%Q*pow(I[2],i-1,Q)%Q
        w %= Q
        b += F[i-2]*I[i-1-B]%Q*I[B-1]%Q*pow(I[2],i-1,Q)%Q
        b %= Q
        print(((1 -  w - b)%Q*I[2]%Q + w)%Q)
