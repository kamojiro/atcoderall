#import sys
#input = sys.stdin.readline
def main():
    N = int( input())
    S = input()
    t = "b"
    ans = -1
    for i in range(50):
        if t == S:
            ans = i
            break
        if (i+1)%3 == 1:
            t = "a" + t + "c"
        elif (i+1)%3 == 2:
            t = "c" + t + "a"
        else:
            t = "b" + t + "b"
    print(ans)
if __name__ == '__main__':
    main()
