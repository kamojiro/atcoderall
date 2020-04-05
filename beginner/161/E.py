#import sys
#input = sys.stdin.readline
def main():
    N, K, C = map( int, input().split())
    S = input()
    T = [False]*N
    ANS = [1]*N
    for i in range(N):
        if S[i] == "o":
            T[i] = True
        else:
            ANS[i] = 0
    F = []
    i = 0
    now = 0
    D = [False]*N
    k = 0
    while i < N and k < K:
        if T[i]:
            F.append(i)
            D[i] = True
            i += C+1
            k += 1
        else:
            i += 1
    for i in range(N):
        if not D[i]:
            ANS[i] = 0
    # print(ANS, F)
    end = N-1
    for i in range(N-1,-1,-1):
        if T[i]:
            end = i
            break
    for m in F[::-1]:
        # print(m, end)
        if m < end:
            ANS[m] = 0
        if end == 0:
            break
        for j in range(end-C-1,-1,-1):
            # print(j,T[j])
            if T[j]:
                end = j
                break

    print("\n".join( map( str, [ i+1 for i in range(N) if ANS[i] == 1])))
            
    
if __name__ == '__main__':
    main()
