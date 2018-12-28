
def check_for_other_sock(candidate, ar):
    for i in ar:
        if i == candidate:
            ar.remove(i)
            return 1

    return 0


# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    no_of_pairs = 0

    while len(ar) > 1:
        candidate = ar[0]
        ar.remove(ar[0])
        no_of_pairs = no_of_pairs + check_for_other_sock(candidate, ar)

    return no_of_pairs


if __name__ == '__main__':
    n = int(input())

    ar = map(int, raw_input().rstrip().split())

    result = sockMerchant(n, ar)

    print result
