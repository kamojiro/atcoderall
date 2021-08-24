#import sys
#input = sys.stdin.readline
def main():
    N = int(input())
    for i in range(1,N+1):
        solve(i)
def solve(n):
    ret = 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i*i < j:
                continue
            if int(round((i**2 - j)**(1/2)))**2 == i**2-j:
                ret += 1
    print(ret)
                
if __name__ == '__main__':
    main()
