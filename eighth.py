def bin_to_dec(binarni_cislo):
    # funkce spocita hodnotu predavaneho binarniho cisla (binarni_cislo muze byt str i int!!!)
    # 111 -> 7
    # "101" -> 5
    bin_str = str(binarni_cislo)

    decimal_value = 0
    n = len(bin_str)

    for i, bit in enumerate(bin_str):
        if bit == "1":
            exponent = n-1-i

            decimal_value += 2 ** exponent
    return decimal_value
    


def test_bin_to_dec():
    assert bin_to_dec("0") == 0
    assert bin_to_dec(1) == 1
    assert bin_to_dec("100") == 4
    assert bin_to_dec(101) == 5
    assert bin_to_dec("010101") == 21
    assert bin_to_dec(10000000) == 128

