import sys

# definice úvodních binárních sekvencí obrázkových souborů
jpeg_header = b'\xff\xd8'
gif_header1 = b'GIF87a'
gif_header2 = b'GIF89a'
png_header = b'\x89PNG\r\n\x1a\n'


def read_header(file_name, header_length):
    """
    Tato funkce načte binární soubor z cesty file_name.
    Vrátí: binární data hlavičky (bytes) nebo None v případě chyby.
    """
    try:
        with open(file_name, 'rb') as f:
            header = f.read(header_length)
            return header
    except Exception:
        return None


def is_jpeg(file_name):
    """
    Funkce zkusí přečíst ze souboru hlavičku JPEG a porovná ji.
    Vrátí True, pokud je soubor JPEG, jinak False.
    """
    header = read_header(file_name, len(jpeg_header))

    if header is None:
        return False
        
    return header == jpeg_header


def is_gif(file_name):
    """
    Funkce zkusí přečíst ze souboru hlavičku GIF a porovná ji.
    Vrátí True, pokud je soubor GIF, jinak False.
    """
    header = read_header(file_name, len(gif_header1))

    if header is None:
        return False

    return header == gif_header1 or header == gif_header2


def is_png(file_name):
    """
    Funkce zkusí přečíst ze souboru hlavičku PNG a porovná ji.
    Vrátí True, pokud je soubor PNG, jinak False.
    """
    header = read_header(file_name, len(png_header))

    if header is None:
        return False

    return header == png_header


def print_file_type(file_name):
    """
    Funkce vypíše typ souboru. Zde je místo pro zpracování chyb.
    """

    if is_jpeg(file_name):
        print(f'Soubor {file_name} je typu **JPEG**')
    elif is_gif(file_name):
        print(f'Soubor {file_name} je typu **GIF**')
    elif is_png(file_name):
        print(f'Soubor {file_name} je typu **PNG**')
    else:
        print(f'Soubor {file_name} je **neznámého typu**')


if __name__ == '__main__':
    try:
        if len(sys.argv) < 2:
            raise IndexError("Chybí argument! Spusťte: python <název_skriptu>.py <cesta_k_souboru>")

        file_name = sys.argv[1]
        print_file_type(file_name)


    except Exception as e:
        print(f"Nastala neočekávaná chyba: {e}")