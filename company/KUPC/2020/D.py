#import sys
#input = sys.stdin.readline
def prime_factor(N): #素因数
    ret = 0
    middle = int( N**(1/2))
    for i in range(2, middle+1):
        if N%i == 0:
            return i
    return N

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


def solve(N, p):
    ANS = []
    q = N//p
    for i in range(p):
        ans = [q]
        t = N*(N-1)//2//p
        for j in range(q-1):
            num = j*p+(j+i)%p
            t -= num
            ans.append(num*2+1)
        if t < 0:
            return []
        ans.append(t*2+1)
        ANS.append(ans)
    return ANS

def solve2(N,p):
    q = N//p
    ANS = []
    print(q)
    for i in range(q):
        ans = [2, i*2+1, N*2-1-i*2]
        ANS.append(ans)
    print("\n".join([" ".join(map(str, ans)) for ans in ANS]))
    return
    

def main():
    # for i in range(2, 10):
    #     print(i, prime_factor(i))
    N = int(input())
    # p = prime_factor(N)
    # if p == N:
    #     print("impossible")
    #     return
    ANS = []
    for p in factors(N):
        if p == 1 or p == N:
            continue
        if p == 2:
            solve2(N,p)
            return
        ANS = solve(N,p)
        if ANS:
            print(N//p)
            break
    # if p == 2:
    #     print(q)
    #     for i in range(q):
    #         ans = [2, i*2+1, N*2-1-i*2]
    #         ANS.append(ans)
    #     print("\n".join([" ".join(map(str, ans)) for ans in ANS]))
    #     return
        
    # print(q)        
    # for i in range(p):
    #     ans = [q]
    #     t = N*(N-1)//2//p
    #     for j in range(q-1):
    #         num = j*p+(j+p//2+1+i)%p
    #         t -= num
    #         ans.append(num*2+1)
    #     ans.append(t*2+1)
    #     ANS.append(ans)
    if ANS:
        print("\n".join([" ".join(map(str, ans)) for ans in ANS]))
    else:
        print("impossible")
if __name__ == '__main__':
    main()
