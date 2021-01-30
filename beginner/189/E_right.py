import sys
input = sys.stdin.readline
import numpy as np

def product(A,B):
    C = [[0]*3 for _ in range(3)]
    

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
    A = np.matrix(A)
    for j, op in enumerate(Op):
        if op[0] == 1:
            T = np.matrix([[0,1,0],[-1,0,0],[0,0,1]])

        elif op[0] == 2:
            T = np.matrix([[0,-1,0],[1,0,0],[0,0,1]])
        elif op[0] == 3:
            T = np.matrix([[-1,0,2*op[1]],[0,1,0],[0,0,1]])
        elif op[0] == 4:
            T = np.matrix([[1,0,0],[0,-1,2*op[1]],[0,0,1]])
        A = np.dot(T,A)
        # print(A)
        # print(A[0][0][0])
        while ABI[index][0] == j+1:
            a, b, i = ABI[index]
            x, y = XY[b-1]
            ANS[i] = (A[0,0]*x+A[0,1]*y+A[0,2], A[1,0]*x+A[1,1]*y+A[1,2])
            index += 1
            if index >= Q:
                break
        if index >= Q:
            break
    print("\n".join([" ".join(map(str, ans)) for ans in ANS ]))
        
if __name__ == '__main__':
    main()
