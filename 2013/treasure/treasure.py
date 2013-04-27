from collections import defaultdict


def treasure(initial, chests, chest_count):
    finish, transitions = find(initial, chests, chest_count)
    if finish is None:
        return 'IMPOSSIBLE'
    else:
        return ' '.join(str(x + 1) for x in list(walk_transitions(transitions, finish))[:-1])


def walk_transitions(transitions, v):
    if transitions.get(v) is None:
        return []
    result = [transitions[v]]
    while True:
        r = transitions.get(v)
        if r is None:
            return reversed(result)
        v = r[1]
        result.append(r[0])


def find(initial, chests, chest_count):
    s = [(initial, tuple([0] * chest_count))]
    visited = set()
    transitions = {}

    while len(s) > 0:
        node, opened = s.pop()
        if all(x == 1 for x in opened):
            return (node, opened), transitions
        visited.add((node, opened))

        for key, key_count in enumerate(reversed(node)):
            key = len(node) - key - 1
            if key_count > 0:
                for chest_number, new_keys in reversed(chests[key]):
                    l = list(node)
                    l[key] -= 1
                    o = list(opened)
                    if o[chest_number] == 0:
                        o[chest_number] = 1
                        for new_key in new_keys:
                            l[new_key - 1] += 1
                        l = tuple(l)
                        o = tuple(o)
                        if (l, o) not in visited:
                            transitions[(l, o)] = (chest_number, (node, opened))
                            s.append((l, o))
    return None, transitions


def generate_initial(starting_keys, n):
    result = [0] * (n + 1)
    for key in starting_keys:
        result[key - 1] += 1
    return tuple(result)


def read_numbers(line):
    if line[-1] == '\n':
        line = line[:-1]
    return [int(x) for x in line.split()]


if __name__ == '__main__':
    import sys
    case_count = int(sys.stdin.readline()[:-1])
    for i in range(1, case_count + 1):
        pattern = []
        key_count, chest_count = read_numbers(sys.stdin.readline())
        starting_keys = read_numbers(sys.stdin.readline())
        chests = defaultdict(list)
        for j in range(0, chest_count):
            row = read_numbers(sys.stdin.readline())
            chests[row[0] - 1].append((j, row[2:]))
        print "Case #{}: {}".format(i, treasure(generate_initial(starting_keys, 200), chests, chest_count))
