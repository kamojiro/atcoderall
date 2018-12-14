N, Q = map(int, input().split())
*X, = map(int, input().split())
for i in range(1,Q+1):
    C, D = map(int, input().split())
    XP = [abs(x-C) if abs(x-C) <= D else D for x in X]
    print(sum(XP))










