# import sys
# input = sys.stdin.readline

#A1 ~ Aiまでの和 O(logN)
#A1 ~ Aiまでの和 O(logN)
# def BIT_query(BIT,idx):
#     res_sum = 0
#     if idx == 0:
#         return 0
#     while idx > 0:
#         res_sum += BIT[idx]
#         idx -= idx&(-idx)
#     return res_sum

# #Ai += x O(logN)
# def BIT_update(BIT,idx,x,n):
#     while idx <= n:
#         BIT[idx] += x
#         idx += idx&(-idx)
#     return

def main():
    N, Q = map( int, input().split())
    C = list( map( int, input().split()))
    LRI = []
    for i in range(Q):
        l, r = map( int, input().split())
        LRI.append((r,l,i))
    LRI.sort(key=lambda x:x[0])
    lastAppend = [-1]*(N+1)
    BIT = [0]*(N+1)
    #A1 ~ Aiまでの和 O(logN)
    def BIT_query(idx):
        res_sum = 0
        if idx == 0:
            return 0
        while idx > 0:
            res_sum += BIT[idx]
            idx -= idx&(-idx)
        return res_sum

    #Ai += x O(logN)
    def BIT_update(idx,x):
        while idx <= N:
            BIT[idx] += x
            idx += idx&(-idx)
        return

    ANS = [0]*Q
    now = 1
    for r, l, i in LRI:
        while now <= r:
            c = C[now-1]
            if lastAppend[c] == -1:
                BIT_update(now, 1)
            else:
                BIT_update( now, 1)
                BIT_update(lastAppend[c],-1)
            lastAppend[c] = now                
            now += 1
        ANS[i] = BIT_query(r) - BIT_query(l-1)
    for ans in ANS:
        print(ans)

if __name__ == '__main__':
    main()
