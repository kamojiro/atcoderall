#import sys
#input = sys.stdin.readline
def main():
    N, H = map( int, input().split())
    A, B, C, D, E = map( int, input().split())
    ans = A*N
    for i in range(N+1):
        cost = i*A
        manpuku = H + i*B
        if manpuku > (N-i)*E:
            if ans > cost:
                ans = cost
            break
        # j回質素
        # E*(N-i-j) > D*j+manpuku
        # E*(N-i)-manpuku > (D+E)*j
        hutsu = (E*(N-i)-manpuku+(D+E))//(D+E)
        # # if (E*(N-i)-manpuku)%(D+E) == 0:
        # #     hutsu += 1
        # print(i, hutsu)
        cost += hutsu*C
        # print(cost)
        if ans > cost:
            ans = cost
    print(ans)
if __name__ == '__main__':
    main()
