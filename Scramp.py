def scramble(clearText, seed = "15312135"):
    result = ""
    if len(seed) <= len(clearText):
        while len(seed) <= len(clearText):
            seed += seed
    for i in range(0, len(clearText)):
        temp = ord(clearText[i])
        temp += int(seed[i])
        result += chr(temp)
    return result


def crack(mixText, seed = "15312135"):
    result = ""
    if len(seed) <= len(mixText):
        while len(seed) <= len(mixText):
            seed += seed
    for i in range(0, len(mixText)):
        temp = ord(mixText[i])
        temp -= int(seed[i])
        result += chr(temp)
    return result

