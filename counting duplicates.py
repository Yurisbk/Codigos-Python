def duplicate_count(text):
    i = 0
    new_list = []
    repetidas = []
    for letra in text:
        if letra.lower() not in new_list:
            new_list.append(letra.lower())
        else:
           repetidas.append(letra.lower()) 

    for letra in new_list:           
        if letra.lower() in repetidas:
            i = i + 1

    return i
print(duplicate_count("Indivisibilities"))  
