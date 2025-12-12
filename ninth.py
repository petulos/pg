def dec_to_bin(cislo):
    # funkce prevede cislo na binarni reprezentaci (cislo muze byt str i int!!!)
    # 7 -> "111"
    # 5 -> "101"
    #return "0"
    cislo = int(cislo)
    list = []
    if cislo == 0:
        return "0"
    
    while cislo > 0:
        zbytek_po_deleni = cislo % 2
        cislo = cislo // 2
        list.insert(0,zbytek_po_deleni)

    return "".join(map(str, list))

def test_bin_to_dec():
    assert dec_to_bin("0") == "0"
    assert dec_to_bin(1) == "1"
    assert dec_to_bin("100") == "1100100"
    assert dec_to_bin(101) == "1100101"
    assert dec_to_bin(127) == "1111111"
    assert dec_to_bin("128") == "10000000"