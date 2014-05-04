import sys


def read_numbers(line=None):
    if line is None:
        line = sys.stdin.readline()
    return [int(x) for x in line.split()]


def magictrick(numbers1, answer1, numbers2, answer2):
    possible_numbers = set(numbers1[answer1]) & set(numbers2[answer2])
    if len(possible_numbers) == 0:
        return 'Volunteer cheated!'
    elif len(possible_numbers) == 1:
        return possible_numbers.pop()
    else:
        return 'Bad magician!'


if __name__ == '__main__':
    case_count = int(sys.stdin.readline()[:-1])
    for i in range(1, case_count + 1):
        answer1 = read_numbers()[0] - 1
        numbers1 = [read_numbers() for _ in range(4)]
        answer2 = read_numbers()[0] - 1
        numbers2 = [read_numbers() for _ in range(4)]
        print "Case #%d: %s" % (i, magictrick(numbers1, answer1, numbers2, answer2))
