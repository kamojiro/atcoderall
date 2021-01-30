#import sys
#input = sys.stdin.readline
def main():
    N = int( input())
    AB = [ tuple(map(int,input().split())) for _ in range(N)]
    sa= 0
    sb= 0
    A = []
    for i, z in enumerate(AB):
        a, b = z
        sa += a
        A.append(b+a*2)
    now = -sa
    # print(now)
    # if now > 0:
    #     print(0)
    #     return
    # A.sort(key=lambda x: x[0], reverse=True)
    A.sort(reverse=True)
    count = 0
    for a in A:
        now += a
        # print(now)
        count += 1
        if now > 0:
            print(count)
            return

if __name__ == '__main__':
    main()
