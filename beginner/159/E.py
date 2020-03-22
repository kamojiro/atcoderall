#import sys
#input = sys.stdin.readline
from itertools import accumulate, product
def main():
    H, W, K = map( int, input().split())
    S = [ list( map( int, list( input()))) for _ in range(H)]
    ans = 10**5
    cnt = 0
    AS = [ [0] + list( accumulate(S[i])) for i in range(H)]
    #print(AS)
    #TAS = list( zip(*AS))
    SAS = []
    for a in AS:
        SAS.extend(a)
    for P in product( range(2), repeat=H-1):
    # for i in range(2**(H-1)):
    #     P =[]
    #     for _ in range(H-1):
    #         P.append(i%2)
    #         i //= 2
        now = sum(P)
        if ans < now:
            continue
        start = 0
        goal = 0
        #print(P, now)
        while start < W:
            for i in range(start, W):
                cnt = 0
                check =True
                for j in range(H):
                    #cnt += AS[j][i+1] - AS[j][start]
                    #cnt += TAS[i+1][j] - TAS[start][j]
                    #                    print(P, start, i, j,cnt)
                    cnt += SAS[j*(W+1)+i+1] - SAS[j*(W+1)+start]
                    if j == H-1:
                        if cnt > K:
                            check = False
                            break
                    else:
                        if P[j] == 1:
                            if cnt > K:
                                check = False
                                
                                break
                            cnt = 0
                if check:
                    goal += 1
            if start == goal:
                start = W+1
                now = 10**5
                break
            #print("sg",P,start, goal, W)
            start = goal
            if goal < W:
                #print("now")
                now += 1
            #print(now)
        
        if now < ans:
            ans = now
    print(ans)
                
if __name__ == '__main__':
    main()
