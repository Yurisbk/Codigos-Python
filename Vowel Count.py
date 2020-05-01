def getCount(inputStr):
    num_vowels = 0
    for letra in inputStr:
        if letra.lower() == 'a' or letra.lower() == 'e' or letra.lower() == 'i' or letra.lower() == 'o' or letra.lower() == 'u':
            num_vowels = num_vowels + 1
    return num_vowels
print(getCount("abracadabra"))