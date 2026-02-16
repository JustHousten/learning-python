# Lektion 1: Variablen und Datentypen
# Variablen sind Speicherplätze für Werte

# Text (String)
charakter_name = "Krieger"

# Ganze Zahl (Integer)
level = 1
gold = 500

# Kommazahl (Float)
angriff_multiplikator= 1.5

# Wahr/Falsch (Boolean)
ist_eingeloggt = True

# Ausgabe
print(charakter_name)
print(level)
print(gold)
print(angriff_multiplikator)
print(ist_eingeloggt)

# Variablen können verändert werden
gold = gold + 100
print(gold) # Was wird ausgegeben?
# Ausgegeben wird [gold500 + 100 = 600]

# Weiter ausprobieren
# print(charakter_name + level)
# Das geht nicht weil es zwei grundverschiedene Dinge sind
# Stattdessen folgendes:
print(charakter_name + str(level))

print("Charakter: " + charakter_name)
print("Level: " + str(level))
print("Gold: " + str(gold))

# Alte Methode (umständlich)
print("Charakter: " + charakter_name + " Level: " + str(level))
# f-String (modern, viel lesbarer)
print(f"Charakter: {charakter_name} Level: {level}")

print(f"Charakter: {charakter_name}")
print(f"Level: {level}")
print(f"Gold: {gold}")

