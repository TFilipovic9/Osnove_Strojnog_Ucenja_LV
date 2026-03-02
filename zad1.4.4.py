import string

rjecnik = {}

with open("song.txt", "r", encoding="utf-8") as datoteka:
    for linija in datoteka:
        linija = linija.lower()
        linija = linija.translate(str.maketrans("", "", string.punctuation))
        
        rijeci = linija.split()
        
        for rijec in rijeci:
            if rijec in rjecnik:
                rjecnik[rijec] += 1
            else:
                rjecnik[rijec] = 1

rijeci_jednom = [rijec for rijec, broj in rjecnik.items() if broj == 1]

print("Broj riječi koje se pojavljuju samo jednom:", len(rijeci_jednom))
print("Riječi koje se pojavljuju samo jednom:")
for rijec in rijeci_jednom:
    print(rijec)