N = int( input())
S = input()
ans = "Yes"
T = [0]*N
T[0] = 1
if S[0] != "R":
    ans = "No"
else:
    for i in range(1,N):
        if T[i-1] == 1:
            if S[i] == "R":
                T[i] = 1
            elif S[i] == "G":
                T[i] = 2
            else:
                ans = "No"
                break
        elif T[i-1] == 2:
            if S[i] == "R":
                T[i] = 1
            elif S[i] == "B":
                T[i] = 3
            else:
                ans = "No"
                break
        elif T[i-1] == 3:
            if S[i] == "R":
                T[i] = 1
            elif S[i] == "G":
                T[i] = 4
            else:
                T[i] = 3
        elif T[i-1] == 4:
            if S[i] == "R":
                T[i] = 1
            elif S[i] == "B":
                T[i] = 5
            else:
                ans = "No"
                break
        elif T[i-1] == 5:
            if S[i] == "R":
                T[i] = 1
            elif S[i] == "G":
                T[i] = 4
            else:
                T[i] = 5

if T[-1] == 1 or T[-1] == 2 or T[-1] == 4:
    ans = "No"
print(ans)
