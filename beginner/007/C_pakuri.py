from collections import deque

r, c = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())

sy -= 1
sx -= 1
gy -= 1
gx -= 1

c = [list(input())for _ in range(r)]

dx = [1, 0,-1, 0]
dy = [0, 1, 0,-1]

def bfs():
    que = deque([(sy,sx)])
    c[sy][sx] = 0
    while bool(que):
        y, x = que.popleft()
        if y == gy and x == gx:
            break
        for i in range(4):
            yi = y + dy[i]
            xi = x + dx[i]
            if c[yi][xi] == ".":
                que.append((yi,xi))
                c[yi][xi] = c[y][x] + 1

bfs()
print(c[gy][gx])
