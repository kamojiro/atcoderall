#import sys
#input = sys.stdin.readline
def checkp(AB):
    for a, b in AB:
        if a <= 0 or b <= 0:
            continue
        for i, z in enumerate(AB):
            c, d = z
            if c == -1 and d == -1:
                continue
            if c > 0:
                h = b-a+c
                if d == -1:
                    AB[i][1] = h
                elif h != d:
                    print("No")
                    return
            if d > 0:
                h = d - (b-a)
                if c == -1:
                    AB[i][1] = h
                elif h != c:
                    print("No")
                    return

def main():
    N = int( input())
    AB = [ list(map(int,input().split())) for _ in range(N)]
    T = [0]*(N*2+1)
    nums = []
    for a, b in AB:
        if a > 0 and b > 0 and a >= b:
            print("No")
            return
        T[a] += 1
        T[b] += 1
    for t in T:
        if t >= 2:
            print("No")
            return

    # we may assume a < b or a = -1 or b = -1

    AB.sort(key=lambda x: x[0])
    checkp(AB)
    AB.sort(key=lambda x: x[0], reverse=True)
    checkp(AB)
    AB.sort(key=lambda x: x[1])
    checkp(AB)
    AB.sort(key=lambda x: x[1], reverse=True)
    checkp(AB)

    
    
                

    
        

if __name__ == '__main__':
    main()
