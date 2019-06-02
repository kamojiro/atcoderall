N, A, B, C, D = map( int, input().split())
S = input()
check = "Yes"
for i in range(A-1, C-1):
    if S[i] == "#" and S[i+1] == "#":
        check = "No"
        break
if check == "Yes":
    for i in range(B-1, D-1):
        if S[i] == "#" and S[i+1] == "#":
            check = "No"
            break    
if check == "Yes":
    if C < D:
        pass
    else:
        check = "No"
        B -= 1
        D -= 1
        t = 0
        for i in range(B-1, D+2):
            if S[i] == ".":
                if t <= 1:
                    t += 1
                else:
                    check = "Yes"
                    break
            else:
                t = 0
print(check)
