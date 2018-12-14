from bisect import bisect_right
N = int(input())
c = 0
def croku(N):
    roku =[0,1] + [6**i for i in range(1,7)]
    c = 0
    while N != 0:
        N = N - roku[bisect_right(roku,N)-1]
        c += 1
    return c

def ckyu(N):
    kyu = [0,1] + [9**i for i in range(1,6)]
    c = 0
    while N != 0:
        N = N - kyu[bisect_right(kyu,N)-1]
        c += 1
    return c

K = 10**5
for i in range(N+1):
    K = min(K, croku(i) + ckyu(N-i))
print(K)








