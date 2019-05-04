H, W, N = map( int, input().split())
sx, sy = map( int, input().split())
sx, sy = sy-1, sx-1
S = input()
T = input()
ans = "YES"
x = sx
for i in range(N):#left
    if S[i] == "L":
        x -= 1
    if x < 0:
        ans = "NO"
        break
    if T[i] == "R":
        if x < W-1:
            x += 1
x = sx
for i in range(N):#right
    if S[i] == "R":
        x += 1
    if x > W-1:
        ans = "NO"
        break
    if T[i] == "L":
        if x > 0 :
            x -= 1
y = sy
for i in range(N):#up
    if S[i] == "U":
        y -= 1
    if y < 0:
        ans = "NO"
        break
    if T[i] == "D":
        if y < H-1 :
            y+= 1

y = sy
for i in range(N):#down
    if S[i] == "D":
        y += 1
    if y > H-1:
        ans = "NO"
        break
    if T[i] == "U":
        if y > 0 :
            y-= 1            
print(ans)
    
# SLR = [0]*N
# SUD = [0]*N
# TLR = [0]*N
# TUD = [0]*N
# for i in range(N):
#     if S[i] == "L":
#         SLR[i] = -1
#     elif S[i] == "R":
#         SLR[i] = 1
#     elif S[i] == "U":
#         SUD[i] = -1
#     else:
#         SUD[i] = 1
#     if T[i] == "L":
#         TLR[i] = -1
#     elif T[i] == "R":
#         TLR[i] = 1
#     elif T[i] == "U":
#         TUD[i] = -1
#     else:
#         TUD[i] = 1


