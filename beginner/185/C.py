#import sys
#input = sys.stdin.readline
def main():
    L = int( input())
    ans = 1
    for i in range(L-1,L-12,-1):
        ans *= i
    for i in range(1,12):
        ans //= i
    print(ans)
if __name__ == '__main__':
    main()








