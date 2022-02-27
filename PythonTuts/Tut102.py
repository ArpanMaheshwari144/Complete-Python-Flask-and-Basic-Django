def removeVowels(s):
    s = s.replace("a", "")
    s = s.replace("e", "")
    s = s.replace("i", "")
    s = s.replace("o", "")
    s = s.replace("u", "")
    s = s.replace("A", "")
    s = s.replace("E", "")
    s = s.replace("I", "")
    s = s.replace("O", "")
    s = s.replace("U", "")
    return s


print(removeVowels("ArpanMaheshwAri"))
