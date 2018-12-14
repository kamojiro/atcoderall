N, C = map( int, input().split())
timetable = [ [0]*(10**5) for _ in range(C)]
for _ in range(N):
    s,t,c = map( int, input().split())
    timetable[c-1][s-1:t] = [1]*(t-s+1)
# for c in range(C):
#     print(timetable[c][:20])
ans = 0
for i in range(10**5):
    now = 0
    for c in range(C):
        now += timetable[c][i]
    if ans < now:
        ans = now
print(ans)
