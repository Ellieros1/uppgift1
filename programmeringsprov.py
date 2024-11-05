#E-uppgift - generera nummer
#Skriv funktionen numbers_between(tal1, tal2) som tar två heltal som argument och skriver ut alla heltal mellan de två talen.

#Körningsexempel:
#numbers_between(12, 20)		
#skriver ut talen 13, 14, 15, 16, 17, 18 och 19 på varsin rad

#numbers_between(0, 4)		
#skriver ut siffrorna 1, 2 och 3 på varsin rad

#numbers_between(0, 1)
#skriver inte ut några siffror

def numbers_between(tal1, tal2): 
    for i in range(tal1 + 1, tal2): #skapar loop
        print(i)
numbers_between(12, 20) #här skiver du talen

#E-uppgift - lever spelaren
#Skriv funktionen is_alive(health) som returnerar True om health är större än noll och annars False.

#Körningsexempel:
#print(is_alive(12))	# skriver ut true
#print(is_alive(0))	# skriver ut false
#print(is_alive(-3))	# skriver ut false

def is_alive(health):
    return health > 0
print(is_alive(13))

def is_alive(health):
    if health > 0:
        return True
    else:
        return False
print(is_alive(3))

monthly_spending = [2689.56, 2770.38, 2394.04, 2099.91, 3182.20, 3267.12, 1746.83, 2545.72, 3328.20, 3147.30, 2462.61, 3890.45]
first_semester= 0
second_semester = 0
for month in range(12):
    if month < 6:
        first_semester += monthly_spending[month]
    else:
        second_semester += monthly_spending[month]
first_semester_avg=first_semester / 6
second_semester_avg=second_semester / 6

print("Avarage expenses for the first semester:", first_semester_avg)
print("Avarage expenses for the second semester:", second_semester_avg)

paul_friends = ["Mary", "Tim", "Mike", "Henry"]
tina_friends = ["Tim", "Susan", "Mary", "Josh"]
 
combined_friends = list(set(paul_friends + tina_friends))
 
print("Combined list of friends:", combined_friends)
