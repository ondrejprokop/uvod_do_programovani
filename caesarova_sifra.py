from unidecode import unidecode #zde je potřeba nainstalovat knivonu pomocí: python -m pip install unidecode

class sifra:
    def __init__(self, text, posun):
        self.text = unidecode(text.strip())
        self.posun = posun
        self.vystup = ""

    @property
    def text(self):
        return self._text
    
    @text.setter
    def text(self, text):
        self._text = text
        
    @property
    def posun(self):
        return self._posun
    
    @posun.setter
    def posun(self, posun):
        self._posun = posun
   
    def sifrovani(self):
        for znak in self.text:
            if znak.isalpha():
                if znak.isupper():
                    pocatek = ord('A')
                else:
                    pocatek = ord('a')

                vysledek = (ord(znak) - pocatek + self.posun) % 26 + pocatek
                self.vystup += chr(vysledek)
            else:
                self.vystup += znak

        return self.vystup
    
    def desifrovani(self):
        for znak in self.text:
            if znak.isalpha():
                if znak.isupper():
                    pocatek = ord('A')
                else:
                    pocatek = ord('a')

                vysledek = (ord(znak) - pocatek - self.posun) % 26 + pocatek
                self.vystup += chr(vysledek)
            else:
                self.vystup += znak

        return self.vystup
    
    def export(self, moznost):
        nazev_souboru = input("Zadejte název výsledného souboru. Název souboru pište bez přípony, automaticky se vytvoří textový dokument: ")
        nazev_souboru += ".txt"
        with open(nazev_souboru, "w", encoding="utf-8") as e:
            if moznost == 1:
                e.write(f"CAESAROVA ŠIFRA\n\nPosun: {self.posun}\n\nPůvodní text: \n  {self.text}\n\nZašifrovaný text: \n  {self.vystup}")
            elif moznost == 2:
                e.write(f"CAESAROVA ŠIFRA\n\nPosun: {self.posun}\n\nPůvodní text: \n  {self.text}\n\nDešifrovaný text: \n  {self.vystup}")

while True:
    vstup = input("Zadejte název souboru s textem, který chcete zašifrovat nebo dešifrovat: ")
    try: 
        with open(vstup, "r", encoding="utf-8") as t:
            vstup = t.read()
            break
    except FileNotFoundError:
        print("Soubor se nepodařilo najít. Zkontrolujte, zda je správně napsaný nabo zadejte celou cestu k souboru.")

while True:
    volba_posunu = input("Zadejte hodnotu posunu: ")
    try:
        pos = int(volba_posunu)
        if pos % 26 == 0:
            print(f"Při posunu o {pos} by se text posunul na původní verzi. Zadejte prosím jinou hodnotu posunu.")
        else:
            break
    except ValueError:
        print("Zadaná hodnota není číslo!")
    
while True: 
    moznost_sifry = input("Chcete text zašifrovat nebo dešifrovat?\n  1 - Zašifrovat\n  2 - Dešifrovat\nZadejte číslo podle operace, kterou chcete provést: ")
    try:
        moz = int(moznost_sifry)
        if 1 <= moz <= 2:
            break
        else: 
            print("Zadejte 1 nebo 2, ostatní možnosti nejsou platné.")
    except ValueError:
        print("Zadejte prosím číslo 1 nebo 2, ostatní znaky nejsou platné.")

SIFRA = sifra(vstup, pos)
if moz == 1:
    SIFRA.sifrovani()
elif moz == 2:
    SIFRA.desifrovani()

SIFRA.export(moz)