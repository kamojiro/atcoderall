#import sys
#input = sys.stdin.readline
Q = 10**9+7
def main():
    N, K = map( int, input().split())
    A = list( map( int, input().split()))
    if K == 1:
        print(max(A))
        return
    positive = 0
    zero = 0
    negative = 0
    for a in A:
        if a > 0:
            positive += 1
        elif a == 0:
            zero += 1
        else:
            negative += 1
    # print(positive, negative, zero)
    # print(positive+negative, K)
    if positive+negative < K:
        print(0)
        return
    if positive == 0:
        if K%2 == 1:
            if zero > 0:
                print(0)
                return
            else:
                A.sort(reverse=True)
                ans = 1
                for a in A[:K]:
                    ans *= a
                    ans %= Q
                print(ans)
                return
        else:
            A.sort()
            ans = 1
            for a in A[:K]:
                ans *= a
                ans %= Q
            print(ans)
            return
    # if K == 2:
    #     if negative <= 1:
    #         A.sort(reverse=True)
    #         print(A[0]*A[1]%Q)
    #         return
    if negative <= 1:
        A.sort(reverse=True)
        ans = 1
        for a in A[:K]:
            ans *= a
            ans %= Q
        print(ans)
        return
    if K == negative + positive:
        if negative%2 == 1:
            if zero > 0:
                print(0)
                return
        ans = 1
        for a in A:
            if a != 0:
                ans *= a
                ans %= Q
        print(ans)
        return
    B = [(abs(a), a) for a in A]
    B.sort(reverse = True)
    minus = False
    minus_value = 0
    plus_value = 0
    ans = 1
    for b in B[:K]:
        ans *= b[0]
        ans %= Q
        if b[1] < 0:
            minus = not minus
            minus_value = b[0]
        elif b[1] > 0:
            plus_value = b[0]
    # print(plus_value, minus_value)
    if minus:
        ans_plus = ans_minus = ans
        plus_replaced_value = 0
        minus_replaced_value = 0
        if minus_value > 0:
            for b in B[K:]:
                if b[1] > 0:
                    ans_plus = ans*pow(minus_value,Q-2,Q)%Q*b[0]%Q
                    if plus_value == 0:
                        plus_replaced_value = b[0]
                    else:
                        plus_replaced_value = plus_value*b[0]
                    break
        if plus_value > 0:
            for b in B[K:]:
                if b[1] < 0:
                    ans_minus = ans*pow(plus_value,Q-2,Q)%Q*b[0]%Q
                    if minus_value == 0:
                        minus_replaced_value = b[0]
                    else:
                        minus_replaced_value = minus_value*b[0]
                    break
        if plus_replaced_value == 0 and minus_replaced_value == 0:
            pass
        elif plus_replaced_value < minus_replaced_value:
            ans = ans_minus
        else:
            ans = ans_plus
    # print(plus_replaced_value, minus_replaced_value)
    # print(ans, ans_minus, ans_plus)
    print(ans)
    
if __name__ == '__main__':
    main()
