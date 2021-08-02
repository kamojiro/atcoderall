#import sys
#input = sys.stdin.readline
def main():
    N = int(input())
    for i in range(1000):
        if i*26 > N:
            break
        M = N - i*26
        for j in range(1000):
            if i*8 > M:
                break
            if (M-i*8)%10 == 0:
                print(i+(M-i*8)//10)
                return
    print(0)
if __name__ == '__main__':
    main()
