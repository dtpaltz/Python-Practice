

def most_common_words(text, excluded):
    excluded = list(map(lambda w: w.lower(), excluded))
    text = text.lower()
    text = text.replace(".", "")
    text = text.replace("!", "")
    text = text.replace(";", "")
    text = text.replace(":", "")
    text = text.replace(",", " ")
    text = text.replace("'", " ")
    text = text.replace("  ", " ")
    text = text.replace("  ", " ")
    wordfreq = {}
    for word in text.split(' '):
        if word not in excluded:
            if word not in wordfreq:
                wordfreq[word] = 0
            wordfreq[word] += 1
    max_count = max(wordfreq.values())
    return list(dict((k, v) for k, v in wordfreq.items() if v == max_count).keys())


literatureText = "Jack and Jill went to the market to buy bread and cheese. Cheese is Jack's and Jill's favorite food."
wordsToExclude = ["and", "he", "the", "to", "is", "Jack", "Jill"]
print(most_common_words(literatureText, wordsToExclude))



