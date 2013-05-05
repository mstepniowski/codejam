# Codility Epsilon challenge
# https://codility.com/demo/take-sample-test/epsilon2011/
import random

START = -10000
END = 10000

def solution(A, B):
    # We want to choose an x that minimizes A_i * x + B_i \forall i
    #
    # We can treat each y = A_i * x + B_i as a line.  If we do that,
    # the problem becomes one of finding the line most distant from 0.
    lines = zip(A, B)

    minimum_f = [(start, A, B) for (start, end, A, B) in minimum(lines, START, END)]
    maximum_f = [(start, -A, -B) for (start, end, A, B) in minimum([(-A, -B) for (A, B) in lines], START, END)]

    minimum_f.reverse()
    maximum_f.reverse()

    x_min, A_min, B_min = minimum_f.pop()
    x_max, A_max, B_max = maximum_f.pop()
    x = x_min
    min_diff = A_max * x + B_max - A_min * x - B_min

    while len(minimum_f) > 0 or len(maximum_f) > 0:
        if len(minimum_f) > 0:
            next_x_min, _, _ = minimum_f[-1]
        else:
            next_x_min = END

        if len(maximum_f) > 0:
            next_x_max, _, _ = maximum_f[-1]
        else:
            next_x_max = END

        if next_x_min < next_x_max:
            x, A_min, B_min = minimum_f.pop()
        else:
            x, A_max, B_max = maximum_f.pop()

        min_diff = min(min_diff, A_max * x + B_max - A_min * x - B_min)

    return min_diff


def minimum(lines, start, end, epsilon=0.1 ** 9):
    # Lines in form (A, B) => f(x) = Ax + B
    y_start, A_start, B_start = min((A * start + B, A, B) for (A, B) in lines)
    end_points = [(A * end + B, A, B) for (A, B) in lines]
    y_end, A_end, B_end = min(end_points)
    if abs(A_start * end + B_start - y_end) < epsilon:
        return [(start, end, A_start, B_start)]
    else:
        # Line minimal at the start is not minimal at the end
        # Get a set of lines that have crossed
        y_start_end = A_start * end + B_start
        interesting_lines = [(A, B) for (y, A, B) in end_points if y < y_start_end]

        # Choose split point
        A_split, B_split = random.choice(interesting_lines)
        x_split = float(B_split - B_start) / (A_start - A_split)

        result = minimum(interesting_lines + [(A_start, B_start)], start, x_split, epsilon)
        result.extend(minimum(interesting_lines, x_split, end, epsilon))
        return result


if __name__ == '__main__':
    print solution([-1, 1, 0], [3, 0, 2]) # should == 0.5
