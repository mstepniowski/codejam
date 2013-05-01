MAX_RESULT = 100000000

def manacher(text):
    # Manacher's algorithm
    # http://leetcode.com/2011/11/longest-palindromic-substring-part-ii.html
    text = '^#' + '#'.join(text) + '#$'

    P = [0] * len(text) # length of the longest palindrome centered at text[i]
    C = 0 # current center
    R = 0 # right edge of the palindrome most to the right

    for i in range(1, len(text) - 1):
        i_mirror = C - (i - C) # i mirrored via C axis
        P[i] = min(R - i, P[i_mirror]) if R > i else 0

        # Try to expand the palindrome centered at i
        while (text[i + 1 + P[i]] == text[i - 1 - P[i]]):
            P[i] += 1

        # If palindrome centered at i expand past R,
        # adjust center based on expanded palindrome.
        if (i + P[i] > R):
            C = i
            R = i + P[i]

    return P

def solution(text):
    P = manacher(text)
    return max(sum(p / 2 for p in P), MAX_RESULT)


if __name__ == '__main__':
    print solution('baababa') # should = 6
