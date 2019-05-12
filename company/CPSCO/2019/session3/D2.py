N = int( input())
S = input()
ans = "Yes"
T = [0]*N
T[0] = 1
if S[0] == "R":
    ans = "No"
else:
    for i in range(2,N):
        if T[i-1] == 1:
            if S[i] == "R":
                T[i] = 1
            elif S[i] == "G":
                T[i] = 2
            else:
                ans = "No"
                break
        if T[i-1] == 2:
            if S[i] == "R":
                T[i] = 1
            elif S[i] == "B":
                T[i] = 2
            else:
                ans = "No"
                break
        if T[i-1] == 3:
            if S[i] == "R":
                T[i] = 1
            elif S[i] == "G":
                T[i] = 4
            else:
                ans = "No"
                break
        if T[i-1] == 4:
            if S[i] == "R":
                T[i] = 1
            elif S[i] == "B":
                T[i] = 5
            else:
                ans = "No"
                break
        if T[i-1] == 5:
            if S[i] == "R":
                T[i] = 1
            elif S[i] == "B":
                T[i] = 5
            else:
                ans = "No"
                break

