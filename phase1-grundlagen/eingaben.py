# Lektion 2: Benutzereingaben
# input() hält das Programm an und wartet auf eine Eingabe

name = input("Wie heißt dein Charakter? ")
print(f"Willkommen, {name}")
alter = int(input(f"Wie alt bist du? "))
naechstes_jahr = alter + 1
print(f"Nächstes Jahr bist du {naechstes_jahr}")

# Kleines Projekt: Charakter-Creator
name = input("Wie heißt dein Charakter? ")
klasse = input("Wähle eine Klasse (Krieger/Magier/Bogenschütze):")
level = int(input("Startlevel (1-10:) "))

gold = level * 100

print(f"\n--- Dein Charakter ---")
print(f"Name:   {name}")
print(f"Klasse: {klasse}")
print(f"Level:  {level}")
print(f"Gold:   {gold}")