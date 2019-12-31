# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10 ** 6)

dp = [[[-1]*301 for _ in range(301)] for _ in range(301)]

def memodp(i,j,k,N):
    if dp[i][j][k] >= 0:
        return dp[i][j][k]
    if i == 0 and j == 0 and k == 0:
        return 0
    res = N
    if i > 0:
        res += memodp(i-1,j,k,N)*i
    if j > 0:
        res += memodp(i+1,j-1,k,N)*j
    if k > 0:
        res += memodp(i,j+1,k-1,N)*k
    dp[i][j][k] = res/(i+j+k)
    return dp[i][j][k]
    
    
def main():
    N = int( input())
    A = list( map( int, input().split()))
    dishes = [0]*4
    for a in A:
        dishes[a] += 1
    print(memodp(dishes[1], dishes[2], dishes[3], N))
        
    
if __name__ == '__main__':
    main()
