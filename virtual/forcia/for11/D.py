#import sys
#input = sys.stdin.readline
def main():
    N = int( input())
    B = list( map( int, input().split()))
    A = [ (b,i+1) for i, b in enumerate(B)]
    # A = []
    # for i in range(N):
    #     A.append((B[i], i+1))
    A.sort(key=lambda x:x[0])
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
    
    for i in range(1,N+1):
        BIT_update(i,1)

    n = N-1
    ans = 0
    # print(BIT_query(4))
    for a, i in A[:-1]:
        left = BIT_query(i)-1
        right = n - left
        # print("a",a, i)
        # print(left, right)
        n -= 1
        BIT_update(i,-1)
        ans += min(left, right)
    print(ans)
        

    
if __name__ == '__main__':
    main()
