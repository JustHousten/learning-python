def charakter_erstellen(name, klasse, level):
    if klasse == "Krieger":
        hp = level * 200
        schaden = level * 15
    elif klasse == "Magier":
        hp = level * 100
        schaden = level * 20
    else:
        hp = level * 150
        schaden = level * 30

    return {
        "name": name,
        "klasse": klasse,
        "level": level,
        "hp": hp,
        "hp_max": hp,
        "schaden": schaden,
        "gold": level * 100,
        "inventar": []
    }

def charakter_anzeigen(charakter):
    print(f"\n--- {charakter['name']} ---")
    print(f"Klasse:  {charakter['klasse']}")
    print(f"Level:   {charakter['level']}")
    print(f"HP:      {charakter['hp']}/{charakter['hp_max']}")
    print(f"Schaden: {charakter['schaden']}")
    print(f"Gold:    {charakter['gold']}")

held = charakter_erstellen("Housten", "Krieger", 10)
charakter_anzeigen(held)