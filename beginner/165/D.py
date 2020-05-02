
def main():
    A, B, N = map( int, input().split())
    def calc(x):
        return A*x//B-x//B*A

    if N < B:
        print(calc(N))
    else:
        print(calc(B-1))
if __name__ == '__main__':
    main()
