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

#import sys
#input = sys.stdin.readline
def main():
    N = int(input())
    ANS = sorted(factors(N))
    print("\n".join(map(str,ANS)))
if __name__ == '__main__':
    main()
