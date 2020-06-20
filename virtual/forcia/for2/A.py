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
    N = int( input())
    ans = 0
    for m in factors(N):
        if m==1:
            continue
        if N//(m-1)*m == N:
            ans += m-1
    print(ans)
    
if __name__ == '__main__':
    main()
