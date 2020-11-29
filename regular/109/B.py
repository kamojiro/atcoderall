#import sys
#input = sys.stdin.readline
def main():
    N = int(input())
    ans = N
    niN = (N+1)*2
    for i in range(int((2*N)**(1/2)), -1,-1):
        if i*(i+1) <= niN:
            print(ans-i+1)
            return
            
if __name__ == '__main__':
    main()
