from statistics import median
import math
N = int(input())
*A, = map(int, input().split())
B = [A[i]-i for i in range(N)]
b = median(B)
bm = math.floor(b)
bM = math.ceil(b)
Bm = [abs(x - bm) for x in B]
BM = [abs(x - bM) for x in B]
m = sum(Bm)
M = sum(BM)
print(int(min([m,M])))


