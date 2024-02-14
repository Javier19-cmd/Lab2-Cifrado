def xor_bin_strings(s_bin_list, key_bin_list):
    # Asegurarse de que la cadena s tenga la misma longitud que la llave
    while len(s_bin_list) < len(key_bin_list):
        s_bin_list += s_bin_list

    # Realizar la operación XOR, bit a bit
    result_bin_list = []
    for s_bin, key_bin in zip(s_bin_list, key_bin_list):
        xor_bin = ''.join('1' if b1 != b2 else '0' for b1, b2 in zip(s_bin, key_bin))
        result_bin_list.append(xor_bin)

    return result_bin_list