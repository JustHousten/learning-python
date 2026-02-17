# Lektion 8: Klassen und Objekte
# Eine Klasse ist ein Bauplan für Objekte

class Charakter:
    def __init__(self, name, klasse):
        self.name = name
        self.klasse = klasse
        self.level = 1
        self.hp = 100
        self.hp_max = 100
        self.gold = 0
        self.erfahrung = 0

    def anzeigen(self):
        print(f"{self.name} ({self.klasse}) - Level {self.level}")
        print(f"HP: {self.hp}/{self.hp_max} | Gold: {self.gold}")

    def schaden_nehmen(self, schaden):
        self.hp -= schaden
        if self.hp < 0:
            self.hp = 0
        print(f"{self.name} nimmt {schaden} Schaden! HP: {self.hp}/{self.hp_max}")
    
    def heilen(self, heilung):
        self.hp += heilung
        if self.hp > self.hp_max:
            self.hp = self.hp_max
        print(f"{self.name} heilt {heilung} HP! HP: {self.hp}/{self.hp_max}")

    def erfahrung_sammeln(self, menge):
        self.erfahrung += menge
        print(f"+{menge} Erfahrungspunkte! Aktuelle Erfahrung: {self.erfahrung}")
        if self.erfahrung >= self.level * 1000:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.hp_max += 50
        self.hp = self.hp_max
        self.erfahrung = 0
        print(f"🎉 LEVEL UP! {self.name} ist jetzt Level {self.level}!")

held = Charakter("Housten", "Krieger")
held.anzeigen()
held.schaden_nehmen(30)
held.schaden_nehmen(25)
held.heilen(40)
held.anzeigen()

held = Charakter("Housten", "Krieger")
held.anzeigen()

held1 = Charakter("Housten", "Krieger")
held2 = Charakter("Merlin", "Magier")

held1.anzeigen()
print()
held2.anzeigen()

held = Charakter("Housten", "Krieger")
held.erfahrung_sammeln(500)
held.erfahrung_sammeln(300)
held.erfahrung_sammeln(300) # Hier sollte ein Level-Up passieren
held.anzeigen()