from unidecode import unidecode #it is necessary to install this library (type this into the terminal): python -m pip install unidecode

class Sifra:
    abc = 'aábcčdďeéěfghiíjklmnňoópqrřsštťuúůvwxyýzž'
    ABC = 'AÁBCČDĎEÉĚFGHIÍJKLMNŇOÓPQRŘSŠTŤUÚŮVWXYÝZŽ'
    def __init__(self, text, posun):
        self.vstup = text.strip()
        self.text = unidecode(text.strip())
        self.posun = posun
        self.vystup = ""

    @property
    def vstup(self):
        return self.__vstup
    
    @vstup.setter
    def vstup(self, text):
        self.__vstup = text

    @property
    def text(self):
        return self.__text
    
    @text.setter
    def text(self, text):
        self.__text = text
        
    @property
    def posun(self):
        return self.__posun
    
    @posun.setter
    def posun(self, posun):
        self.__posun = posun
   
    def sifrovani_zakl(self):
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
    
    def desifrovani_zakl(self):
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
    
    def sifrovani_cele(self):
        for znak in self.vstup:
            if znak in self.abc:
                nove_poradi = (self.abc.index(znak) + self.posun) % 41
                self.vystup += self.abc[nove_poradi]
            elif znak in self.ABC:
                nove_poradi = (self.ABC.index(znak) + self.posun) % 41
                self.vystup += self.ABC[nove_poradi]
            else:
                self.vystup += znak

        return self.vystup
    
    def desifrovani_cele(self):
        for znak in self.vstup:
            if znak in self.abc:
                nove_poradi = (self.abc.index(znak) - self.posun) % 41
                self.vystup += self.abc[nove_poradi]
            elif znak in self.ABC:
                nove_poradi = (self.ABC.index(znak) - self.posun) % 41
                self.vystup += self.ABC[nove_poradi]
            else:
                self.vystup += znak
                
        return self.vystup
    
    def export(self, moznost):
        nazev_souboru = input("Zadejte název výsledného souboru. Název souboru pište bez přípony, automaticky se vytvoří textový dokument: ")
        nazev_souboru += ".txt"
        with open(nazev_souboru, "w", encoding="utf-8") as e:
            if moznost == 1 or moznost == 3:
                e.write(f"CAESAROVA ŠIFRA\n\nPosun: {self.posun}\n\nPůvodní text: \n{self.vstup}\n\nZašifrovaný text: \n{self.vystup}")
            elif moznost == 2 or moznost == 4:
                e.write(f"CAESAROVA ŠIFRA\n\nPosun: {self.posun}\n\nPůvodní text: \n{self.vstup}\n\nDešifrovaný text: \n{self.vystup}")

while True:
    vstup = input("Zadejte název souboru s textem, který chcete zašifrovat nebo dešifrovat: ")
    try: 
        with open(vstup, "r", encoding="utf-8") as t:
            vstup = t.read()
            if not vstup.strip():
                print("Soubor je prázdný a nedá se tedy zašifrovat/dešifrovat. Zadejte prosím jiný název souboru.")
            else:
                break
    except FileNotFoundError:
        print("Soubor se nepodařilo najít. Zkontrolujte, zda je správně napsaný nabo zadejte celou cestu k souboru.")

while True: 
    moznost_sifry = input("Chcete text zašifrovat nebo dešifrovat?\n  1 - Zašifrovat podle klasické šifrovací abecedy\n  2 - Dešifrovat podle klasické šifrovací abecedy\n  3 - Zašifrovat podle české abecedy (s háčky, čárkami a bez ch)\n  4 - Dešifrovat podle české abecedy (s háčky, čárkami a bez ch)\nZadejte číslo podle operace, kterou chcete provést: ")
    try:
        moz = int(moznost_sifry)
        if 1 <= moz <= 4:
            break
        else: 
            print("Zadejte číslo od 1 do 4, ostatní možnosti nejsou platné.")
    except ValueError:
        print("Zadejte prosím číslo od 1 do 4, ostatní znaky nejsou platné.")

while True:
    volba_posunu = input("Zadejte hodnotu posunu: ")
    try:
        pos = int(volba_posunu)
        if moz == 1 or moz ==2:
            if pos % 26 == 0:
               print(f"Při posunu o {pos} by se text posunul na původní verzi. Zadejte prosím jinou hodnotu posunu.")
            else:
                break
        else: 
            if pos % 41 == 0:
               print(f"Při posunu o {pos} by se text posunul na původní verzi. Zadejte prosím jinou hodnotu posunu.")
            else:
                break
    except ValueError:
        print("Zadaná hodnota není číslo!")

SIFRA = Sifra(vstup, pos)
if moz == 1:
    SIFRA.sifrovani_zakl()
elif moz == 2:
    SIFRA.desifrovani_zakl()
elif moz == 3:
    SIFRA.sifrovani_cele()
elif moz == 4:
    SIFRA.desifrovani_cele()

SIFRA.export(moz)
