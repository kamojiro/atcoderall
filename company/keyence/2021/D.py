#import sys
#input = sys.stdin.readline
def main():
    N = int(input())
    # print((2**N-1)//2)
    a = "A"
    D = 2**N
    K = D-1
    L = K//2
    Z = K
    if N >= 3:
        
    ANS = [["A"]+["B"]*K for _ in range(Z)]
    for j in range(K):
        for i in range(L):
            ANS[(i+j)%K][j+1] = a
    print(K)
    print("\n".join(["".join(ans) for ans in ANS]))
    print(N)
if __name__ == '__main__':
    main()
