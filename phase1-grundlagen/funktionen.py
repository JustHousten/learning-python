# Lektion 5: Funktionen
# Eine Funktion ist ein wiederverwendbarer Code-Block

def begruesse_spieler(name):
    print(f"Willkommen, {name}!")

begruesse_spieler("Housten")
begruesse_spieler("Krieger")
begruesse_spieler("Magier")

def berechne_hp(level, klasse):
    if klasse == "Krieger":
        hp = level * 200
    elif klasse == "Magier":
        hp = level * 100
    elif klasse == "Bogenschütze":
        hp = level * 150
    else:
        hp = level * 100
    return hp

krieger_hp = berechne_hp(5, "Krieger")
magier_hp = berechne_hp(5, "Magier")

print(f"Krieger HP: {krieger_hp}")
print(f"Magier HP: {magier_hp}")