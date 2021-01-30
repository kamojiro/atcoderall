#import sys
#input = sys.stdin.readline
def main():
    N = int(input())
    A = list(map(int,input().split()))
    K = 2**N
    Nums = [ i+1 for i in range(K)]
    for i in range(N,1,-1):
        GA = []
        GNums = []
        for i in range(0,2**i,2):
            if A[i] < A[i+1]:
                GA.append(A[i+1])
                GNums.append(Nums[i+1])
            else:
                GA.append(A[i])
                GNums.append(Nums[i])
        A = GA
        Nums = GNums
    if A[0] < A[1]:
        print(Nums[0])
    else:
        print(Nums[1])
                
if __name__ == '__main__':
    main()
