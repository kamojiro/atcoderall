A, B, C = map( int, input().split() )
K = int(input())
print(A + B + C - max(A,B,C) + max(A,B,C)*(2**K))
