

def je_mimo_sachovnici(pozice):
    min_pozice= 1
    max_pozice = 8
    radek, sloupec = pozice
    return not (min_pozice <= radek <= max_pozice and min_pozice <= sloupec <= max_pozice)

def je_tah_pripustny_vez(puvodni_pozice, cilova_pozice):
    puvodni_radek, puvodni_sloupec = puvodni_pozice
    cilovy_radek, cilovy_sloupec = cilova_pozice
    return (puvodni_radek == cilovy_radek and puvodni_sloupec != cilovy_sloupec) or \
           (puvodni_radek != cilovy_radek and puvodni_sloupec == cilovy_sloupec)

def je_tah_pripustny_strelec(puvodni_pozice, cilova_pozice):
    puvodni_radek, puvodni_sloupec = puvodni_pozice
    cilovy_radek, cilovy_sloupec = cilova_pozice
    rozdil_radku = abs(puvodni_radek - cilovy_radek)
    rozdil_sloupcu = abs(puvodni_sloupec - cilovy_sloupec)
    return rozdil_radku == rozdil_sloupcu and puvodni_pozice != cilova_pozice

def je_cesta_volna(puvodni_pozice, cilova_pozice, obsazene_pozice):
    puvodni_radek, puvodni_sloupec = puvodni_pozice
    cilovy_radek, cilovy_sloupec = cilova_pozice

    rozdil_radku = cilovy_radek - puvodni_radek
    rozdil_sloupcu = cilovy_sloupec - puvodni_sloupec

    #  smer pohybu
    krok_radek = 0
    if rozdil_radku > 0:
        krok_radek = 1
    elif rozdil_radku < 0:
        krok_radek = -1

    krok_sloupec = 0
    if rozdil_sloupcu > 0:
        krok_sloupec = 1
    elif rozdil_sloupcu < 0:
        krok_sloupec = -1

    #vsechny pole 
    aktualni_radek, aktualni_sloupec = puvodni_radek + krok_radek, puvodni_sloupec + krok_sloupec
    while (aktualni_radek, aktualni_sloupec) != cilova_pozice:
        if (aktualni_radek, aktualni_sloupec) in obsazene_pozice:
            return False  
        aktualni_radek += krok_radek
        aktualni_sloupec += krok_sloupec

    return True  

def je_tah_mozny_strelec():
    pass

def je_tah_mozny_dama():
    pass

def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    """
    Ověří, zda se figurka může přesunout na danou pozici.

    :param figurka: Slovník s informacemi o figurce (typ, pozice).
    :param cilova_pozice: Cílová pozice na šachovnici jako n-tice (řádek, sloupec).
    :param obsazene_pozice: Množina obsazených pozic na šachovnici.
    
    :return: True, pokud je tah možný, jinak False.
    """
    typ_figurky = figurka["typ"]
    puvodni_pozice = figurka["pozice"]
    puvodni_radek, puvodni_sloupec = puvodni_pozice
    cilovy_radek, cilovy_sloupec = cilova_pozice
    
    
    if je_mimo_sachovnici(cilova_pozice) or puvodni_pozice == cilova_pozice:
        return False
        
    if cilova_pozice in obsazene_pozice:
        return False

    rozdil_radku = cilovy_radek - puvodni_radek
    rozdil_sloupcu = cilovy_sloupec - puvodni_sloupec
    
    
    if typ_figurky == "pěšec":
        if rozdil_sloupcu != 0 or rozdil_radku <= 0:
            return False
            
        if rozdil_radku == 1:
            return True
        elif rozdil_radku == 2 and puvodni_radek == 2:
            mezilehla_pozice = (puvodni_radek + 1, puvodni_sloupec)
            return mezilehla_pozice not in obsazene_pozice
        else:
            return False

    elif typ_figurky == "jezdec":
        if (abs(rozdil_radku) == 2 and abs(rozdil_sloupcu) == 1) or \
           (abs(rozdil_radku) == 1 and abs(rozdil_sloupcu) == 2):
            return True 
        return False

    elif typ_figurky == "věž":
        if je_tah_pripustny_vez(puvodni_pozice, cilova_pozice):
            return je_cesta_volna(puvodni_pozice, cilova_pozice, obsazene_pozice)
        return False
        
    elif typ_figurky == "střelec":
        if je_tah_pripustny_strelec(puvodni_pozice, cilova_pozice):
            return je_cesta_volna(puvodni_pozice, cilova_pozice, obsazene_pozice)
        return False
        
    elif typ_figurky == "dáma":
        if je_tah_pripustny_vez(puvodni_pozice, cilova_pozice) or \
           je_tah_pripustny_strelec(puvodni_pozice, cilova_pozice):
            return je_cesta_volna(puvodni_pozice, cilova_pozice, obsazene_pozice)
        return False

    elif typ_figurky == "král":
        if abs(rozdil_radku) <= 1 and abs(rozdil_sloupcu) <= 1:
            return True
        return False
        
    return False 


if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    print(f"Pěšec (2,2) -> (3,2): {je_tah_mozny(pesec, (3, 2), obsazene_pozice)}")  # True

    print(f"Pěšec (2,2) -> (4,2): {je_tah_mozny(pesec, (4, 2), obsazene_pozice)}")  # True/False (dle mé logiky True, dle poznámky False)
    print(f"Pěšec (2,2) -> (1,2): {je_tah_mozny(pesec, (1, 2), obsazene_pozice)}")  # False

    print(f"Jezdec (3,3) -> (4,4): {je_tah_mozny(jezdec, (4, 4), obsazene_pozice)}")  # False
    print(f"Jezdec (3,3) -> (5,4): {je_tah_mozny(jezdec, (5, 4), obsazene_pozice)}")  # False (obsazená pozice)
    print(f"Jezdec (3,3) -> (1,2): {je_tah_mozny(jezdec, (1, 2), obsazene_pozice)}")  # True
    print(f"Jezdec (3,3) -> (9,3): {je_tah_mozny(jezdec, (9, 3), obsazene_pozice)}")  # False

    print(f"Dáma (8,3) -> (8,1): {je_tah_mozny(dama, (8, 1), obsazene_pozice)}")  # False (blokuje (8,2))
    print(f"Dáma (8,3) -> (1,3): {je_tah_mozny(dama, (1, 3), obsazene_pozice)}")  # False (blokuje (6,3))
    print(f"Dáma (8,3) -> (3,8): {je_tah_mozny(dama, (3, 8), obsazene_pozice)}")  # True