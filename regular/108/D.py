#import sys
#input = sys.stdin.readline
Q = 10**9+7
def calc(N):
    x, y = 1, 1
    t = 2
    while t < N:
        x, y = y, (x+y)%Q
        t += 1
    return x

def main():
    N = int( input())
    CAA = input()
    CAB = input()
    CBA = input()
    CBB = input()
    if N == 2:
        print(1)
        return
    S = CAA+CAB+CBA+CBB
    A = "A"
    B = "B"
    Power =["ABAA","BABA","BABB","BBAA"]
    Fibo = ["ABBA","BAAA","BBBA","BAAB"]
    if S in Power:
        print(pow(2,N-3,Q))
    elif S in Fibo:
        print(calc(N))
    else:
        print(1)
if __name__ == '__main__':
    main()
