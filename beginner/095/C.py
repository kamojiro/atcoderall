A, B, C, X, Y = map(int, input().split())
mA = min(A,B)
MB = max(A,B)
mXY = min(X,Y)
if A != mA:
    AX = Y
    BY = X
else:
    AX = X
    BY = Y
A = mA
B = MB
X = AX
Y = BY
ans = 0
if A <= C and B <= C:
    ans = A*X + B*Y
else:
    if A + B <= 2*C:
        ans = mXY * (A+B)
        if X > Y:
            ans += A*(X - mXY)
        else:
            ans += B*(Y - mXY)
    else:
        ans = mXY * 2 * C
        if X > Y:
            ans += min(A,2*C)*(X-mXY)
        else:
            ans += min(B,2*C)*(Y-mXY)
print(ans)










