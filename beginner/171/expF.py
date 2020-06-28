#import sys
#input = sys.stdin.readline
def main():
    K = int( input())
    S = input()
    N = len(S)
    T = set()
    T.add(S)
    a = ord("a")
    for i in range(K):
        Z = set()
        n = N+i
        for t in T:
            for j in range(n+1):
                for k in range(4):
                    Z.add(t[:j] + chr(k+a) + t[ j:])
        # print(Z)
        print( len(Z))
        T = Z

if __name__ == '__main__':
    main()
