#import sys
#input = sys.stdin.readline
def Primefactors(N):# Nより小さい自然数の素因数の個数と約数の個数を返すO(Nlog(N))
    Ints = [ i for i in range(N)]
    # Primefactors = [0]*N
    Factors = [1]*N
    for i in range(2, N):
        if Ints[i] == 1:
            continue
        for j in range(1, N):
            if i*j < N:
                t = 1
                while Ints[i*j]%i == 0:
                    Ints[i*j] //= i
                    # Primefactors[i*j] += 1
                    t += 1
                Factors[i*j] *= t
            else:
                break
    return Factors

def main():
    N = int( input())
    F = Primefactors(N+1)
    # print(F)
    ans = 0
    for i,x in enumerate(F):
        ans += i*x
    print(ans)
if __name__ == '__main__':
    main()
