# Lektion 3: if/elif/else
# Python trifft Entscheidungen basierend auf Bedingungen

klasse = input("Wähle eine Klasse (Krieger/Magier/Bogenschütze):")

if klasse == "Krieger":
    print("Du hast den Krieger gewählt!")
elif klasse == "Magier":
    print("Du hast den Magier gewählt!")
elif klasse == "Bogenschütze":
    print("Du hast den Bogenschützen gewählt!")
else:
    print("Unbekannte Klasse!")

level = int(input("Wähle dein Startlevel (1-10): "))

if level <1 or level > 10:
    print("Ungültiges Level! Muss zwischen 1 und 10 sein.")
elif level <= 3:
    print("Du startest als Anfänger.")
elif level <=7:
    print("Du startest als Forgeschrittener.")
else:
    print("Du startest als Experte!")