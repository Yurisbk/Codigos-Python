x = 0
def duplicate_count(text):
    x = 0
    for letra in text:
        #print(letra)
        i = 0
        for segundaletra in text:
            #print(segundaletra)
            if letra == segundaletra:
                i = i + 1
            if i > 1 and x < 1:
                x = x + 1

    return x
print (x)
print(duplicate_count("indivisibility"))  