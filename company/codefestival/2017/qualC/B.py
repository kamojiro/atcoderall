#import sys
#input = sys.stdin.readline
def main():
    N = int( input())
    A = list( map( int, input().split()))
    ans_complement = 1
    for a in A:
        if a%2 == 0:
            ans_complement *= 2
    print( pow(3, N) - ans_complement)
    
if __name__ == '__main__':
    main()
