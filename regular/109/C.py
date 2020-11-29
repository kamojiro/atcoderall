#import sys
#input = sys.stdin.readline
def a_win(x,y):
    if x == y:
        return True
    if x == 1 and y == 0:
        return True
    if x == 0 and y == 2:
        return True
    if x == 2 and y == 1:
        return True
    return False

def main():
    n, k = map(int,input().split())
    s = list(input())
    R = 0
    P = 1
    S = 2
    G = []
    for t in s:
        if t == "R":
            G.append(R)
        elif t == "P":
            G.append(P)
        else:
            G.append(S)
    gamari = G[-pow(2,k,n):]
    q = n
    r = len(gamari)
    # 2^k = q*?+r
    for kk in range(k,0,-1):
        if q == 1:
            break
        H = []
        if q%2 == 0:
            for i in range(0,q,2):
                a, b = G[i], G[i+1]
                if a_win(a,b):
                    H.append(a)
                else:
                    H.append(b)
            hq = q//2
        else:
            for i in range(0,q*2,2):
                a, b = G[i%q], G[(i+1)%q]
                if a_win(a,b):
                    H.append(a)
                else:
                    H.append(b)
            hq = q
        G = H
        q = hq
    if G[0] == 0:
        print("R")
    elif G[0] == 1:
        print("P")
    else:
        print("S")
        # hr = pow(2,kk-1,hq)

            
        #     hamari = []
        #     for i in range(0,2,r):
        #         a, b = gamari[i], gamari[i+1]
        #         if a_win(a,b):
        #             hamari.append(a)
        #         else:
        #             hamari.append(b)
        #         r //= 2
    
                
    
    
if __name__ == '__main__':
    main()
