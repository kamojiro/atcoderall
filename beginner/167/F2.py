import sys
input = sys.stdin.readline
def main():
    N = int( input())
    S = [input().strip() for _ in range(N)]
    Up = []
    Down = []
    for s in S:
        now = 0
        m = 0
        for t in s:
            if t == "(":
                now += 1
            else:
                now -= 1
            if now < m:
                m = now
            # print(t, now)
        if now >= 0:
            Up.append((m,now))
        else:
            Down.append((m-now,-now))
    up = 0
    Up.sort(reverse=True)
    for m, inc in Up:
        if up+m < 0:
            print("No")
            return
        up += inc
    
    down = 0
    Down.sort(reverse=True)
    # print(Up, Down)
    for m, dec in Down:
        if down+m < 0:
            print("No")
            return
        down += dec
    if up != down:
        print("No")
        return
    print("Yes")
    
if __name__ == '__main__':
    main()
