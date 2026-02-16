# Lektion 4: Schleifen
# for-Schleife - wiederholt etwas eine bestimmte Anzahl von Malen

for runde in range(1, 6):
    print(f"Runde: {runde}")

spieler_hp = 100
gegner_hp = 80
spieler_schaden = 15
gegner_schaden = 10

print("--- Kampf beginnt ---")

for runde in range (1, 6):
    gegner_hp -= spieler_schaden
    spieler_hp -= gegner_schaden
    print(f"Runde {runde}:")
    print(f"    Du triffst für {spieler_schaden} - Gegner HP: {gegner_hp}")
    print(f"    Gegner trifft für {gegner_schaden} - Deine HP: {spieler_hp}")
