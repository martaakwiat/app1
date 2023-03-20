# v.1.0 dzialajacej aplikacji

wiek = input("Podaj wiek użytkownika:")
#sprawdzenie czy wiek jest liczbą całkowitą
if wiek.isdigit() == False:
    exit("Wiek musi byc liczba calkowita. Zamykam aplikację")
wiek=int(wiek)
if wiek>=18 and wiek<=40:
    print("Witamy w apce. Mozesz kupować u nas alkohol")
elif wiek>40:
    print("Witamy w apce. Mozesz kupować u nas alkohol")
    print("Prosze korzystaj z produktów z umiarem")
else:
    exit("Jestes za młody/a na alkohol. Zapraszamy na disney/com :)")