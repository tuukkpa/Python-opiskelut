# Kysytään käyttäjältä kuhan pituus
pituus = int(input("Anna kuhan pituus senttimetreinä: "))

# Alin sallittu pituus
sallittu = 37

# Tarkistetaan, onko kuha alamittainen
if pituus < sallittu:
    puuttuu = sallittu - pituus
    print(f"Kuha on alamittainen. Laske se takaisin järveen! "
          f"Pituudesta puuttuu {puuttuu} cm.")
else:
    print("Kuha on sallittua pyyntimittaa, voit pitää sen.")
