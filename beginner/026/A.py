#import sys
#input = sys.stdin.readline
def main():
    A = int( input())
    ans = 0
    for i in range(1,A):
        if ans < i*(A-i):
            ans = i*(A-i)
    print(ans)
if __name__ == '__main__':
    main()
