#import sys
#input = sys.stdin.readline
from collections import deque
def main():
    N = int(input())
    n = 0
    for k in range(1, 10**5):
        if N*2 == k*(k+1):
            n = k
            break
        if N*2 < k*(k+1):
            print("No")
            return
    ANS = [[n] for _ in range(n+1)]
    cnt = 1
    for i, p in enumerate(range(n,0,-1)):
        for t in range(p):
            ANS[i].append(cnt+t)
        for t in range(p):
            ANS[i+1+t].append(cnt+t)
        cnt += p
    print("Yes")
    print(len(ANS))
    print("\n".join([" ".join(map(str,ans)) for ans in ANS]))
if __name__ == '__main__':
    main()
