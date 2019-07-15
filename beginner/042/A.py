#import sys
#input = sys.stdin.readline
def main():
    A = list( map( int, input().split()))
    C = [0]*11
    for a in A:
        C[a] += 1
    if C[5] == 2 and C[7] == 1:
        print("YES")
    else:
        print("NO")
if __name__ == '__main__':
    main()
