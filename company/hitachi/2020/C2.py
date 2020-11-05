#import sys
#input = sys.stdin.readline
def solve11(N,V,mod3):
    ANS = [0]*N
    for i,v in enumerate(V):
        if v == 0:
            if mod3[v+1]:
                ANS[i] = mod3[v+1].pop()
            else:
                ANS[i] = mod3[0].pop()
        else:
            if mod3[v+1]:
                ANS[i] = mod3[v+1].pop()
            else:
                ANS[i] = mod3[0].pop()
    return ANS

def solve10(N,V,t,mod3):
    ANS = [0]*N
    for i, v in enumerate(V):
        if v == t:
            ANS[i] = mod3[0].pop()
        else:
            for j in range(3):
                k = (j+1)%3
                if mod3[k]:
                    ANS[i] = mod3[k].pop()
                    break
    return ANS

def main():
    N = int(input())
    AB = [ tuple(map(lambda x:int(x)-1, input().split())) for _ in range(N-1)]
    E = [[] for _ in range(N)]
    for a, b in AB:
        E[a].append(b)
        E[b].append(a)
    stack = [0]
    V = [-1]*N
    V[0] = 0
    parity = [1,0]
    while stack:
        s = stack.pop()
        v = (V[s]+1)%2
        for t in E[s]:
            if V[t] == -1:
                V[t] = v
                parity[v] += 1
                stack.append(t)

    mod3 = [[] for _ in range(3)]
    for i in range(1,N+1):
        mod3[i%3].append(i)

    if parity[0] > N//3 and parity[1] > N//3:
        ANS = solve11(N,V,mod3)
    elif parity[0] > N//3:
        ANS = solve10(N,V,1,mod3)
    else:
        ANS = solve10(N,V,0,mod3)

    print(" ".join(map(str,ANS)))
        
if __name__ == '__main__':
    main()
