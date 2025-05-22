class Konyv:
    def __init__(self, cim, mufaj, oldalak_szama, ev, ar):
        self.cim = cim
        self.mufaj = mufaj
        self.oldalak_szama = oldalak_szama
        self.ev = ev
        self.ar = ar

    def hossz(self):
        if self.oldalak_szama < 200:
            return "rövid"
        elif 200 < self.oldalak_szama < 600:
            return "közepes"
        else:
            return "hosszú"

konyvek = []
with open("konyvek-adatok.txt", "r", encoding="utf-8") as FILE:
    FILE.readline()
    for line in FILE:
        data = line.strip().split(";")
        konyv = Konyv(data[0], data[1], int(data[2]), int(data[3]), int(data[4]))
        konyvek.append(konyv)

#1. feladat
print(f"A listában {len(konyvek)} db könyv található.")
#2. feladat
genre_input_field = input("Írd ide a könyv műfaját: ")
genre_count = 0
sum_of_pages = 0
for row in konyvek:
    if row.mufaj == genre_input_field:
        sum_of_pages += row.oldalak_szama
        genre_count += 1
        
print(f"{genre_count} db könvy tartozik ebbe a műfajba")
#print(sum_of_pages)

#3. feladat
is_true = False
for row in konyvek:
    if 1600 <= row.ev < 1700 and row.mufaj == "színmű":
        is_true = True
if is_true:
    print("1600 és 1699 között van színmű műfajban írt könyv.")

#5. feladat
with open("negyezer-export.txt", "w", encoding="utf-8") as DESTINATION:
    for row in konyvek:
        if row.ar == 4000:
            DESTINATION.write(f"{row.cim} ({row.hossz()})\n")

        