import random
import math

# 1. Lista proizvoda
proizvodi = ["Laptop", "Mis", "Tastatura", "Telefon", "Slusalice", "Punjac", "Tablet", "Monitor"]

# 2. Recnik
cene = {
    "Laptop": 950.99,
    "Mis": 19.99,
    "Tastatura": 49.99,
    "Telefon": 1300.00,
    "Slusalice": 200.00,
    "Punjac": 30.99,
    "Tablet": 650.99,
    "Monitor": 200.99
}

# 3. Ispis proizvoda i njihove cene
print("Svi proizvodi i njihove cene:")
for proizvod in proizvodi:
    print(f"{proizvod} - {cene[proizvod]:.2f} €")

# 4. Unos budzeta
budzet = float(input("Unesite vaš budžet: "))

print("Proizvodi koje možete da priuštite:")
for proizvod in proizvodi:
    if cene[proizvod] <= budzet:
        print(proizvod)

# 5. Najskuplji proizvod
def najskuplji_proizvod(podaci):
    return max(podaci, key=podaci.get)

najskuplji = najskuplji_proizvod(cene)
print("Najskuplji proizvod je:", najskuplji, "-", cene[najskuplji], "€")

# 6. Nasumican proizvod iz liste
random_proizvod = random.choice(proizvodi)
print("Korisniku je privukao pažnju proizvod:", random_proizvod)

# 7. Prosecna cena
prosek = sum(cene.values()) / len(cene)
zaokruzen_prosek = math.floor(prosek * 100) / 100
print("Prosečna cena proizvoda je:", zaokruzen_prosek, "€")

# 8. Broj prodatih komada
kolicine = [5, 20, 10, 7, 12, 6, 4, 8]

ukupan_prihod = 0
for i in range(len(proizvodi)):
    ukupan_prihod += cene[proizvodi[i]] * kolicine[i]

print("Ukupan prihod je:", ukupan_prihod, "€")

# 9. Dodavanje novog proizvoda
proizvodi.append("Sat")
cene["Sat"] = 350.00

print("Ažurirana lista proizvoda:")
for proizvod in proizvodi:
    print(proizvod)

# 10. Sortiranje
sortirani = sorted(cene.items(), key=lambda x: x[1])

print("Proizvodi sortirani po ceni:")
for proizvod, cena in sortirani:
    print(f"{proizvod} - {cena} €")