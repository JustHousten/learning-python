def berechne_schaden(angriff, verteidigung):
    schaden = angriff - verteidigung
    return max(0, schaden)

def kampf(spieler_hp, spieler_angriff, gegner_hp, gegner_angriff):
    runde = 1
    print("--- Kampf beginnt ---")

    while spieler_hp > 0 and gegner_hp > 0:
        spieler_hp -= berechne_schaden(gegner_angriff, 0)
        gegner_hp -= berechne_schaden(spieler_angriff, 0)
        print(f"Runde {runde}: Spieler HP: {max(0, spieler_hp)}")
        runde += 1

    if spieler_hp > 0 and gegner_hp <= 0:
        return "Sieg"
    elif spieler_hp <= 0 and gegner_hp <= 0:
        return "Unentschieden"
    else:
        return "Niederlage"
    
ergebnis = kampf(100, 20, 80, 15)
print(f"\nErgebnis: {ergebnis}")