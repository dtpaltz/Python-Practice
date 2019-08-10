

def designerPdfViewer(h, word):
    chars = split_word(word)
    max_h = 0
    for c in chars:
        idx = ord(c) - 97
        if h[idx] > max_h:
            max_h = h[idx]

    return max_h * len(word)


def split_word(word):
    return [char for char in word]








h1 = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
w1 = "abc"
print(designerPdfViewer(h1, w1))
