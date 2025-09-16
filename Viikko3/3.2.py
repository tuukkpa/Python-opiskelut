luokka = input("Anna hyttiluokka (LUX, A, B, C): ")

# Muutetaan syöte isoiksi kirjaimiksi varmuuden vuoksi
luokka = luokka.upper()

# Tarkistetaan hyttiluokka ja tulostetaan kuvaus
if luokka == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif luokka == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif luokka == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif luokka == "C":
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka.")
