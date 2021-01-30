#import sys
#input = sys.stdin.readline
def main():
    N, K = map(int, input().split())
    A = list(map(int,input().split()))
    ans = 0
    P = 3*10**5+1
    Nums = [0]*(P+1)
    for a in A:
        Nums[a] += 1
    ans = 0
    for i in range(P+1):
        K = min(K, Nums[i])
        ans += K
    print(ans)
if __name__ == '__main__':
    main()
