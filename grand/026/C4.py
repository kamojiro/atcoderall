from collections import Counter
from itertools import product
N = int(input())
S = input()
Left = Counter()
Right = Counter()
S_left = S[:N]
S_right = S[2*N-1:N-1:-1]
for B in product(range(2),repeat = N):
    red_left = ''
    blue_left = ''
    red_right = ''
    blue_right = ''
    for i in range(N):
        if B[i]:
            red_left += S_left[i]
            red_right += S_right[i]
        else:
            blue_left += S_left[i]
            blue_right += S_right[i]
    Left[red_left + '|' + blue_left] += 1
    Right[blue_right + '|' + red_right] += 1
ans = 0
for i in Left.keys():
    ans += Left[i]*Right[i]
print(ans)
