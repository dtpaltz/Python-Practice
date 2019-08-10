

def migratoryBirds(arr):
    seen_ids = {}
    for i in arr:
        if i in seen_ids.keys():
            seen_ids[i] = seen_ids[i] + 1
        else:
            seen_ids[i] = 1

    max_val = max(seen_ids.values())
    max_id = max(seen_ids.keys())

    for b in range(max_id + 1):
        if b in seen_ids.keys() and seen_ids[b] == max_val:
            return b


migratoryBirds([1, 4, 4, 4, 5, 3])


