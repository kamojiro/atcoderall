#import sys
#input = sys.stdin.readline
def main():
    N = int( input())
    s = input()
    t = input()
    for i in range(N):
        check = True
        for j in range(N-i):
            if not s[i+j]  == t[j]:
                check = False
                break
        if check:
            print(i+N)
            return
    print(N*2)
if __name__ == '__main__':
    main()
