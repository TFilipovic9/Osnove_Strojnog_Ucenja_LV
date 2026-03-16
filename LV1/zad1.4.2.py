try:
    ocjena = float(input("Unesite ocjenu: "))

    if ocjena > 1.0 or ocjena < 0.0:
        print("Greška pri upisu.")
    elif ocjena >= 0.9:
        print("Ocjena: A")
    elif ocjena >= 0.8:
        print("Ocjena: B")
    elif ocjena >= 0.7:
        print("Ocjena: C")
    elif ocjena >= 0.6:
        print("Ocjena: D")
    else: 
        print("Ocjena: F")
except ValueError:
    print("Niste unjeli ispravan broj.")

