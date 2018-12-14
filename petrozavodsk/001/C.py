N = int( input())
V = [0]*(N+1)
L = 0
R = N
print(0)
s = input()
if s == "Vacant":
    pass
else:
    V[0] = V[N]= s
    for i in range(19):
        M = (L+R)//2
        print(M)
        s = input()
        if s == "Vacant":
            break
        else:
            V[M] = s
            if V[L] == V[M]:
                if (M-L)%2 == 1:
                    R = M
                else:
                    L = M
            else:
                if (M-L)%2 == 0:
                    R = M
                else:
                    L = M
