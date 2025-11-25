import sys
import requests
import re # Import pro regulární výrazy


def download_url_and_get_all_hrefs(url):
    """
    Funkce stahne url predanou v parametru url pomoci volani response = requests.get(),
    zkontroluje navratovy kod response.status_code, ktery musi byt 200,
    pokud ano, najdete ve stazenem obsahu stranky response.content vsechny vyskyty
    <a href="url">odkaz</a> a z nich nactete url, ktere vratite jako seznam pomoci return
    """
    hrefs = []
    
    
    href_regex = re.compile(r'<a\s+[^>]*?href\s*=\s*(["\'])(.*?)\1', re.IGNORECASE)

    print(f"Stahuji URL: {url}")
    try:
        response = requests.get(url, timeout=10) 
        
        if response.status_code == 200:
            print("Status code 200 - stranka stazena uspesne.")
            
            content = response.text 
            
            
            matches = href_regex.findall(content)
            
            for match in matches:
                hrefs.append(match[1])

            print(f"Nalezeno {len(hrefs)} potenciálních odkazů.")
            return hrefs
        else:
            print(f"Chyba při stahování. Status code: {response.status_code}")
            return [] 

    except requests.exceptions.RequestException as e:
        print(f"Chyba při stahování (Requests Exception): {e}")
        return []


if __name__ == "__main__":
    try:
        if len(sys.argv) < 2:
            print("Použití: python sixth.py <URL>")
            sys.exit(1)
            
        url = sys.argv[1]
        
        all_hrefs = download_url_and_get_all_hrefs(url)
        
        if all_hrefs:
            print("\n--- Nalezené odkazy (prvních 10) ---")
            for href in all_hrefs[:10]: 
                print(href)
            
            print(f"\nCelkem nalezeno: {len(all_hrefs)} odkazů.")
        else:
            print("Nebyly nalezeny žádné odkazy nebo došlo k chybě.")

    
    except Exception as e:
        print(f"Program skončil neočekávanou chybou: {e}")