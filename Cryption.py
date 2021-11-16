def cryption():
    text = input()
    alphavit = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    s_output = ''
    key = input()
    number_in_key = 0
    for simvol in text:
        if simvol.upper() in alphavit:
            key_simvol = key[number_in_key%(len(key))]
            number_in_key %= len(key)
            number_in_key += 1
            number_in_crypt = alphavit.index(simvol.upper()) + alphavit.index(key_simvol)+1
            if number_in_crypt > 33:
                number_in_crypt -= 33
            if simvol.lower() == simvol:
                s_output += alphavit[number_in_crypt-1].lower()
            else:
                s_output += alphavit[number_in_crypt-1]
        else:
            s_output += simvol
    return(s_output)