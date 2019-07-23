N = int( input())
S = [ input() for _ in range(N)]
ANS = [""]*N
for i in range(N):
    for j in range(N):
        ANS[i] += S[N-1-j][i]
for ans in ANS:
    print(ans)
