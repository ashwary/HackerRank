def charoccurence(str):
    freq = {}
    for c in str:
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1

    return freq


print(charoccurence("aaabbbcefkfjdfjslfdf"))
