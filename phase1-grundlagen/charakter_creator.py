# Charakter-Creator
name = input("Wie heißt dein Charakter? ")
klasse = input("Wähle eine Klasse (Krieger/Magier/Bogenschütze): ")
level = int(input("Startlevel (1-10): "))

# Grundwerte
gold = level * 100

# Klassenspezifische Boni
if klasse == "Krieger":
    hp = level * 200
    schaden = level * 15
    bonus = "Schild"
elif klasse == "Magier":
    hp = level * 100
    schaden = level * 30
    bonus = "Zauberstab"
elif klasse == "Bogenschütze":
    hp = level * 150
    schaden = level * 20
    bonus = "Bogen"
else:
    print("Unbekannte Klase - Standardwerte werden verwendet.")
    hp = level * 100
    schaden = level * 10
    bonus = "Keine"

print(f"\n--- Dein Charakter ---")
print(f"Name:    {name}")
print(f"Klasse:  {klasse}")
print(f"Level:   {level}")
print(f"HP:      {hp}")
print(f"Schaden: {schaden}")
print(f"Gold:    {gold}")
print(f"Bonus:   {bonus}")