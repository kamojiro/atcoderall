#import sys
#input = sys.stdin.readline
def main():
    N, L = map(int,input().split())
    A = [-1] + list(map(int,input().split())) + [1]
    B = [-1] + list(map(int,input().split())) + [1]
    T = [0]*(N+2)
    R = [False]*(N+2)
    R[0] = True
    R[N+1] = True
    for i, t in enumerate(zip(A,B)):
        # print(t)
        a, b = t
        if a < b:
            T[i] = 1
        elif a > b:
            T[i] = -1
        else:
            R[i] = True
    # print(T)
    direction = 0
    stack = []
    ans = 0
    ABT = 
    for i in range(N+2):
        a, b, t = A[i], B[i], T[i]
        if t == 0:
            
        elif t > 0:
            if direction < 0:
                print(-1)
                return
            if direction > 0:

        else:
            if direction > 0:
                
                
if __name__ == '__main__':
    main()
