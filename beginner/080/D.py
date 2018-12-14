from itertools import accumulate
N, C = map( int, input().split())
timetable = [ [0]*(10**5+2) for _ in range(C+1)]
for _ in range(N):
    s, t, c = map( int, input().split())
    timetable[c][s-1] += 1
    timetable[c][t+1] -= 1
for c in range(1,C+1):
    timetable[c] = list( accumulate(timetable[c]))
ans = 0
for i in range(1,10*5+1):
    now = 0
    for c in range(1,C+1):
        if timetable[c][i] > 0:
            now += 1
    ans = max( now, ans)
for c in range(1,C+1):
    print( timetable[c][:40])
print(ans)
