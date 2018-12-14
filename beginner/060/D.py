from itertools import accumulate
N, W = map( int, input().split())
o, k = map( int, input().split())
A = [k]
B, C, D = [], [], []
for _ in range(N-1):
    w, v = map( int, input().split())
    if w == o:
        A.append(v)
    elif w == o+1:
        B.append(v)
    elif w == o+2:
        C.append(v)
    else:
        D.append(v)
A.sort(key=None, reverse = True)
B.sort(key=None, reverse = True)
C.sort(key=None, reverse = True)
D.sort(key=None, reverse = True)
A = [0] + list(accumulate(A))
B = [0] + list(accumulate(B))
C = [0] + list(accumulate(C))
D = [0] + list(accumulate(D))
# print(A)
# print(B)
# print(C)
# print(D)
ans = 0
for i in range( len(A)):
    for j in range( len(B)):
        for k in range( len(C)):
            for l in range( len(D)):
                if i*o + j*(o+1) + k*(o+2) + l*(o+3) <= W:
#                    print('{} {} {} {}'.format(i,j,k,l))
                    ans = max( ans, A[i]+B[j]+C[k]+D[l])
print(ans)
