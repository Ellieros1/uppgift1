'''
tal_1 = 10
tal_2 = 20
summa = add(tal_1, tal_2) #add finns inte som en funktion och är inte definerat och därför måste vi skapa de
print(f"Summan av {tal_1} och {tal_2} är {summa}")

def add(a, b):     # Här
  the_sum = a + b  # skapas
  return the_sum   # funktionen

# Huvudprogram nedan
tal_1 = 10
tal_2 = 20
summa = add(tal_1, tal_2) # Här anropas funktionen

print(f"Summan av {tal_1} och {tal_2} är {summa}")
'''

# en funktion som adderar två tal
# nyckelordet def används för att definiera en funktion
def add(tal_1, tal_2):  # Talen tal_ och tal_2 som tas emot kallas parametrar.

    summa = tal_1 + tal_2
    # nyckelordet return används för att returnera någonting från en funktion
    return summa


# Huvudprogrammet anropar funktionen add med argumenten 2 och 3
# det returnerade värdet från funktionen läggs i variabeln my_sum
my_sum = add(2, 3)

print(my_sum)