#import sys
#input = sys.stdin.readline
from itertools import permutations
def main():
    C = list(map( int, input().split()))
    S = [1, 2, 4,8]
    N = 4*int( input())
    ans = 10**20
    for P in permutations( range(4)):
        cost = 0
        left = N
        for i in P:
            cost += left//S[i]*C[i]
            left -= left//S[i]*S[i]
        if cost < ans:
            ans = cost
    print(ans)
if __name__ == '__main__':
    main()




