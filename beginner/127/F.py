import sys
input = sys.stdin.readline
from heapq import heappush, heappop
def main():
    Q = int(input())
    Queries = [ tuple(map(int,input().split())) for _ in range(Q)]
    ANS = []
    mq = []
    Mq = []
    c = 0
    count = 0
    m = 0
    M = 0
    for query in Queries:
        if query == (2,):
            # print(m,M)
            # print(-mq[0],((-mq[0])*((count+1)//2))-m, (M-(-mq[0])*(count//2)), c)
            ANS.append((-mq[0],((-mq[0])*((count+1)//2)-m) + (M-(-mq[0])*(count//2)) +c))
            continue
        
        count += 1
        _, a, b = query
        c += b
        if count == 1:
            mq.append(-a)
            m += a
            continue
        elif count == 2:
            if -mq[0] > a:
                M = -mq[0]
                m = a
                Mq.append(-mq[0])
                mq[0] = -a
            else:
                M = a
                Mq.append(a)
            continue

        s, t = -mq[0], Mq[0]

        if count%2 == 1:
            if a <= t:
                heappush(mq,-a)
                m += a
            else:
                z = heappop(Mq)
                M -= z
                M += a
                m += z
                heappush(Mq,a)
                heappush(mq,-z)

        else:
            if a >= s:
                heappush(Mq,a)
                M += a
            else:
                z = -heappop(mq)
                m -= z
                m += a
                M += z
                heappush(mq,-a)
                heappush(Mq,z)
        
    print("\n".join(map(str,[" ".join(map(str,ans)) for ans in ANS])))
   
if __name__ == '__main__':
    main()

    
