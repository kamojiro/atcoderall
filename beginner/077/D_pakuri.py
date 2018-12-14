from collections import deque
K = int(input())
dist = [10 ** 5] * K
dist[1] = 1
print(dist)
d = deque()
d.append(1)
print(d)
a = 0
while a == 0:
    u = d.popleft()
    if u == 0:
        print(dist[u])
        break
    if dist[u] < dist[(u * 10) % K]:
        dist[(u * 10) % K] = dist[u]
        d.appendleft((u * 10) % K)
        print("A")
        print(dist)
        print(d)
    if dist[u] < dist[(u + 1) % K]:
        dist[(u + 1) % K] = dist[u] + 1
        d.append((u + 1) % K)
        print("B")
        print(dist)
        print(d)

    
