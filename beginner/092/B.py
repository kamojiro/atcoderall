N = int(input())
D, X = map(int, input().split())
ans = 0
for i in range(N):
    a = int(input())
    ans += 1 + (D-1)//a
print(ans+X)

