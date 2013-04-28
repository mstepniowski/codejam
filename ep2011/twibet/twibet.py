import sys
sys.setrecursionlimit(10000)


def count_followers(i, followers, seen):
    result = 1
    seen.add(i)
    for follower in followers[i]:
        if not follower in seen:
            result += count_followers(follower, followers, seen)
    return result


def following_to_followers(following):
    followers = [[] for x in following]
    for m, f in enumerate(following):
        followers[f - 1].append(m)
    return followers


def twibet(monks):
    followers = following_to_followers(monks)
    result = []
    for i in range(len(followers)):
        seen = set()
        result.append(count_followers(i, followers, seen))
    return result


def read_numbers(line):
    if line[-1] == '\n':
        line = line[:-1]
    return [int(x) for x in line.split()]


if __name__ == '__main__':
    import sys
    case_count = int(sys.stdin.readline()[:-1])
    for i in range(1, case_count + 1):
        pattern = []
        monk_count = read_numbers(sys.stdin.readline())
        monks = read_numbers(sys.stdin.readline())
        print "Case #%d:" % i
        for x in twibet(monks):
            print x
