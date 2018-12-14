from itertools import product
from copy import deepcopy
S = list(input())
x, y = map( int, input().split())
UD = [] #updown
LR = [0] #leftright
X = deepcopy(LR)
t = 0
for w in S:
    if w == 'F':
        X[-1] += 1
    elif t == 0:
        LR = deepcopy(X)
        X = deepcopy(UD)
        X.append(0)
        t = 1
    else:
        UD = deepcopy(X)
        X = deepcopy(LR)
        X.append(0)
        t = 0
if t == 0:
    LR = deepcopy(X)
else:
    UD = deepcopy(X)
x = x - LR.pop(0)
G = 0
H = 0
LLR = len(LR)
LUD = len(UD)
for B in product([-1,1], repeat = LLR):
    Z = 0
    for i in range(LLR):
        Z += LR[i]*B[i]
    if Z == x:
        G = 1

for B in product([-1,1],repeat = LUD):
    Z = 0
    for i in range(LUD):
        Z += UD[i]*B[i]
    if Z == y:
        H = 1
print('Yes' if G == 1 and H == 1 else 'No')
