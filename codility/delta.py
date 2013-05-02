# Codility Delta challenge
# https://codility.com/demo/take-sample-test/delta2011/

def solution(A):
    if len(A) == 0:
        return 0
    max_value = max(A) ** 2
    possible_values = set([0])
    for e in A:
        new_possible = set([])
        for value in possible_values:
            if value - e >= -max_value:
                new_possible.add(value - e)
            if value + e <= max_value:
                new_possible.add(value + e)
        possible_values = new_possible
    return min(abs(value) for value in possible_values)


if __name__ == '__main__':
    print solution([1, 5, 2, -2]) # should == 0
