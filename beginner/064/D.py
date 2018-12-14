#グラフを書いて前から順番に埋めていけば良さげ
N = int( input())
S = list( input())
X = [0]
now = S[0]
cnt = 0
for k in S:
    if k != now:
        X.append(cnt)
        now = k
    if k == '(':
        cnt += 1
    else:
        cnt -= 1
else:
    if X[-1] != cnt:
        X.append(cnt)
m = min(X)

if m < 0:
    X = list(map( lambda x: x-m, X))

if X[0] != 0:
    if X[0] <= X[1]:
        X[0] = 0
    else:
        X.insert(0,0)
if X[-1] != 0:
    if X[-2] <= X[-1]:
        X.append(0)
    else:
        X[-1] = 0
L = len(X)
up = 'up'
down = 'down'
updown = up

ans = ''
L = len(X)
for i in range(1,L):
    if updown == up:
        ans += '('*(X[i] - X[i-1])
        updown = down
    else:
        ans += ')'*(X[i-1] - X[i])
        updown = up
print(ans)
    

    
    

