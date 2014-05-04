import sys
from collections import deque


def war(naomi, ken):
    naomi = list(sorted(naomi, reverse=True))
    ken = list(sorted(ken, reverse=True))

    while len(ken) > 0:
        while len(ken) > 0 and ken[-1] < naomi[-1]:
            ken.pop()
        if len(ken) > 0:
            naomi.pop()
            ken.pop()

    return len(naomi)


def naive_war(naomi, ken):
    naomi = list(sorted(naomi, reverse=True))
    ken = deque(sorted(ken, reverse=True))

    points = 0
    while len(naomi) > 0:
        n, k = naomi[-1], ken[-1]
        if n > k:
            naomi.pop()
            ken.pop()
            points += 1
        else:
            naomi.pop()
            ken.popleft()
    return points


def deceitful_war(naomi, ken):
    naomi = list(sorted(naomi, reverse=True))
    ken = list(sorted(ken))

    max_points = naive_war(naomi, ken)
    while len(naomi) > max_points:
        naomi.pop()
        ken.pop()
        max_points = max(max_points, naive_war(naomi, ken))

    return max_points


def read_floats(line=None):
    if line is None:
        line = sys.stdin.readline()
    return [float(x) for x in line.split()]


if __name__ == '__main__':
    case_count = int(sys.stdin.readline()[:-1])
    for i in range(1, case_count + 1):
        _ = read_floats()
        naomi = read_floats()
        ken = read_floats()
        print "Case #%d: %d %d" % (i, deceitful_war(naomi, ken), war(naomi, ken))
