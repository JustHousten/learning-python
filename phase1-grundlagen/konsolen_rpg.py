import random

# --- Schritt 1: Charakter erstellen ---
def charakter_erstellen(name, klasse):
    if klasse == "Krieger":
        hp = 150
        schaden_min = 15
        schaden_max = 25
    elif klasse == "Magier":
        hp = 100
        schaden_min = 20
        schaden_max = 40
    elif klasse == "Bogenschütze":
        hp = 120
        schaden_min = 18
        schaden_max = 30
    else:
        print("Unbekannte Klasse - Krieger wird verwendet.")
        hp = 150
        schaden_min = 15
        schaden_max = 25

    return {
        "name": name,
        "klasse": klasse,
        "hp": hp,
        "hp_max": hp,
        "schaden_min": schaden_min,
        "schaden_max": schaden_max,
        "gold": 100,
        "inventar": ["Heiltrank", "Heiltrank"]
    }

name = input("Wie heißt dein Charakter? ")
klasse = input("Wähle eine Klasse (Krieger/Magier/Bogenschütze): ")
held = charakter_erstellen(name, klasse)

print(f"\nWillkommen, {held['name']} der {held['klasse']}!")
print(f"HP: {held['hp']} | Schaden: {held['schaden_min']}-{held['schaden_max']} | Gold: {held['gold']}")

# --- Schritt 2: Gegner erstellen ---
def gegner_erstellen():
    gegner_typen = [
        {"name": "Goblin", "hp": 50, "schaden_min": 5, "schaden_max": 10, "gold": 20},
        {"name": "Ork", "hp": 80, "schaden_min": 10, "schaden_max": 18, "gold": 35},
        {"name": "Troll", "hp": 120, "schaden_min": 15, "schaden_max": 25, "gold": 50},
    ]
    return random.choice(gegner_typen)

gegner = gegner_erstellen()
print(f"\nEin {gegner['name']} greift an!")
print(f"Gegner HP: {gegner['hp']} | Schaden: {gegner['schaden_min']}-{gegner['schaden_max']} | Gold: {gegner['gold']}")

# --- Schritt 3: Kampfsystem ---
def angriff_berechnen(angreifer):
    return random.randint(angreifer["schaden_min"], angreifer["schaden_max"])

def kampf(held, gegner):
    print(f"\n--- Kampf gegen {gegner['name']} beginnt ---")
    runde = 1

    while held["hp"] > 0 and gegner["hp"] > 0:
        # Held greift an
        schaden_held = angriff_berechnen(held)
        gegner["hp"] -= schaden_held
    
        # Gegner greift an
        schaden_gegner = angriff_berechnen(gegner)
        held["hp"] -= schaden_gegner

        print(f"Runde {runde}: Du triffst für {schaden_held} | Gegner trifft für {schaden_gegner}")
        print(f"  Deine HP: {max(0, held['hp'])} | Gegner HP: {max(0, gegner['hp'])}")
        runde += 1

    if held["hp"] > 0:
        gold_gewonnen = gegner["gold"]
        held["gold"] += gold_gewonnen
        print(f"\nDu hast gewonnen! +{gold_gewonnen} Gold")
        return True
    else:
        print(f"\nDu wurdest besiegt!")
        return False

kampf(held, gegner)

# --- Schritt 4: Heiltrank benutzen ---
def heiltrank_benutzen(held):
    if "Heiltrank" in held["inventar"]:
        held["inventar"].remove("Heiltrank")
        heilung = 50
        held["hp"] = min(held["hp"] + heilung, held["hp_max"])
        print(f"Du hast einen Heiltrank benutzt! +{heilung} HP → {held['hp']}/{held['hp_max']}")
    else:
        print("Keine Heiltränke mehr!")

heiltrank_benutzen(held)
heiltrank_benutzen(held)
heiltrank_benutzen(held)  # Beim dritten Mal sollte keine mehr da sein