import random

class Charakter:
    def __init__(self, name, klasse):
        self.name = name
        self.klasse = klasse
        self.level = 1
        self.erfahrung = 0
        self.gold = 100
        self.inventar = ["Heiltrank", "Heiltrank"]

        if klasse == "Krieger":
            self.hp_max = 150
            self.schaden_min = 15
            self.schaden_max = 25
        elif klasse == "Magier":
            self.hp_max = 100
            self.schaden_min = 20
            self.schaden_max = 40
        elif klasse == "Bogenschütze":
            self.hp_max = 120
            self.schaden_min = 18
            self.schaden_max = 30
        
        self.hp = self.hp_max

    def anzeigen(self):
        print(f"\n--- {self.name} ({self.klasse}) ---")
        print(f"Level: {self.level} | EP: {self.erfahrung}/{self.level * 1000}")
        print(f"HP: {self.hp}/{self.hp_max}")
        print(f"Schaden: {self.schaden_min}-{self.schaden_max}")
        print(f"Gold: {self.gold}")
        print(f"Inventar: {self.inventar}")

    def angreifen(self):
        return random.randint(self.schaden_min, self.schaden_max)
    
    def schaden_nehmen(self, schaden):
        self.hp -= schaden
        if self.hp < 0:
            self.hp = 0
        print(f"{self.name} nimmt {schaden} Schaden! HP: {self.hp}/{self.hp_max}")

    def heiltrank_benutzen(self):
        if "Heiltrank" in self.inventar:
            self.inventar.remove("Heiltrank")
            heilung = 50
            self.hp += heilung
            if self.hp > self.hp_max:
                self.hp = self.hp_max
            print(f"{self.name} benutzt einen Heiltrank und heilt {heilung} HP! HP: {self.hp}/{self.hp_max}")
        else:
            print("Keine Heiltränke mehr im Inventar!")

    def erfahrung_sammeln(self, menge):
        self.erfahrung += menge
        print(f"{self.name} erhält {menge} Erfahrungspunkte! Aktuelle EP: {self.erfahrung}/{self.level * 1000}")
        if self.erfahrung >= self.level * 1000:
            self.level_up()
            
        
    def level_up(self):
        self.level += 1
        self.erfahrung = 0
        self.hp_max += 20
        self.hp = self.hp_max
        self.schaden_min += 5
        self.schaden_max += 5
        print(f"🎉 {self.name} steigt auf Level {self.level} auf! HP und Schaden erhöht!")

class Gegner:
    def __init__(self, name, hp, schaden_min, schaden_max, gold, ep):
        self.name = name
        self.hp = hp
        self.schaden_min = schaden_min
        self.schaden_max = schaden_max
        self.gold = gold
        self.ep = ep

    def angreifen(self):
        return random.randint(self.schaden_min, self.schaden_max)

    def ist_besiegt(self):
        return self.hp <= 0
    
def kampf(held, gegner):
    print(f"\n⚔️ {held.name} vs {gegner.name} ⚔️")
    runde = 1

    while held.hp and not gegner.ist_besiegt():
        schaden_held = held.angreifen()
        schaden_gegner = gegner.angreifen()

        gegner.hp -= schaden_held
        held.hp -= schaden_gegner

        print(f"Runde {runde}: {held.name} trifft für {schaden_held} | {gegner.name} trifft für {schaden_gegner}")
        print(f"  {held.name} HP: {max(0, held.hp)}/{held.hp_max}")
        runde += 1

    if held.hp > 0:
        held.gold += gegner.gold
        held.erfahrung_sammeln(gegner.ep)
        print(f"\n✅ Sieg! +{gegner.gold} Gold +{gegner.ep} EP")
    else:
        print(f"\n❌ Niederlage!")


# --- Testen der Gegnerklasse ---
held = Charakter("Housten", "Krieger")
held.anzeigen()
goblin = Gegner("Goblin", 60, 8, 12, 25, 150)
kampf(held, goblin)
held.anzeigen()

# --- Testen der Klasse ---
# held = Charakter("Housten", "Krieger")
# held.anzeigen()
# held.erfahrung_sammeln(1000)
# held.anzeigen()
