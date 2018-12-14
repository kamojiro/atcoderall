N, Q = map(int, input().split())
*X, = map(int, input().split())
for i in range(1,Q+1):
    C, D = map(int, input().split())
    K = 0
    XP = [abs(x-C) for x in X]
    for x in XP:
        if x <= D:
            K += x
        else:
            K += D
    print(K)

