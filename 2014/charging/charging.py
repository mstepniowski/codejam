import sys
from collections import Counter


INFINITY = 10 ** 6


def read_numbers(line=None):
    if line is None:
        line = sys.stdin.readline()
    return [int(x) for x in line.split()]


def charging_chaos(outlets, devices, index=0):
    devices_counter = Counter(devices)
    min_switches = INFINITY
    for outlet in outlets:
        diff = devices[0] ^ outlet
        outlets_counter = Counter(o ^ diff for o in outlets)
        if devices_counter == outlets_counter:
            min_switches = min(min_switches, bin(diff).count('1'))
    return min_switches if min_switches < INFINITY else 'NOT POSSIBLE'


if __name__ == '__main__':
    case_count = int(sys.stdin.readline()[:-1])
    for i in range(1, case_count + 1):
        n, l = read_numbers()
        outlets = [int(s, 2) for s in sys.stdin.readline().split()]
        devices = [int(s, 2) for s in sys.stdin.readline().split()]
        print "Case #%d: %s" % (i, charging_chaos(outlets, devices))
