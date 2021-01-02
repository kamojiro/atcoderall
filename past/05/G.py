#import sys
#input = sys.stdin.readline
# from collections import defaultdict
# def sum_periodic(x):
#     ret = 0
#     while x > 0:
#         ret += x%2
#         x //= 2
#     return ret

def exists(x,p):
    if (x & p) == p:
        return True
    else:
        return False
def main():
    H, W = map( int, input().split())
    S = [list(input()) for _ in range(H)]
    visited = [[False]*(2**20) for _ in range(H*W)]
    before = [[-1]*(2**20) for _ in range(H*W)]
    P = [pow(2,i) for i in range(20)]
    P
    target = 0
    occupied = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                target += 1
                occupied += P[i*W+j]
    q = []
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                q.append((i*W+j,P[i*W+j]))
                visited[i*W+j][P[i*W+j]] = True
                if target == 1:
                    print(1)
                    print(str(i+1)+" "+str(j+1))
                    return
    # print("?",visited[0][occupied])
    while q:
        x, y = q.pop()
        i, j = x//W, x%W
        # print(x,y,q)
        if i > 0:
            if S[i-1][j] == ".":
                pass
            elif exists(y,P[(i-1)*W+j]):
                # print("yP", y, P[(i-1)*W+j], (y and P[(i-1)*W+j] == P[(i-1)*W+j]))
                pass
            else:
                # print("i>0")
                p = y + P[(i-1)*W+j]
                if visited[(i-1)*W+j][p]:
                    pass
                else:
                    visited[(i-1)*W+j][p] = True
                    before[(i-1)*W+j][p] = x
                    q.append(((i-1)*W+j,p))
        if i < H-1:
            if S[i+1][j] == ".":
                pass
            elif exists(y, P[(i+1)*W+j]):
                pass
            else:
                p = y + P[(i+1)*W+j]
                if visited[(i+1)*W+j][p]:
                    pass
                else:
                    visited[(i+1)*W+j][p] = True
                    before[(i+1)*W+j][p] = x
                    q.append(((i+1)*W+j,p))
        if j > 0:
            if S[i][j-1] == ".":
                pass
            elif exists(y, P[i*W+j-1]):
                pass
            else:
                p = y + P[i*W+j-1]
                if visited[i*W+j-1][p]:
                    pass
                else:
                    visited[i*W+j-1][p] = True
                    before[i*W+j-1][p] = x
                    q.append((i*W+j-1,p))

        if j < W-1:
            if S[i][j+1] == ".":
                pass
            elif exists(y, P[i*W+j+1]):
                pass
            else:
                # print(y,P[i*W+j+1],exists(y, P[i*W+j+1]))
                p = y + P[i*W+j+1]
                if visited[i*W+j+1][p]:
                    pass
                else:
                    visited[i*W+j+1][p] = True
                    before[i*W+j+1][p] = x
                    q.append((i*W+j+1,p))
    x = 0
    for i in range(H*W):
        if visited[i][occupied]:
            x = i
            break
    ANS = []
    # print(target, occupied)
    # print(x, occupied)
    while occupied > 0:
        ANS.append((x//W+1,x%W+1))
        x, occupied = before[x][occupied], occupied-P[x]
        # print(x, occupied)
    print(target)
    print("\n".join([" ".join(map(str,ans)) for ans in ANS]))
        
        
        



    
                
if __name__ == '__main__':
    main()
