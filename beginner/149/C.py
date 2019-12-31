#import sys
#input = sys.stdin.readline
def eratosthenes(N):
    from collections import deque
    work = [True] * (N+1)
    work[0] = False
    work[1] = False
#    ret = []
    for i in range(N+1):
        if work[i]:
#            ret.append(i)
            for j in range(2* i, N+1, i):
                work[j] = False
    return work

def main():
    primes = eratosthenes(2*10**5)
    X = int( input())
    for i in range(X, 2*10**5):
        if primes[i]:
            print(i)
            return
if __name__ == '__main__':
    main()
