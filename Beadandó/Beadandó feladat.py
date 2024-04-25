from datetime import datetime

class Szoba:
    def __init__(self, szobaszam, ar):
        self.szobaszam = szobaszam
        self.ar = ar

class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, 10000)

class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, 20000)

class Foglalas:
    def __init__(self, szobaszam, datum):
        self.szobaszam = szobaszam
        self.datum = datum

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []

    def add_szoba(self, szoba):
        self.szobak.append(szoba)

    def foglalas(self, szobaszam, datum):
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                return szoba.ar

    def lemondas(self, szobaszam, datum):
        pass  # Implementáld a lemondás metódust

    def listaz_foglalasok(self):
        pass  # Implementáld a foglalások listázását

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []
        self.foglalasok = []

    def add_szoba(self, szoba):
        self.szobak.append(szoba)

    def foglalas(self, szobaszam, datum):
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                foglalas = Foglalas(szobaszam, datum)
                self.foglalasok.append(foglalas)
                return szoba.ar
        return None  # Szoba nem található

    def lemondas(self, szobaszam, datum):
        for foglalas in self.foglalasok:
            if foglalas.szobaszam == szobaszam and foglalas.datum == datum:
                self.foglalasok.remove(foglalas)
                return True
        return False  # Foglalás nem található

    def listaz_foglalasok(self):
        for foglalas in self.foglalasok:
            print(f"Szoba: {foglalas.szobaszam}, Dátum: {foglalas.datum}")

def main():
    szalloda = Szalloda("Példa Szálloda")
    szalloda.add_szoba(EgyagyasSzoba("101"))
    szalloda.add_szoba(KetagyasSzoba("102"))
    szalloda.add_szoba(EgyagyasSzoba("103"))

    for i in range(5):
        szalloda.foglalas("101", datetime(2024, 3, i + 1))

    while True:
        print("\n1. Foglalás")
        print("2. Lemondás")
        print("3. Foglalások listázása")
        print("4. Kilépés")

        valasztas = input("Válasszon egy lehetőséget: ")

        if valasztas == "1":
            szobaszam = input("Adja meg a szobaszámot: ")
            datum_str = input("Adja meg a foglalás dátumát (YYYY-MM-DD formátumban): ")
            datum = datetime.strptime(datum_str, "%Y-%m-%d")
            ar = szalloda.foglalas(szobaszam, datum)
            if ar is not None:
                print(f"Foglalás sikeres. Ár: {ar}")
            else:
                print("Hiba: A szoba nem található vagy a foglalás dátuma érvénytelen.")
        elif valasztas == "2":
            szobaszam = input("Adja meg a szobaszámot: ")
            datum_str = input("Adja meg a foglalás dátumát (YYYY-MM-DD formátumban): ")
            datum = datetime.strptime(datum_str, "%Y-%m-%d")
            if szalloda.lemondas(szobaszam, datum):
                print("Lemondás sikeres.")
            else:
                print("Hiba: A foglalás nem található.")
        elif valasztas == "3":
            szalloda.listaz_foglalasok()
        elif valasztas == "4":
            break
        else:
            print("Érvénytelen választás.")

if __name__ == "__main__":
    main()