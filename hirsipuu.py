import random

class Sana:
    def __init__(self, tiedoston_nimi = "sanakirja.txt"):
        self.sanat = self.lataa_sanat(tiedoston_nimi)
        
    def lataa_sanat(self, tiedoston_nimi):
        try:
            with open(tiedoston_nimi) as tiedosto:
                return [rivi.strip() for rivi in tiedosto.readlines() if rivi.strip()]
        except FileNotFoundError:
            print(f"Virhe: Tiedostoa {tiedoston_nimi} ei löytynyt. Käytetään oletussanoja.")
            return["omena", "banaani", "kissa", "koira", "puhelin", "tietokone", "auto", "moottoripyörä"]
        
    def valitse_sana(self):
        return random.choice(self.sanat)