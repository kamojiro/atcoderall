#import sys
#input = sys.stdin.readline
from itertools import permutations
def main():
    N = int(input())
    ans = [0]*(N**2+1)
    for p in permutations(range(N)):
        a = 0
        for i in range(N):
            a += abs(i-p[i])
        ans[a] += 1
    print(ans)
if __name__ == '__main__':
    main()
    

