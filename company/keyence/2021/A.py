#import sys
#input = sys.stdin.readline
def main():
    N = int(input())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    C = [A[0]*B[0]]
    a = A[0]
    for i in range(1,N):
        a = max(a, A[i])
        C.append(max(C[-1], a*B[i]))
    print("\n".join(map(str, C)))
if __name__ == '__main__':
    main()
