from math import gcd
def eratosthenes(N):
    from collections import deque
    work = [True] * (N+1)
    work[0] = False
    work[1] = False
    ret = []
    for i in range(N+1):
        if work[i]:
            ret.append(i)
            for j in range(2* i, N+1, i):
                work[j] = False
    return ret

# def gcd(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a

def main():
    N = int( input())
    A = list( map( int, input().split()))
    g = A[0]
    for a in A:
        g = gcd(a, g)
    if g > 1:
        print("not coprime")
        return
    E = eratosthenes(10**3)
    EE = [0]*len(E)
    R = []
    for a in A:
        for i, e in enumerate(E):
            if a%e == 0:
                if EE[i] > 0:
                    print("setwise coprime")
                    return
                EE[i] = 1
            while a%e == 0:
                a //= e
        if a > 1:
            R.append(a)
    R.sort()
    for i in range(len(R)-1):
        if R[i] == R[i+1]:
            print("setwise coprime")
            return
    print("pairwise coprime")
    
    
if __name__ == '__main__':
    main()
