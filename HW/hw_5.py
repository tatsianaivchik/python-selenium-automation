def first_unique(str_1):
    for letter in str_1:
        if str_1.lower().count(letter) == 1:
            return letter
    return ""

print(first_unique("Google"))
print(first_unique("Amazon"))
print(first_unique("xoxoxo"))