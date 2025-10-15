def cislo_text(cislo):
    # funkce zkonvertuje cislo do jeho textove reprezentace
    # napr: "25" -> "dvacet pět", omezte se na cisla od 0 do 100
    # udelat si seznamy jednotek, desitek, nactek, poslepovat to
    jednotky = {
        0: "nula",
        1: "jedna",
        2: "dva",
        3: "tři",
        4: "čtyři",
        5: "pět",
        6: "šest",
        7: "sedm",
        8: "osm",
        9: "devět"
    }

    teen = {
        10: "deset",
        11: "jedenáct",
        12: "dvanáct",
        13: "třináct",
        14: "čtrnáct",
        15: "patnáct",
        16: "šestnáct",
        17: "sedmnáct",
        18: "osmnáct",
        19: "devatenáct"
    }

    desitky = {
        20: "dvacet",
        30: "třicet",
        40: "čtyřicet",
        50: "padesát",
        60: "šedesát",
        70: "sedmdesát",
        80: "osmdesát",
        90: "devadesát"
    }
    n = int(cislo)

    if n < 10:
        return jednotky[n]
    
    elif n >= 10 and n < 20:
        return teen[n]
    
    elif n == 100:
        return "sto"
    
    elif n >= 20:
        
        des = (n // 10) * 10
        jed = n % 10
        text_desitky = desitky[des]
        text_jednotky = jednotky[jed]

        if jed == 0:
            return text_desitky
        
        finalni_cislo = text_desitky + " " + text_jednotky
        return finalni_cislo
    
    elif n not in desitky or n not in jednotky:
        if n == 100:
            return "sto"
        else:
            return "chybné číslo"

if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    text = cislo_text(cislo)
    print(text)
