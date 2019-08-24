#import sys
#input = sys.stdin.readline
def main():
    M, D = map( int, input().split())
    ans = 0
    for i in range(1, M+1):
        if i == 1:
            continue
        for j in range(1,D+1):
            if j < 10:
                continue
            s = str(j)
            a, b = int(s[0]), int(s[1])
            if a < 2 or b < 2:
                continue
            if i == a*b:
                ans += 1
    print(ans)
if __name__ == '__main__':
    main()
