import random

def blocks():
    naomi = set(random.sample(range(2000), 1000))
    ken = set(range(2000)) - naomi
    return '%s\n%s' % (' '.join(str(b) for b in naomi), ' '.join(str(b) for b in ken))


if __name__ == '__main__':
    print 50
    for i in range(50):
        print 1000
        print blocks()
