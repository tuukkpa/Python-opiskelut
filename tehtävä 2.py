import math
#2.1
nimi = input("Kerro nimesi:")
print("Terve, "+ nimi + "!")

#2.2
sade = float(input("Anna ympyrän säde: "))

pinta_ala = math.pi * sade**2

print(f"Ympyrän pinta-ala on {pinta_ala:.2f}")

#2.3
kanta = float(input("Anna suorakulmion kanta: "))
korkeus = float(input("Anna suorakulmion korkeus: "))

pinta_ala = kanta * korkeus
piiri = 2 * (kanta + korkeus)

print("Suorakulmion pinta-ala on:", pinta_ala)
print("Suorakulmion piiri on:", piiri)

#2.4

luku1 = int(input("Anna ensimmäinen kokonaisluku: "))
luku2 = int(input("Anna toinen kokonaisluku: "))
luku3 = int(input("Anna kolmas kokonaisluku: "))

summa = luku1 + luku2 + luku3
tulo = luku1 * luku2 * luku3
keskiarvo = summa / 3

print("Lukujen summa on:", summa)
print("Lukujen tulo on:", tulo)
print("Lukujen keskiarvo on:", keskiarvo)

#2.5
leiviskat = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

# Muutetaan kaikki luodeiksi
kokonaisluodit = leiviskat * 20 * 32 + naulat * 32 + luodit

# Lasketaan kokonaismassaksi grammoina
grammat = kokonaisluodit * 13.3

# Muutetaan kilogrammoiksi ja grammoiksi
kilot = int(grammat // 1000)          # Täydet kilogrammat
loput_grammat = grammat % 1000        # Jäljelle jäävät grammat

print("Massa nykymittojen mukaan:")
print(f"{kilot} kilogrammaa ja {loput_grammat:.2f} grammaa.")

#2.6
import random

# Kolmenumeroinen koodi (0–9)
koodi1 = ""
for i in range(3):
    koodi1 += str(random.randint(0, 9))

# Nelinumeroinen koodi (1–6)
koodi2 = ""
for i in range(4):
    koodi2 += str(random.randint(1, 6))

# Tulostetaan tulokset
print("Kolmenumeroinen koodi:", koodi1)
print("Nelinumeroinen koodi:", koodi2)
