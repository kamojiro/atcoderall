#import sys
#input = sys.stdin.readline
def main():
    N, S = input().split()
    N = int(N)
    A = [0]*(N+1)
    T = [0]*(N+1)
    G = [0]*(N+1)
    C = [0]*(N+1)
    for i, s in enumerate(S):
        if s == "A":
            A[i+1] += 1
        elif s == "T":
            T[i+1] += 1
        elif s == "C":
            C[i+1] += 1
        else:
            G[i+1] += 1
        A[i+1] += A[i]
        C[i+1] += C[i]
        T[i+1] += T[i]
        G[i+1] += G[i]
    ans = 0
    for i in range(N-1):
        for j in range(i+2, N+1):
            a = A[j] - A[i]
            c = C[j] - C[i]
            g = G[j] - G[i]
            t = T[j] - T[i]
            if a == t and g == c:
                ans += 1
    print(ans)
if __name__ == '__main__':
    main()








