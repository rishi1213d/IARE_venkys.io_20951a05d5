def radix_sort(arr):
    RADIX = 10
    max_length = False
    tmp, placement = -1, 1

    while not max_length:
        max_length = True
        buckets = [list() for _ in range(RADIX)]

        for i in arr:
            tmp = i / placement
            buckets[int(tmp % RADIX)].append(i)
            if max_length and tmp > 0:
                max_length = False

        a = 0
        for b in range(RADIX):
            bucket = buckets[b]
            for i in bucket:
                arr[a] = i
                a += 1

        placement *= RADIX
    return arr
