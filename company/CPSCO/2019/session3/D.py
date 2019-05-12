N = int( input())
S = input()
L = [0]*N
R = [0]*N
if S[0] != "R":
    pass
else:
    L[0] = 1
    for i in range(1,N):
        if S[i] == "R":
            L[i] = 1
        elif S[i] == "G":
            if L[i-1] == 1:
                L[i] = 2
            else:
                break
        elif S[i] == "B":
            if L[i-1] == 2:
                L[i] = 3
            else:
                break
if S[N-1] != "B":
    pass
else:
    R[N-1] = 1
    for i in range(N-2,-1,-1):
        if S[i] == "B":
            R[i] = 1
        elif S[i] == "G":
            if R[i+1] == 1:
                R[i] = 2
            else:
                break
        elif S[i] == "R":
            if R[i+1] == 2:
                R[i] = 3
            else:
                break
ans = "No"
for i in range(N):
    if L[i] == 3 and R[i] == 1 or L[i] == 1 and R[i] == 3:
        ans = "Yes"
        break
print( ans)
            
