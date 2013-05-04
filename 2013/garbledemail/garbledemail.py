INFINITY = 10000


class Node(object):
    def __init__(self, letter=None, leaf=False):
        self.letter = letter
        self.leaf = leaf
        self.children = {}

    def add(self, word, pos=0):
        if pos >= len(word):
            self.leaf = True
        else:
            if word[pos] not in self.children:
                self.children[word[pos]] = Node(word[pos])
            self.children[word[pos]].add(word, pos + 1)

    def search(self, word, pos=0):
        if pos >= len(word):
            return self.leaf
        elif word[pos] not in self.children:
            return False
        else:
            return self.children[word[pos]].search(word, pos + 1)

    def __repr__(self):
        return 'Node(%r, %r)' % (self.letter, self.leaf)


def create_trie():
    trie = Node()
    words = [line[:-1] for line in file('garbled_email_dictionary.txt')]
    for word in words:
        trie.add(word)
    return trie


def garbled_email(s, trie):
    dp = [[INFINITY] * 5 for _ in range(len(s) + 1)]
    dp[0][4] = 0

    def search(node, pos, d, start_pos, start_d, errors):
        if node.leaf:
            dp[pos][d] = min(dp[pos][d], dp[start_pos][start_d] + errors)
        if pos >= len(s):
            return
        for letter in node.children:
            if letter == s[pos]:
                search(node.children[letter], pos + 1, min(d + 1, 4), start_pos, start_d, errors)
            elif d == 4:
                search(node.children[letter], pos + 1, 0, start_pos, start_d, errors + 1)

    # print dp
    for pos in range(len(s)):
        for d in range(5):
            if dp[pos][d] == INFINITY:
                continue
            search(trie, pos, d, pos, d, 0)
            # print dp
    return min(dp[-1])


def read_numbers(line):
    if line[-1] == '\n':
        line = line[:-1]
    return [int(x) for x in line.split()]


if __name__ == '__main__':
    import sys

    trie = create_trie()

    case_count = int(sys.stdin.readline()[:-1])
    for i in range(1, case_count + 1):
        s = sys.stdin.readline()[:-1]
        print "Case #{}: {}".format(i, garbled_email(s, trie))
