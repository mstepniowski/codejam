import sys


def read_numbers(line=None):
    if line is None:
        line = sys.stdin.readline()
    return [int(x) for x in line.split()]


def number_to_bin(n):
    return [int(c) for c in bin(n)[2:].zfill(30)]


def lottery_slow(a, b, k):
    result = 0
    for x in range(a):
        for y in range(b):
            if x & y < k:
                result += 1
    return result


def lottery_dp(m, n, a, b, k, smaller_than_a, smaller_than_b, smaller_than_k):
    if n == 30:
        return int(smaller_than_a and smaller_than_b and smaller_than_k)

    memoized = m.get((n, smaller_than_a, smaller_than_b, smaller_than_k))
    if memoized is not None:
        return memoized

    result = 0
    for an in (0, 1):
        for bn in (0, 1):
            if ((smaller_than_a or an <= a[n])
                    and (smaller_than_b or bn <= b[n])
                    and (smaller_than_k or an & bn <= k[n])):
                result += lottery_dp(m, n + 1, a, b, k,
                                     smaller_than_a or an < a[n],
                                     smaller_than_b or bn < b[n],
                                     smaller_than_k or an & bn < k[n])

    # print '>>', n, smaller_than_a, smaller_than_b, smaller_than_k, result
    m[(n, smaller_than_a, smaller_than_b, smaller_than_k)] = result
    return result


def lottery(a, b, k):
    return lottery_dp({}, 0,
                      number_to_bin(a),
                      number_to_bin(b),
                      number_to_bin(k),
                      False, False, False)


if __name__ == '__main__':
    case_count = int(sys.stdin.readline()[:-1])
    for i in range(1, case_count + 1):
        a, b, k = read_numbers()
        print "Case #%d: %s" % (i, lottery(a, b, k))
