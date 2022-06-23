def main():
    N = int( input())
    A = list(map(int, input().split()))
    if N == 1:
        print(A[0])
        return

    ans = [1<<31]
    orxor(N, A, 0, 0, ans)
    print(ans[0])

def orxor(N, A, i, ians, ans):
    if i == N:
        if ians < ans[0]:
            ans[0] = ians
        return
    a = 0
    for j in range(i, N):
        a |= A[j]
        orxor(N, A, j+1, ians^a, ans)

if __name__ == '__main__':
    main()