# Lektion 7: Dictionaries
# Ein Dictionary speichert Schlüssel-Wert-Paare

charakter = {
    "name": "Housten",
    "klasse": "Krieger",
    "level": 10,
    "hp": 2000,
    "gold": 5000
}

print(charakter)
print(charakter["name"])
print(charakter["level"])

# Wert ändern
charakter["level"] = 11
charakter["gold"] += 500
print(f"Level: {charakter['level']}, Gold: {charakter['gold']}")

# Neuen Schlüssel hinzufügen
charakter["erfahrung"] = 0
print(charakter["erfahrung"])

# Prüfen ob ein Schlüssel existiert
if "hp" in charakter:
    print(f"HP: {charakter['hp']}")

# Alle Schlüssel und Werte durchloopen
for schluessel, wert in charakter.items():
    print(f"{schluessel}: {wert}")