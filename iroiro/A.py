N, A, B = map( int, input().split())
S = input()
ans = ""
ab = 0
b=0
AB = A+B
for i in range(N):
    if S[i] == "c":
        print("No")
        continue
    if S[i] == "a":
        if ab < AB:
            ab += 1
            print("Yes")
        else:
            print("No")
    else:
        if b < B and ab < AB:
            b += 1
            ab += 1
            print("Yes")
        else:
            print("No")
