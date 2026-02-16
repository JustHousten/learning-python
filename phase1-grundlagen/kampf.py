# while-Schleife - läuft solange eine Bedingung erfüllt ost
spieler_hp = 100
gegner_hp = 80
spieler_schaden = 16
gegner_schaden = 20
runde = 1

print("--- Kampf beginnt ---")

while gegner_hp > 0 and spieler_hp > 0:
    gegner_hp -= spieler_schaden
    spieler_hp -= gegner_schaden
    print(f"Runde {runde}:")
    print(f"    Du triffst für {spieler_schaden} - Gegner HP: {max(0, gegner_hp)}")
    print(f"    Gegner trifft für {gegner_schaden} - Deine HP: {max(0, spieler_hp)}")
    runde += 1

print("\n--- Kampf Ende ---")

if spieler_hp > 0 and gegner_hp <= 0:
    print("Du hast gewonnen!")
elif gegner_hp <= 0 and spieler_hp <= 0:
    print("Unentschieden - ihr habe euch gegenseitig besiegt!")
else:
    print("Du wurdest besiegt!")
