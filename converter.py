KM_TO_MI = 0.621371
KG_TO_LB = 2.20462
L_TO_GAL = 0.264172
USD_TO_EUR = 0.84235020
print ("Izvēlies konversiju: 1) km<->mi 2) kg<->lb 3) L<->gal 4) USD<->EUR")
izvēle = input ("> ")
if izvēle == "1":
    print ("Izvēlies virzienu: 1) km -> mi 2) mi -> km")
    virziens = input ("> ")
    if virziens == "1" or virziens == "2":
        try:
            value = float(input("Ievadi vērtību: "))
            if virziens == "1":
                result = value * KM_TO_MI
                print (f"{value:.2f} km = {result:.2f} mi")
            elif virziens == "2":
                result = value / KM_TO_MI
                print (f"{value:.2f} mi = {result:.2f} km")
        except ValueError:
            print ("Kļūda: Ievadi skaitli!")
    else:
        print ("Kļūda: Lūdzu, ievadi 1 vai 2!")
elif izvēle == "2":
    print ("Izvēlies virzienu: 1) kg -> lb 2) lb -> kg")
    virziens = input ("> ")
    if virziens == "1" or virziens == "2":
        try:
            value = float(input("Ievadi vērtību: "))
            if virziens == "1":
                result = value * KG_TO_LB
                print (f"{value:.2f} kg = {result:.2f} lb")
            elif virziens == "2":
                result = value / KG_TO_LB
                print (f"{value:.2f} lb = {result:.2f} kg")
        except ValueError:
            print ("Kļūda: Lūdzu, ievadi skaitli!")
    else:
        print ("Kļūda: Lūdzu, ievadi 1 vai 2!")
elif izvēle == "3":
    print ("Izvēlies virzienu: 1) L -> gal 2) gal -> L")
    virziens = input ("> ")
    if virziens == "1" or virziens == "2":
        try:
            value = float(input("Ievadi vērtību: "))
            if virziens == "1":
                result = value * L_TO_GAL
                print (f"{value:.2f} L = {result:.2f} gal")
            elif virziens =="2":
                result = value / L_TO_GAL
                print (f"{value:.2f} gal = {result:.2f} L")
        except ValueError:
            print ("Kļūda: Lūdzu, ievadi skaitli!")
    else:
        print ("Kļūda: Lūdzu, ievadi 1 vai 2!")
elif izvēle == "4":
    print ("Izvēlies virzienu: 1) USD -> EUR 2) EUR -> USD")
    virziens = input ("> ")
    if virziens == "1" or virziens == "2":
        try:
            value = float(input("Ievadi vērtību: "))
            if virziens == "1":
                result = value * USD_TO_EUR
                print (f"{value:.2f} USD = {result:.2f} EUR")
            elif virziens == "2":
                result = value / USD_TO_EUR
                print (f"{value:.2f} EUR = {result:.2f} USD")
        except ValueError:
            print ("Kļūda: Lūdzu, ievadi skaitli!")
    else:
        print ("Kļūda: Lūdzu, ievadi 1 vai 2!")
else:
    print ("Kļūda: Lūdzu, ievadi skaitli no 1 līdz 4!")