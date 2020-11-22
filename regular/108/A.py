#import sys
#input = sys.stdin.readline
def factors(N): #約数を全て求める。ただし、順不同
    from collections import deque
    ret = deque()
    middle = int( N**(1/2))
    for i in range(1, middle):
        if N%i == 0:
            ret.append(i)
            ret.append(N//i)
            
    if N%middle == 0:
        ret.append(middle)
        if middle != N//middle:
            ret.append(N//middle)
    return ret

def main():
    S, P = map(int,input().split())
    F = factors(P)
    for p in F:
        if p + P//p == S:
            print("Yes")
            return
    print("No")
if __name__ == '__main__':
    main()
