#import sys
#input = sys.stdin.readline
def main():
    N = int( input())
    ANS = []
    for _ in range(N):
        a, b, c, d = input().split()
        if a == "<":
            ANS.append((0, int(b), int(c), int(d)))
        else:
            ANS.append((1, int(b), int(c), int(d)))
    ans = 0
    for a in range(11):
        for b in range(11):
            L = [0]*(100000)
            L[0] = a
            L[1] = b
            for t, i, j , k in ANS:
                if t == 0:
                    if L[i] < L[j]:
                        L[k] = 1
                    else:
                        L[k] = 0
                else:
                    L[k] = L[i]+L[j]
            print(a, b, L[2])
            if a*b == L[2]:
                ans += 1
    print(ans, 121)
if __name__ == '__main__':
    main()
