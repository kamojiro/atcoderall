#import sys
#input = sys.stdin.readline
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

def main():
    N = 10**5
    L = eratosthenes(N)
    ans = 0
    for i in range(N+1):
        if L[i]:
            ans += i
        if ans > 10**5:
            break
    print(i, ans)
if __name__ == '__main__':
    main()








