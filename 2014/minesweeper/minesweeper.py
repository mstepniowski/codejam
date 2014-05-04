import sys


def minesweeper(rows, columns, mines):



def read_ints(line=None):
    if line is None:
        line = sys.stdin.readline()
    return [int(x) for x in line.split()]


if __name__ == '__main__':
    case_count = int(sys.stdin.readline()[:-1])
    for i in range(1, case_count + 1):
        rows, columns, mines = read_ints()
        print "Case #%d:" % i
        print minesweeper(rows, columns, mines)



....
....
....
....

# Board 2xN -- can do [2, 4, 6, 8...]

# 16 i wiecej na planszy 4x4 - can always do!

CASES = [['XXXX.',
          'XXXX.',
          'XX...',
          'XX...'],
         ['XXXX.',
          'XXXX.',
          'XXX..',
          'XX...'],
         ['XXXXX',
          'XXXXX',
          'XX...',
          'XX...'],
         ['XXXXX',
          'XXXXX',
          'XXX..',
          'XX...'],
         ['XXXXX',
          'XXXXX',
          'XXX..',
          'XXX..'],
         ['XXXXX',
          'XXXXX',
          'XXXX.',
          'XXX..'],
         ['XXXXX',
          'XXXXX',
          'XXXXX',
          'XXX..'],
         ['XXXXX',
          'XXXXX',
          'XXXXX',
          'XXXX.'],
         ['XXXXX',
          'XXXXX',
          'XXXXX',
          'XXXXX]']]
