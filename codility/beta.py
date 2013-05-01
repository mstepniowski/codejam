MAX_N = 10000000
START = 0
END = 1


class Node(object):
    def __init__(self, start, end, count=0, left=None, right=None):
        self.start = start
        self.end = end
        self.count = count
        self.left = left
        self.right = right
        self.parent = None

    def __repr__(self):
        return 'Node(%r, %r, %r, %r, %r)' % (self.start, self.end, self.count, self.left, self.right)

    def __lt__(self, other):
        return (self.start, self.end) < (other.start, other.end)

    def __eq__(self, other):
        return (self.start, self.end) == (other.start, other.end)

def create_segment_tree(nodes, start=0, end=None, parent=None):
    """Creates a new segment tree, given a sorted list of Nodes."""
    if end is None:
        end = len(nodes) - 1

    if start > end:
        return None
    elif start == end:
        root = nodes[start]
        root.parent = parent
        return root
    else:
        median = start + (end - start) / 2

        root = nodes[median]
        root.left = create_segment_tree(nodes, start, median - 1, root)
        root.right = create_segment_tree(nodes, median + 1, end, root)
        root.parent = parent
        return root

def add_node(tree, node):
    while node is not None:
        node.count += 1
        node = node.parent

def remove_node(tree, node):
    while node is not None:
        node.count -= 1
        node = node.parent

def count_starting_after(tree, start):
    if tree is None:
        return 0
    elif tree.start >= start:
        left_count = tree.left.count if tree.left is not None else 0
        right_count = tree.right.count if tree.right is not None else 0
        return count_starting_after(tree.left, start) + right_count + (1 if left_count + right_count < tree.count else 0)
    else:
        return count_starting_after(tree.right, start)


def solution(A):
    nodes = [Node(center - radius, center + radius) for (center, radius) in enumerate(A)]
    nodes.sort()
    tree = create_segment_tree(nodes)
    events = ([(node.start, START, node.end, node) for (i, node) in enumerate(nodes)]
              + [(node.end, END, node.start, node) for (i, node) in enumerate(nodes)])
    events.sort()

    result = 0
    for point, event, other_point, node in events:
        if event == START:
            add_node(tree, node)
        else:
            remove_node(tree, node)
            # for real discs (here we have circles):
            # result += count_starting_after(tree, node.start)
            result += tree.count
            if result > MAX_N:
                return -1

    return result


if __name__ == '__main__':
    print solution([1, 5, 2, 1, 4, 0]) # should == 11
