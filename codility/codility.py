def wire_burnouts(N, A, B, C):
    left = set([(0, n) for n in range(1, N)] + [(n, N - 1) for n in range(N - 1)])
    right = set([(n, 0) for n in range(1, N)] + [(N - 1, n) for n in range(N - 1)])
    connections = {}

    def add_edge(n, m, d):
        target = (n, m + 1) if d == 0 else (n + 1, m)
        shorten_path((n, m))
        shorten_path(target)
        if (((n, m) in left and target in right)
            or ((n, m) in right and target in left)):
            return False
        if connections.get((n, m)) is None:
            connections[(n, m)] = target
        elif connections.get(target) is None:
            connections[target] = (n, m)
        else:
            connections[(n, m)] = connections[target]
        return True

    def shorten_path((n, m)):
        parent = connections.get((n, m))
        if parent is not None:
            shorten_path(parent)
            if parent in left:
                left.add((n, m))
            elif parent in right:
                right.add((n, m))


    for t, (n, m, d) in enumerate(zip(A, B, C)):
        if not add_edge(n, m, d):
            return t

    return -1



if __name__ == '__main__':
    print wire_burnouts(4,
                        [0, 1, 1, 2, 3, 2, 1, 0, 0],
                        [0, 1, 1, 1, 2, 2, 3, 1, 0],
                        [0, 1, 0, 0, 0, 1, 1, 0, 1])

    print wire_burnouts(4,
                        [0],
                        [0],
                        [0])
