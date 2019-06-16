# import sys
# input = sys.stdin.readline
# def main():
N = int( input())
A = list( map( int, input().split()))
B = list( map( int ,input().split()))
dpOne = [0]*(N+1)
for i in range(3):
    a, b = A[i], B[i]
    for j in range(N-a+1):
        if dpOne[j+a] < dpOne[j]+b:
            dpOne[j+a] = dpOne[j]+b
donguri = N
for i in range(N+1):
    if donguri < N-i+dpOne[i]:
        donguri = N - i +dpOne[i]
K = donguri
dpTwo = [0]*(K+1)
for i in range(3):
    a, b  = A[i], B[i]
    for j in range(K-b+1):
        if dpTwo[j+b] < dpTwo[j]+a:
            dpTwo[j+b] = dpTwo[j]+a
ans = K
for i in range(K+1):
    if ans < K - i + dpTwo[i]:
        ans = K-i+dpTwo[i]
print( ans)
# if __name__ == '__main__':
#     main()
fpy
