import time

H = 30
W = 30-1
N = 1000
base = [ list(map(int,input().split())) for _ in range(H)]
conclution = [[list(map(int,input().split())) for _ in range(H)] for _ in range(N)]
input()
for n, c in enumerate(conclution):
    if n < 0:
        continue
    for i in range(H):
        print(" ".join(map(lambda x: str(x).rjust(5, ' '), [base[i][j] - c[i][j] for j in range(W)])))

    s = sum([ sum([ abs(base[i][j] - c[i][j])for j in range(W)]) for i in range(H)])
    a = sum([ sum([ base[i][j] - c[i][j] for j in range(W)]) for i in range(H)])
    print(n,s,a, "-"*200)
    time.sleep(0.1)
    

