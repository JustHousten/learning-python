# Lektion 6: Listen
# Eine Liste ist eine geordnete Sammlung von Werten

inventar = ["Schwert", "Schild", "Heiltrank", "Lederrüstung"]

print(inventar)         # Gesamte Liste
print(inventar[0])      # Erstes Element
print(inventar[3])      # Viertes Element
print(len(inventar))    # Anzahl der Elemente
print(inventar[-1])

# Element hinzufügen
inventar.append("Zauberstab")
print(inventar)

# Prüfen ob etwas in der Liste ist
if "Heiltrank" in inventar:
    print("Du hast einen Heiltrank!")

# Durch die Liste loopen
for item in inventar:
    print(f"- {item}")

def item_hinzufuegen(inventar, item):
    inventar.append(item)
    print(f"{item} wurde zum Inventar hinzugefügt!")

def item_benutzen(inventar, item):
    if item in inventar:
        inventar.remove(item)
        print(f"Du hast {item} benutzt!")
    else:
        print(f"{item} ist nicht in deinem Inventar!")
    
def inventar_anzeigen(inventar):
    print("\n--- Inventar ---")
    for item in inventar:
        print(f"    -{item}")
    print(f"Gesamt: {len(inventar)} Items")

# Test

mein_inventar = ["Schwert", "Schild"]
item_hinzufuegen(mein_inventar, "Heiltrank")
item_hinzufuegen(mein_inventar, "Zauberstab")
inventar_anzeigen(mein_inventar)
item_benutzen(mein_inventar, "Heiltrank")
item_benutzen(mein_inventar, "Bogen")
inventar_anzeigen(mein_inventar)