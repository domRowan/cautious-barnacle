def twoStrings(s1, s2):
    sortedS1 = sorted(s1)
    sortedS2 = sorted(s2)

    for width in range(0, len(sortedS1)):
        for pointer in range(0, len(sortedS1)):
            substringS1 = sortedS1[pointer: pointer + width + 1]
            substringS2 = sortedS2[pointer: pointer + width + 1]

            if substringS1 == substringS2:
                return "YES"

    return "NO"


def twoStrings_SLOW(s1, s2):
    s1SubStrings = getAllSubStrings(s1)
    s2SubStrings = getAllSubStrings(s2)

    for subString in s1SubStrings:
        if subString in s2SubStrings:
            return "YES"

    return "NO"


def getAllSubStrings(string):
    subStrings = {}
    for width in range(0, len(string)):
        for pointer in range(0, len(string)):
            subString = string[pointer:pointer + width + 1]
            subStrings[subString] = 1
    return subStrings


string1 = "thisIsMyString"

print(twoStrings(string1, "fooS"))
