#import sys
#input = sys.stdin.readline
def main():
    N = int( input())
    A = list(map(int,input().split()))
    B  = list(map(int,input().split()))
    ans = sum([ a*b for a, b in zip(A,B)])
    if ans == 0:
        print("Yes")
    else:
        print("No")
        
if __name__ == '__main__':
    main()
