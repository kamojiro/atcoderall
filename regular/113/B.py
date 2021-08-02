#import sys
#input = sys.stdin.readline
def main():
    A, B, C = map(int,input().split())
    a = A%10
    # if a == 0 or a == 1 or a == 5 or a == 6:
    #     print(a)
    #     return
    P = [a, a*a%10]
    while P[0] != P[-1]:
        P.append(P[-1]*P[0]%10)
    # print(P)
    Q = len(P)-1
    b = pow(B,C,Q)
    if b == 0:
        print(pow(a,Q,10))
    else:
        print(pow(a,b,10))
if __name__ == '__main__':
    main()
