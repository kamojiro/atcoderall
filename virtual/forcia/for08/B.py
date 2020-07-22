#import sys
#input = sys.stdin.readline
def mod(n):
    if n > 0:
        return -(n//2), n%2
    elif n < 0:
        return (-n+1)//2 ,(-n)%2
    else:
        return 0,0
    
def main():
    N = int( input())
    if N == 0:
        print(0)
        return
    ANS = []
    while N != 0:
        N, b = mod(N)
        ANS.append(b)
    print("".join( map( str, ANS[::-1])))
        
if __name__ == '__main__':
    main()
