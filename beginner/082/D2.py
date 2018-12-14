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
dpx = [0]
k = 0
while k <= len(LR)-1:
    dpx_kari = deepcopy(dpx)
    dpx = []
    for m in dpx_kari:
        dpx.append(m + LR[k])
        dpx.append(m - LR[k])
    k += 1
k = 0
dpy = [0]
while k <= len(UD)-1:
    dpy_kari = deepcopy(dpy)
    dpy = []
    for m in dpy_kari:
        dpy.append(m + UD[k])
        dpy.append(m - UD[k])
    k += 1

if x in dpx and y in dpy:
    print('Yes')
else:
    print('No')
