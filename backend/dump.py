def target_subsequence(sequence, target):
    start = 0
    end = 0 # noninclusive
    total = 0
    while start < len(sequence) and end <= len(sequence):
        if total < target:
            total += sequence[end]
            end += 1
        elif total > target:
            total -= sequence[start]
            start += 1
        if total == target:
            return start, end

    return None


if __name__ == '__main__':
    sequence = [0, 1, 3, 0, 0, 0, 0, 1, 3]
    target = 7
    start, end = target_subsequence(sequence,target)
    print(sequence[start:end])
    target = 1000
    start, end = target_subsequence(sequence,target)
    print(sequence[start:end])

