from bisect import bisect_right
N, H = map( int, input().split())
A,B = [], []
for i in range(N):
    a,b = map(int, input().split())
    A.append(a)
    B.append(b)

maxA = max(A)
sortB = sorted(B)
RsortB = sortB[::-1]
L = N - bisect_right(sortB,maxA)
ans = 0
damage_sum = 0
Flag = True
for i in range(L):
    damage_sum = damage_sum + RsortB[i]
    if damage_sum < H:
        ans += 1
        pass
    else:
        ans += 1
        Flag = False
        break
if Flag:
    ans += (H - damage_sum + maxA - 1)//maxA
print(ans)

