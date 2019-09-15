#import sys
#input = sys.stdin.readline
import heapq
def main():
    N, M = map( int, input().split())
    A = list( map( lambda x:-x, map( int, input().split())))
    heapq.heapify(A)
    for _ in range(M):
        a = heapq.heappop(A)
        a = -((-a)//2)
        heapq.heappush(A, a)
    print( -sum(A))
if __name__ == '__main__':
    main()
