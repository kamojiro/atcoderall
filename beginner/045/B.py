S = [list( input()) for _ in range(3)]
C = ['A', 'B', 'C']
now = 0
nowc = 'A'
while True:
    if not S[now]:
        ans = C[now]
        break
    nowc = S[now].pop(0)
    if nowc == 'a':
        now = 0
    elif nowc == 'b':
        now = 1
    else:
        now = 2
print(ans)
