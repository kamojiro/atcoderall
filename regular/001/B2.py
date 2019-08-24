#import sys
#input = sys.stdin.readline
def main():
    ans = 0
    a, b = map( int, input().split())
    c = abs(b-a)
    if c >= 10:
        ans += c//10
        c -= c//10*10
    if c <= 2:
        ans += c
    elif c <= 7:
        ans += 1 + abs(5-c)
    else:
        ans += 1 + 10-c

    print(ans)
if __name__ == '__main__':
    main()
