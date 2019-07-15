#import sys
#input = sys.stdin.readline
from collections import Counter
def main():
    N = int( input())
    A = list( map( int, input().split()))
    CA = Counter(A)
    d = dict()
    if len(CA) > 3:
        print("No")
        return
    if len(CA) == 1:
        if CA[0] == N:
            print("Yes")
            return
        else:
            print("No")
            return
    if len(CA) == 2:
        for c in CA:
            if c != 0:
                t = c
        if N%3 == 0 and CA[t]== CA[0]*2:
            print("Yes")
        else:
            print("No")
        return
    ans = "Yes"
    s = 0
    for c in CA:
        s ^= c
        if CA[c] != N//3:
            ans = "No"
    if s != 0:
        ans = "No"
    print(ans)
if __name__ == '__main__':
    main()
