VOWELS =  ['a', 'e', 'i', 'o', 'u']


def hashv(word, base):
    n = len(word)
    return sum(ord(c) * base ** (n - i - 1)
               for (i, c) in enumerate(word))


def rabin_karp(haystack, needle, base=256):
    n = len(haystack)
    m = len(needle)
    haystack_h = hashv(haystack[:m], base)
    needle_h = hashv(needle, base)
    offsets = []

    for i in range(n - m + 1):
        if haystack_h == needle_h and haystack[i:i+m] == needle:
            offsets.append(i)
        if i < n - m:
            h = base * (haystack_h - (ord(haystack[i]) * base ** (m - 1)))
            haystack_h = h + ord(haystack[i+m])

    return offsets


def count_syllabes(word):
    return sum(1 for c in word if c in VOWELS)


def irregularexp(word):
    for i in range(len(word)):
        for j in range(i + 2, len(word)):
            guess = word[i:j]
            if count_syllabes(guess) < 2:
                continue
            offsets = rabin_karp(word, guess)
            if len(offsets) < 2:
                break
            if offsets[-1] > j and count_syllabes(word[j:offsets[-1]]) >= 1:
                return True

    return False


if __name__ == '__main__':
    import sys
    case_count = int(sys.stdin.readline()[:-1])
    for i in range(1, case_count + 1):
        word = sys.stdin.readline()[:-1]
        print "Case #%d: %s" % (i, "Spell!" if irregularexp(word) else "Nothing.")
