import sys
try:
    n=int(sys.argv[1])
except (IndexError, ValueError):
    print ("Lūdzu, ievadiet derīgu skaitli!")
    sys.exit()
rules = {3: "Fizz", 5: "Buzz", 7: "Jazz", 11: "Puzz"}
for i in range (1, n+1):
    result = ""
    for divisor in rules:
        if i % divisor == 0:
            result += rules [divisor]
    if result == "":
        print(i)
    else:
        print (result)