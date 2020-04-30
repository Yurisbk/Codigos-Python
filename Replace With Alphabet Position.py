def alphabet_position(text):
    alphabet_numbers = []
    for letra in text:
        if type(letra) == str:
            x = ord(letra.lower()) - 96
            if '-' in str(x):
                pass
            else:
                alphabet_numbers.append(x)
        else:
            pass
    listToStr = ' '.join([str(numero) for numero in alphabet_numbers])    
    return str(listToStr)    
print(alphabet_position("The sunset sets at twelve o' clock."))