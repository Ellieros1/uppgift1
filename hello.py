'''
print("Hello")
print(3+4)
print("hej" + "då")
print("3"+"4")
#Uträkningar
print(5+5) #addition 
print(7-2) #subtraktion
print(5*7) #multiplikation
print(5/8) #divison
print(15//7) #heltalsdivison
print(17%7) #rest 
print(7**3) #upphöjt
#variabler och datatyper
namn = "Ellie" #sträng
print("vad heter du?")
print(namn)

a = 22
if a > 14:
    print("a är större än 14")
#a är strörre än 14
a = -3
if a > 0:
    print("a är större än 0")
else:
    print("a är mindre än 0")
#a är mindre än 0

#Vilket titel har du?
pro = 2000
robux = int(input('Ange hur många robux du har ->'))
if robux >= pro:
    print('pro')
print('programmet avslutas')

e_gräns = 15
poäng = int(input('ange ditt poäng'))
if poäng >= e_gräns:
    print('godkänt')
else:
    print('ej godkänt')
print('programet avslutas')
'''
'''
i = 1
while i <= 10:
   print(f"{i} * 15 = {i * 15}")
   i += 1
'''
'''
import random as rand
slumptal = rand.randint(1, 35), end=" ") # Skapar ett slumptal mellan, och inklusive, 1 och 35
while i <= 35:
    print(rand.randint)(1,35), end=" ")
    i += 1
'''
'''
import random as rand
i = 1
print("Din LOTTO-rad:", end=" ")
while i <= 7:
    print(rand.randint(1,35), end=" ")
    i += 1
'''
'''
import random as rand
i = 1
print(f"{'match nr':>10}.{'resultat':>11}")
print("==========================")
while i <= 13:
    res = randit
'''
'''
#Detta program ska göra en lista på 15 gångertabel
for i in range(1, 16):
    print(f"{i:2.0f} * 15 = {i*15:3.0f}")
'''
