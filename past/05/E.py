#import sys
#input = sys.stdin.readline
def check(H,W,S,P,Q,T):
    for h in range(H+P-1):
        for w in range(W+Q-1):
            check = True
            # print(h,w)
            for i in range(P):
                for j in range(Q):
                    if P-1 <= h+i < H+P-1 and Q-1 <= w+j < W+Q-1:
                        
                        # print("T",i,j,T[i][j], "S", h+i-(H-1),w+j-(W-1), S[h-i-(H-1)][w+j-(W-1)])
                        if T[i][j] == "#" and S[h+i-(P-1)][w+j-(Q-1)] == "#":
                            check = False
                            break
                    else:
                        if T[i][j] == "#":
                            check = False
                            break
                if not check:
                    break
            if check:
                # print(h,w)
                return True
    return False
                    


def main():
    H, W = map(int, input().split())
    S = [ list(input()) for _ in range(H)]
    T = [ list(input()) for _ in range(H)]
    for _ in range(4):
        # print("\n".join(["".join(a) for a in T]))
        P = len(T)
        Q = len(T[0])
        if check(H,W,S,P,Q,T):
            print("Yes")
            return
        T = [ x for x in zip(*T[::-1])]

    print("No")
    
if __name__ == '__main__':
    main()
