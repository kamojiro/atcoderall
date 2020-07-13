#import sys
#input = sys.stdin.readline
def main():
    N = int( input())
    ANS = [0]*(N+1)
    for x in range(1,101):
        for y in range(1,101):
            for z in range(1,101):
                t = x**2 + y**2 + z**2 +x*y + y*z + z*x
                if t <= N:
                    ANS[t] += 1
    print("\n".join( map(str, ANS[1:])))
if __name__ == '__main__':
    main()
