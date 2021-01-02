#import sys
#input = sys.stdin.readline
def periodic(n, p):
    while n > 0:
        if n%p == 7:
            return False
        n //= p
    return True

def main():
    N = int( input())
    ans = 0
    for i in range(1,N+1):
        if periodic(i,8) and periodic(i,10):
            ans += 1
    print(ans)
    
if __name__ == '__main__':
    main()
