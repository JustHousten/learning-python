# Lektion 9: Fehlerbehandlung mit try/except

# Erinnerst du dich? Das ist abgestürzt:
# alter = int(input("Gib dein Alter ein: "))
# Wenn der Nutzer "hallo" eingibt → Absturz 

# Lösung:
try:
    alter = int(input("Gib dein Alter ein: "))
    print(f"Du bist {alter} Jahre alt.")
except ValueError:
    print("Das ist keine gültige Zahl! Bitte gib eine Zahl ein.")

def zahl_eingabe(frage, minimum, maximum):
    while True:
        try:
            wert = int(input(frage))
            if wert < minimum or wert > maximum:
                print(f"Bitte gib eine Zahl zwischen {minimum} und {maximum} ein.")
            else:
                return wert
        except ValueError:
            print("Ungültige Eingabe! Bitte gib eine Zahl ein.")

level = zahl_eingabe("Wähle dein Startlevel (1-10): ", 1, 10)
print(f"Du hast Level {level} gewählt.")