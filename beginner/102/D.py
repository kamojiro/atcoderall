N = int(input())
*A, = map(int, input().split())
a = sum(A)/4
B1 = 0
B2 = 0
B3 = 0
B4 = 0
for i in range(N):
    if B1 + A[i] <= a and N >= i + 3:
        B1 += A[i]
    elif N == i + 2:
        B2 += A[i]
    else:
        if B2 + A[i] <= a and N >= i + 2:
            B2 += A[i]
        elif N == i + 1:
            B3 += A[i]
        else:
            if B3 + A[i] <= a and N >= i + 1:
                B3 += A[i]
            elif N == i:
                B4 += A[i]
            else:
                B4 += A[i]
C1 = max([B1,B2,B3,B4]) - min([B1,B2,B3,B4])

B1 = 0
B2 = 0
B3 = 0
B4 = 0
for i in range(N):
    if B1 + A[i] <= a and N >= i + 3:
        B1 += A[i]
    elif N == i + 2:
        B2 += A[i]
    else:
        if B2 + A[i] <= a and N >= i + 2:
            B2 += A[i]
        elif N == i + 1:
            B3 += A[i]
        else:
            if B3 <= a and N >= i + 1:
                B3 += A[i]
            elif N == i:
                B4 += A[i]
            else:
                B4 += A[i]
C2 = max([B1,B2,B3,B4]) - min([B1,B2,B3,B4])

B1 = 0
B2 = 0
B3 = 0
B4 = 0
for i in range(N):
    if B1 + A[i] <= a and N >= i + 3:
        B1 += A[i]
    elif N == i + 2:
        B2 += A[i]
    else:
        if B2 <= a and N >= i + 2:
            B2 += A[i]
        elif N == i + 1:
            B3 += A[i]
        else:
            if B3 + A[i] <= a and N >= i + 1:
                B3 += A[i]
            elif N == i:
                B4 += A[i]
            else:
                B4 += A[i]
C3 = max([B1,B2,B3,B4]) - min([B1,B2,B3,B4])

B1 = 0
B2 = 0
B3 = 0
B4 = 0
for i in range(N):
    if B1 + A[i] <= a and N >= i + 3:
        B1 += A[i]
    elif N == i + 2:
        B2 += A[i]
    else:
        if B2 <= a and N >= i + 2:
            B2 += A[i]
        elif N == i + 1:
            B3 += A[i]
        else:
            if B3 <= a and N >= i + 1:
                B3 += A[i]
            elif N == i:
                B4 += A[i]
            else:
                B4 += A[i]
C4 = max([B1,B2,B3,B4]) - min([B1,B2,B3,B4])

B1 = 0
B2 = 0
B3 = 0
B4 = 0
for i in range(N):
    if B1 <= a and N >= i + 3:
        B1 += A[i]
    elif N == i + 2:
        B2 += A[i]
    else:
        if B2 + A[i] <= a and N >= i + 2:
            B2 += A[i]
        elif N == i + 1:
            B3 += A[i]
        else:
            if B3 + A[i] <= a and N >= i + 1:
                B3 += A[i]
            elif N == i:
                B4 += A[i]
            else:
                B4 += A[i]
C5 = max([B1,B2,B3,B4]) - min([B1,B2,B3,B4])

B1 = 0
B2 = 0
B3 = 0
B4 = 0
for i in range(N):
    if B1 <= a and N >= i + 3:
        B1 += A[i]
    elif N == i + 2:
        B2 += A[i]
    else:
        if B2 + A[i] <= a and N >= i + 2:
            B2 += A[i]
        elif N == i + 1:
            B3 += A[i]
        else:
            if B3 <= a and N >= i + 1:
                B3 += A[i]
            elif N == i:
                B4 += A[i]
            else:
                B4 += A[i]
C6 = max([B1,B2,B3,B4]) - min([B1,B2,B3,B4])

B1 = 0
B2 = 0
B3 = 0
B4 = 0
for i in range(N):
    if B1 <= a and N >= i + 3:
        B1 += A[i]
    elif N == i + 2:
        B2 += A[i]
    else:
        if B2 <= a and N >= i + 2:
            B2 += A[i]
        elif N == i + 1:
            B3 += A[i]
        else:
            if B3 + A[i] <= a and N >= i + 1:
                B3 += A[i]
            elif N == i:
                B4 += A[i]
            else:
                B4 += A[i]
C7 = max([B1,B2,B3,B4]) - min([B1,B2,B3,B4])

B1 = 0
B2 = 0
B3 = 0
B4 = 0
for i in range(N):
    if B1 <= a and N >= i + 3:
        B1 += A[i]
    elif N == i + 2:
        B2 += A[i]
    else:
        if B2 <= a and N >= i + 2:
            B2 += A[i]
        elif N == i + 1:
            B3 += A[i]
        else:
            if B3 <= a and N >= i + 1:
                B3 += A[i]
            elif N == i:
                B4 += A[i]
            else:
                B4 += A[i]
C8 = max([B1,B2,B3,B4]) - min([B1,B2,B3,B4])

print(min([C1, C2, C3, C4, C5, C6, C7, C8]))
