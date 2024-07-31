def delete_nth(order,max_e):
    dictionary = {}
    result = []

    for element in order:
        if element in dictionary:
            dictionary[element] +=1

        else:
            dictionary[element] = 1
        if not dictionary[element] > max_e:
            result.append(element)

    return result
        