sukupuoli = input("Anna biologinen sukupuoli (mies/nainen): ").lower()
arvo = int(input("Anna hemoglobiiniarvo (g/l): "))

# Tarkistetaan sukupuolen mukaan
if sukupuoli == "nainen":
    if arvo < 117:
        print("Hemoglobiiniarvo on alhainen.")
    elif arvo <= 175:
        print("Hemoglobiiniarvo on normaali.")
    else:
        print("Hemoglobiiniarvo on korkea.")
elif sukupuoli == "mies":
    if arvo < 134:
        print("Hemoglobiiniarvo on alhainen.")
    elif arvo <= 195:
        print("Hemoglobiiniarvo on normaali.")
    else:
        print("Hemoglobiiniarvo on korkea.")
else:
    print("Virheellinen sukupuoli.")
