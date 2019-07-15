#import sys
#input = sys.stdin.readline
def main():
    Q = 2019
    L, R = map( int, input().split())
    if L%Q == 0:
        print(0)
        return
    if (L//Q+1)*Q <= R:
        print(0)
        return
    T = [0]*2019
    for i in range(L%Q, R%Q+1):
        T[i] = 1
    ans = 2018
    for i in range(Q-1):
        if T[i] == 0:
            continue
        for j in range(i+1,Q):
            if T[j] == 0:
                continue
            if i*j%Q < ans:
                ans = i*j%Q
    print(ans)
if __name__ == '__main__':
    main()
