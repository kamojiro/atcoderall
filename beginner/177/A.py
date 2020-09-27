def main():
    D, T, S = map( int, input().split())
    if S*T >= D:
        print("Yes")
    else:
        print("No")
if __name__ == '__main__':
    main()
