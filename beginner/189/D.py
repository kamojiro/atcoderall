#import sys
#input = sys.stdin.readline
def main():
    N = int(input())
    S =[input() for _ in range(N)]
    true = 1
    false = 1
    for s in S:
        if s == "OR":
            true, false = 2*true + false, false
        else:
            true, false = true, true+false*2
    print(true)
if __name__ == '__main__':
    main()
