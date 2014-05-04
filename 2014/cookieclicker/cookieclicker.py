from decimal import *
getcontext().prec = 7

def cookieclicker(farm_cost, farm_production, cookies_needed):
    seconds_spent = 0.0
    production = 2.0
    seconds_needed = cookies_needed / production

    # build farms
    while cookies_needed > farm_cost:
        seconds_needed = cookies_needed / production
        seconds_needed_to_build_farm = farm_cost / production
        seconds_needed_after_building_farm = (cookies_needed / (production + farm_production))
        # print '#', seconds_spent, production
        if seconds_needed_to_build_farm + seconds_needed_after_building_farm < seconds_needed:
            seconds_spent += seconds_needed_to_build_farm
            production += farm_production
        else:
            break

    return seconds_spent + seconds_needed


def read_floats(line):
    if line[-1] == '\n':
        line = line[:-1]
    return [float(x) for x in line.split()]


if __name__ == '__main__':
    import sys
    case_count = int(sys.stdin.readline()[:-1])
    for i in range(1, case_count + 1):
        pattern = []
        c, f, x = read_floats(sys.stdin.readline())
        print "Case #%d: %.7f" % (i, cookieclicker(c, f, x))
