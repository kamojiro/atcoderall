#import sys
#input = sys.stdin.readline
def one(D, S):
    d = {"A":0, "B":1, "C":2}
    ANS = []
    for a, b in S:
        x = d[a]
        y = d[b]
        if D[x] == 0 and D[y] == 0:
            print("No")
            return
        if D[x] == 0:
            D[x] += 1
            D[y] -= 1
            ANS.append(a)
        else:
            D[x] -= 1
            D[y] += 1
            ANS.append(b)
    print("Yes")
    print("\n".join(ANS))
            
def two(D,S,N):
    d = {"A":0, "B":1, "C":2}
    e = {0:"A", 1:"B",2:"C"}
    ANS = []
    for i in range(N):
        a, b = S[i]
        x = d[a]
        y = d[b]
        if D[x] == 0 and D[y] == 0:
            print("No")
            return
        if D[x] == 0:
            D[x] += 1
            D[y] -= 1
            ANS.append(a)
        elif D[y] == 0: 
            D[x] -= 1
            D[y] += 1
            ANS.append(b)
        else: #(1,1)
            if i+1 > N-1:
                D[x] += 1
                D[y] -= 1
                ANS.append(a)
                continue
            if S[i] == S[i+1]:
                D[x] += 1
                D[y] -= 1
                ANS.append(a)
                continue
            if not a in S[i+1]:
                x,y = y, x
                a, b = b,a
            D[x] += 1
            D[y] -= 1
            ANS.append(a)
    print("Yes")
    print("\n".join(ANS))
    
def main():
    N, A, B, C = map( int, input().split())
    S = [ tuple( input()) for _ in range(N)]
    d = {"A":0, "B":1, "C":2}
    D = [A,B,C]
    ANS = []
    if sum(D) == 1:
        one(D, S)
        return
    if sum(D) == 2:
        two(D,S,N)
        return
    for a, b in S:
        x = d[a]
        y = d[b]
        if D[x] == 0 and D[y] == 0:
            print("No")
            return
        if D[x] == 0:
            D[x] += 1
            D[y] -= 1
            ANS.append(a)
        elif D[x] == 1:
            if D[y] == 0:
                D[x] -= 1
                D[y] += 1
                ANS.append(b)
            else:
                D[x] += 1
                D[y] -= 1
                ANS.append(a)
        else:
            D[x] -= 1
            D[y] += 1
            ANS.append(b)

    print("Yes")
    print("\n".join(ANS))
    
if __name__ == '__main__':
    main()
