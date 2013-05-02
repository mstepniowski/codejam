INFINITY = 10 ** 12

def solution(well, rings):
    max_diameters = []
    min_diameter = INFINITY
    for diameter in well:
        min_diameter = min(diameter, min_diameter)
        max_diameters.append(min_diameter)

    result = 0
    for ring in rings:
        diameter = -1
        while ring > diameter:
            if len(max_diameters) == 0:
                return result
            diameter = max_diameters.pop()
        result += 1
    return result


if __name__ == '__main__':
    print solution([5, 6, 4, 3, 6, 2, 3], [2, 3, 5, 2, 4]) # should = 4
    print solution([19, 7, 18, 9, 5, 5, 9, 8, 11, 16, 19, 16], [7, 3, 2, 7, 6]) # should = 4
