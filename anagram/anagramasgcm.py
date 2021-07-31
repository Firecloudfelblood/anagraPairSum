def anagram(frase1, frase2):
    '''
    toma 2 fraces las convierte a diccionario ignorando los espacios y guines
     y las compara para ver si son anagramas
    :param frase1:
    :param frase2:
    :return:
    '''
    dic1 = create_dic(frase1)
    dic2 = create_dic(frase2)

    # algunas de las frases marcadas como anagramas no lo eran asi que deje este print para probarlo
    # print(frase1)
    # print(frase2)
    # print(dic1)
    # print(dic2)

    #los prints dentro del if son para indicar que resultado de acuerdo alos valores y llaves
    if dic1 == dic2:
        # print('\n\n*********Son anagramas***********\n\n')
        return True
    else:
        # print('\n\n*********NO Son anagramas***********\n\n')
        return False


def create_dic(frase):
    '''
    toma la frase y la combierte en un diccionario usando la letra como llave y
     sumando la cantidad de veces que se repite cada letra como valor
    :param frase: trae la frace a convertir a diccionario
    :return: regresa el diccionario
    '''
    #esta declaracion es para que el diccionario exista fuera del for
    dictionary = {}
    # aqui estoy quitando los espacios vacios y los guiones del string
    frase = frase.replace(' ', '').replace('-', '').lower()
    for i in frase:
        #reviso si la letra en i ya existe en el diccionario si es asi le agrego uno al valor actual,
        # de lo contrario inicializo la llave en uno
        if i in dictionary.keys():
            dictionary[i] = dictionary[i] + 1
        else:
            dictionary[i] = 1
    return dictionary


