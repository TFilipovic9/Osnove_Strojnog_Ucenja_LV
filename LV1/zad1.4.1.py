def total_euro(RadniSati, Satnica):
    total = RadniSati * Satnica
    print("Ukupno:", total, "eura")

rs = int(input("Radni sati: "))
eh = float(input("eura/h: "))
total_euro(rs,eh)
