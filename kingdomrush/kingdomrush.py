# http://code.google.com/codejam/contest/1645485/dashboard#s=p1
from collections import deque

def kingdomrush(l):        
    levels = []
    for i, (one_star, two_stars) in enumerate(l):
        levels.append({'index': i, 'reqs': one_star, 'stars': 1, 'upgrade': two_stars})
        levels.append({'index': i, 'reqs': two_stars, 'stars': 2, 'upgrade': two_stars})
    levels.sort(key=lambda l: l['reqs'])

    collected_levels = {}
    collected_count = 0
    stars = 0

    # Sorted by upgrade cost, reversed
    accesible_one_star_levels = []

    # Sorted by requirement cost
    unaccesible_one_star_levels = []

    def collect_level(level):
        collected = collected_levels.get(level['index'])
        if collected:
            collected_stars = max(0, level['stars'] - collected['stars'])
        else:
            collected_stars = level['stars']
        
        if collected_stars > 0:
            collected_levels[level['index']] = level

        # print "Collected %r, stars %d" % (level, stars + collected_stars)
        return collected_stars
    
    for level in levels:
        if level['stars'] == 1:
            if level['reqs'] > stars:
                unaccesible_one_star_levels.append(level)
            else:
                accesible_one_star_levels.append(level)
            continue
                
        if level['reqs'] > stars:
            # Two-star level has higher requirements than we meet
            # Need to play some one-star levels
            # print 'Need to work on level %r' % level
            
            unaccesible_one_star_levels.sort(key=lambda l: l['reqs'], reverse=True)
            while len(accesible_one_star_levels) > 0 and level['reqs'] > stars:
                accesible_one_star_levels.sort(key=lambda l: l['upgrade'])
                # print 'accesible_one_star_levels', accesible_one_star_levels
                one_star_level = accesible_one_star_levels.pop()
                collected_stars = collect_level(one_star_level)
                if collected_stars > 0:
                    collected_count += 1
                    stars += collected_stars
                while len(unaccesible_one_star_levels) > 0 and unaccesible_one_star_levels[-1]['reqs'] <= stars:
                    accesible_one_star_levels.append(unaccesible_one_star_levels.pop())                
                    
            if level['reqs'] > stars:
                return None

        stars += collect_level(level)
        collected_count += 1

    return collected_count


def read_numbers(line):
    if line[-1] == '\n':
        line = line[:-1]
    return [int(x) for x in line.split()]


if __name__ == '__main__':
    import sys
    case_count = int(sys.stdin.readline()[:-1])
    for i in range(1, case_count + 1):
        level_count = int(sys.stdin.readline()[:-1])
        levels = [read_numbers(sys.stdin.readline()) for j in range(level_count)]
        result = kingdomrush(levels)
        print "Case #{}: {}".format(i, result if result is not None else 'Too Bad')
        
