N = int( input())
ANS = [["", "", 0] for _ in range(N)]
for i in range(N):
    s, p = input().split()
    ANS[i] = [s,-int(p),i+1]
ANS.sort()
for i in range(N):
    print(ANS[i][2])
