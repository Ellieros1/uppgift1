#Uppgift 1 (E-nivå)

basen= int(input("skriv basen på triangeln: "))
höjden= int(input("skriv höjden på triangeln: "))
arean_på_triangel=(basen * höjden)/2
print(f"Triangelns area är: {arean_på_triangel} areaenheter.")

#Uppgift 2 (E-nivå)

def get_price_type(age):
    if age < 15:
        return("barn")
    elif 14 < age <20:
        return("ungdom")
    else: 
        age < 19
        return("vuxen")
print(get_price_type(14))
print(get_price_type(15))
print(get_price_type(20))

#Uppgift 6 (C-nivå)