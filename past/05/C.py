#import sys
#input = sys.stdin.readline
def main():
    N = int( input())
    if N == 0:
        print("0")
        return
    a = ord("A")
    ans = ""
    while N > 0:
        if N%36 < 10:
            ans += str(N%36)
        else:
            ans += chr(a+N%36 - 10)
        N //= 36
    print(ans[::-1])
if __name__ == '__main__':
    main()
