#import sys
#input = sys.stdin.readline
def main():
    X = input()
    s = 0
    ans = len(X)
    for x in X:
        if x == 'S':
            s += 1
        else:
            if s > 0:
                s -= 1
                ans -= 2
    print(ans)
if __name__ == '__main__':
    main()








