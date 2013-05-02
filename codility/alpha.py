def solution ( A ):
    remaining = set(A)
    for i, e in enumerate(A):
        remaining.discard(e)
        if len(remaining) == 0:
            return i
