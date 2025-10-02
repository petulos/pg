
def sudy_nebo_lichy(cislo):
    if cislo % 2 == 0:

        return f"Číslo {cislo} je sude"
    else:

        return f"Číslo {cislo} je liche"
        


if __name__ == "__main__":
    sudy_nebo_lichy(5)
    sudy_nebo_lichy(1000000)