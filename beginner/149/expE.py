#import sys
#input = sys.stdin.readline
def main():
    N, M = map( int, input().split())
    A = list( map( int, input().split()))
    t = []
    for a in A:
        for b in A:
            t.append(a+b)
    t.sort(reverse=True)
    print(t)
    print(t[:M])
    print(sum(t[:14]))
if __name__ == '__main__':
    main()






