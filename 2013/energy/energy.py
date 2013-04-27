def max_element(l):
    m, idx = l[0], 0
    for i, e in enumerate(l[1:]):
        if e > m:
            m, idx = e, i + 1
    return m, idx


def energy(events, initial_energy, ending_energy, max_energy, regain):
    if len(events) == 0:
        return 0

    value, idx = max_element(events)
    stored_energy = max(0, ending_energy - (len(events) - idx) * regain)
    possible_energy = min(initial_energy + regain * idx, max_energy)
    expended_energy = possible_energy - stored_energy

    result = expended_energy * value
    result += energy(events[:idx], initial_energy, expended_energy + stored_energy, max_energy, regain)
    result += energy(events[idx + 1:], stored_energy + regain, ending_energy, max_energy, regain)

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
        initial, regain, n = read_numbers(sys.stdin.readline())
        events = read_numbers(sys.stdin.readline())
        regain = min(initial, regain)
        print "Case #%d: %d" % (i, energy(events, initial, 0, initial, regain))
