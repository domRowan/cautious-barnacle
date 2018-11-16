def checkMagazine(magazine, note):
    ransomNoteWords = {}

    for word in note:
        if word not in ransomNoteWords:
            ransomNoteWords[word] = 1
        else:
            ransomNoteWords[word] += 1

    return checkMagazineAgainstRansomNoteWords(magazine, ransomNoteWords)


def checkMagazineAgainstRansomNoteWords(magazine, ransomNoteWords):
    for word in magazine:
        if word in ransomNoteWords:
            if ransomNoteWords[word] > 1:
                ransomNoteWords[word] -= 1
            else:
                del ransomNoteWords[word]

    if len(ransomNoteWords) > 0:
        return "No"
    else:
        return "Yes"


note = ["give", "one", "grand", "today"]
magazine = ["give", "one", "grand", "today", "night"]

print(checkMagazine(magazine, note))
