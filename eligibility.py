while True:
    try:
        vecums = int (input ("Ievadi vecumu: "))
        if vecums < 0:
            print ("Vecums nevar būt negatīvs. Mēģini vēlreiz.")
            continue
        break
    except ValueError:
        print("Kļūda: Lūdzu, ievadiet skaitli ar cipariem!")
while True:
    aplieciba = input ("Vai ir autovadītāja apliecība? (j/n): ").lower().strip()
    if aplieciba == "j" or aplieciba == "n":
        ir_aplieciba = aplieciba == "j"
        break
    else:
        print ("Lūdzu, ievadiet tikai 'j' vai 'n'!")
while True:
    students = input ("Vai ir students? (j/n): ")
    if students == "j" or students == "n":
        ir_students = students == "j"
        break
    else:
        print ("Lūdzu, ievadiet tikai 'j' vai 'n'!")
while True:
    veterans = input ("Vai ir veterāns? (j/n): ")
    if veterans == "j" or veterans == "n":
        ir_veterans = veterans == "j"
        break
    else:
        print ("Lūdzu, ievadiet tikai 'j' vai 'n'!")
var_balsot = vecums >= 18
var_iret = vecums >= 21 and ir_aplieciba
iemesls = ""
if not var_iret:
    if not ir_aplieciba:
        iemesls = " (nav apliecības)"
    elif vecums <21:
        iemesls = " (par jaunu)"
senioru_atlaide = vecums >= 65 or ir_veterans
studentu_atlaide = 16 <= vecums <= 26 and ir_students
print ("---")
rezultatu_logs = f"""
Balsošana:          {"Jā \u2713" if var_balsot else "Nē \u2717"}
Auto īre:           {"Jā \u2713" if var_iret else "Nē \u2717" + iemesls}
Senioru atlaide:    {"Jā \u2713" if senioru_atlaide else "Nē \u2717"}
Studentu atlaide:   {"Jā \u2713" if studentu_atlaide else "Nē \u2717"}
"""
print (rezultatu_logs)