class Peli:
    def __init__(self):
        self.sana = "koira"
        self.arvattu = []
        self.max_vaarin = 6
        self.vaarat = 0
        self.oikeat_kirjainmet = set()
        self.hirsipuu_kuvat = ['''
            +---+
            |   |
                |
                |
                |
                |
            =========''', '''
            +---+
            |   |
            O   |
                |
                |
                |
            =========''', '''
            +---+
            |   |
            O   |
            |   |
                |
                |
            =========''', '''
            +---+
            |   |
            O   |
           /|   |
                |
                |
            =========''', '''
            +---+
            |   |
            O   |
           /|/  |
                |
                |
            =========''', '''
            +---+
            |   |
            O   |
           /|/  |
           /    |
                |
            =========''', '''
            +---+
            |   |
            O   |
           /|/  |
           / /  |
                |
            =========''']

    # Palauttaa sanan, jossa oikeat kirjaimet näkyvät ja muut ovat alaviivoja
    def näytettävä_sana(self):
        näytettävä_sana = ""
        for kirjain in self.sana:
            if kirjain in self.oikeat_kirjainmet:
                näytettävä_sana += kirjain
            else:
                näytettävä_sana += "_"
        return näytettävä_sana
    
    def tarkista_arvaus(self, arvaus):
        if arvaus.lower() in self.sana:
            self.oikeat_kirjainmet.add(arvaus.lower())
        else:
            self.vaarat += 1

    # Tarkistaa onko peli ohi
    def peli_ohi(self):
        if self.vaarat >= self.max_vaarin:
            print(self.hirsipuu_kuvat[self.vaarat])
            print("Hävisit pelin!")
            print("Oikea sana oli:", self.sana)
            return True
        elif self.näytettävä_sana() == self.sana:
            print("Voitit pelin!")
            return True
        return False
    
    # Pelin pääsilmukka
    def pelaa(self):
        while not self.peli_ohi():
            print(self.hirsipuu_kuvat[self.vaarat])
            print(self.näytettävä_sana())
            arvaus = input("Arvaa kirjain: ")
            if len(arvaus) != 1:
                print("Anna tasan yksi kirjain!")
                continue
            self.tarkista_arvaus(arvaus)

if __name__ == "__main__":
    peli = Peli()
    peli.pelaa()
