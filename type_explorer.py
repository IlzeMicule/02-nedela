# Mainīgo definēšana
vārds = "Dainis"
vecums = 24
augums = 1.85
ir_students = True
adrese = None
# Datu tipu pārbaude
print ("vārds", type (vārds))
print ("vecums", type (vecums))
print ("augums", type (augums))
print ("ir_students", type (ir_students))
print ("adrese", type (adrese))
print ("Vai vārds un vecums ir vienādi datu tipi?", type (vārds) == type (vecums))
#Virkņu savienošana - Python ļauj savienot tekstu (str) ar tekstu (str), bet neļauj ar citiem datu tipiem
print ("8" + "3") # teksts + teksts
print ("Līgums Nr." + "71") # teksts + teksts
print (int ("8") + 3) #11, jo teksts "8" tiek konvertēts par skaitli (int) un tiek saskaitīts ar otru skaitli (int)
# Truthy / falsy piemēri
print (bool (0)) # False, jo False = 0
print (bool (0.02)) # True - jebkurš skaitlis, kas nav 0 ir True
print (bool (256)) 
print (bool (-67))
print (bool ("0")) # True - jebkura netukša virkne ir True, šeit 0 ir teksts jeb virkne
print (bool ("Mājasdarbs"))
print (bool (" ")) # True - atstarpe ir simbols, tātad virkne nav tukša
print (bool ("")) # False - tukša virkne
print (bool ([])) # False - tukšs saraksts
print (bool ([1,2,3])) # True - skaitļu saraksts
print (bool (["pirmdiena", "otrdiena", "trešdiena"])) # True - teksta saraksts
print (bool (None)) # False
print (True + True) # 2 - bool ir int apakšklase, True = 1
print (False + False) # 0 - False = 0
print (True + False) # 1 - 1+0=1
# Jauktā aritmētika
print (True*9) #9 - True ir 1
print (False+12) #12 - False  ir 0
print (20/True)
#Skaitļu pārveidošana
print (int(14.176)) # pārveido decimālskaitli par veselu skaitli bez noapaļošanas
# print (int ("14.176")) izmet ValueError. Lai Python konvertētu tekstu (str) par veselu skaitli (int), tekstam ir jāizskatās pēc vesela skaitļa. Šajā gadījumā tas neizpildās, jo skaitlī ir punkts, kas ir decimālskaitļa (float) pazīme.
print (int (float ("14.176"))) # vispirms str tiek pārveidots par float, pēc tam float tiek pārveidots par int
print (float ("1e3")) # e nozīmē "reiz desmit pakapē", kāpinātājs šajā gadījumā ir 3
print (float ("0.1e2"))
# Peldošā komata (float) precizitātes problēma
print (0.1 + 0.2 == 0.3) # False, jo binārā sistēma, ko izmanto datori, nevar precīzi saglabāt skaitļus 0.1 un 0.2
print (round (0.1 + 0.2, 1) == 0.3) # to var labot ar noapaļošanu (round)
# Banker's rounding - apaļošana uz tuvāko pāra skaitli, lai izvairītos no uzkrātām apaļošanas kļūdām lielos aprēķinos
print (round (2.5)) #2, jo Python apaļo uz tuvāko pāra skaitli
print (round (3.5)) #4, jo tuvākais pāra skaitlis ir 4