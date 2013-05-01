from bisect import bisect

MAX_N = 10000000

def solution(A):
    starts = [center - radius for (center, radius) in enumerate(A)]
    ends = [center + radius for (center, radius) in enumerate(A)]
    starts.sort()
    ends.sort()

    result = 0
    for i, end in enumerate(ends):
        result += bisect(starts, end) - i - 1
        if result > MAX_N:
            return -1
    return result


if __name__ == '__main__':
    print solution([1, 5, 2, 1, 4, 0]) # should == 11
