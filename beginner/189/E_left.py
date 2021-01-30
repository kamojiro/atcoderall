import sys
input = sys.stdin.readline
# import numpy as np
from numpy import matrix


def main():
    N = int(input())
    XY = [tuple(map(int,input().split())) for _ in range(N)]
    M = int(input())
    Op = [tuple(map(int,input().split())) for _ in range(M)]
    Q = int(input())
    ABI = [tuple(list(map(int,input().split()))+[i]) for i in range(Q)]
    # print(ABI)
    ABI.sort(key=lambda x: x[0])
    ANS = [(0,0)]*Q
    index = 0
    while ABI[index][0] == 0:
        a, b, i = ABI[index]
        ANS[i] = XY[b-1]
        index += 1
    A = [[0]*3 for _ in range(3)]
    A[0][0] = 1
    A[1][1] = 1
    A[2][2] = 1
    A = matrix(A)
    Z  =matrix([[0,-1,0],[1,0,0],[0,0,1]])
    W = matrix([[0,1,0],[-1,0,0],[0,0,1]])
    for j, op in enumerate(Op):
        if op[0] == 1:
            T = Z
        elif op[0] == 2:
            T = W
        elif op[0] == 3:
            T = matrix([[-1,0,0],[0,1,0],[2*op[1],0,1]])
        elif op[0] == 4:
            T = matrix([[1,0,0],[0,-1,0],[0,2*op[1],1]])
        A = A.dot(T)
        # print(A)
        # print(A[0][0][0])
        while ABI[index][0] == j+1:
            a, b, i = ABI[index]
            x, y = XY[b-1]
            ANS[i] = (A[0,0]*x+A[1,0]*y+A[2,0], A[0,1]*x+A[1,1]*y+A[2,1])
            index += 1
            if index >= Q:
                break
        if index >= Q:
            break
    print("\n".join([" ".join(map(str, ans)) for ans in ANS ]))
        
if __name__ == '__main__':
    main()
