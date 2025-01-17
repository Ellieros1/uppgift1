# ------------------------------- Information --------------------------------- #
"""
Titel: Biblioteket
Författare: 
Datum: 
Det här är ett program för hantering av enklare biblioteksrutiner.
Programmet lagrar böckerna i en fil med namnet "bibliotek.txt" mellan körningarna.
"""
# ------------------------- Biblioteksimportering ----------------------------- #
import os

# ---------------------------- Klassdefinitioner ------------------------------ #

class Bok:
    """ Bok är en klass som representerar en bok i biblioteket. Varje objekt
    som skapas ur klassen har en titel, författare och en variabel som håller
    reda på om boken är utlånad eller inte. """
    
    def __init__(self, titel, författare, utlånad=False): #Definerar init som initieringsmetod och lägger till nytt bok objekt med, titel, författare och om boken är utlånad eller inte.
        self.titel = titel #Lägger till titel attributet(Attribut egenskap som går ihop med ett objekt i en klass, attributet lagrar data som beskriver egenskaper/tillståndet hos ett objekt.)
        self.författare = författare #lägger till författare attributet.
        self.utlånad = utlånad #lägger till utlånad attributet med standadard värdet false.

    def __str__(self): #Definerar str som skapar en strängreperestation av objektet.
        return f"Boken '{self.titel}', skriven av {self.författare}, utlånad: {'ja' if self.utlånad else 'nej'}."#Retunerar en sträng med information om boken.#Skapar en sträng med infromation om boken.#Variabeln "f" används för att skapa strängar med variabler och uttryck på ett mycket enklare sätt och som gör koden mer läsbar alltså mindre sökig och det ser bättre ut. Utan f strängar så används t.ex "+" för att sammanfoga flera strängar.

class Bibliotek:
    """ Bibliotek är en klass som representerar en bibliotekskatalog. Ett objekt
    ur klassen har en lista över böcker som attribut, samt metoder för att
    modifiera katalogen. """

    def __init__(self, filnamn="bibliotek.txt"): #Definerar init som intergeringsmetod/Konstruktorn som lägger till/intergrerar nytt biblioteks objekt som tar emot filen "bibliotek.txt".
        self.filnamn = filnamn #Lägger till filnamn attributet med standard värdet "bibliotek.txt".
        self.böcker = self.läs_från_fil() #Läser in böcker från filen och lagrar dom i böcker attributet.

    def läs_från_fil(self):
        böcker = [] #Skapar en tom lista som används för att lagra alla böcker i.
        if os.path.exists(self.filnamn): #Kontrollerar om filen finns.
            with open(self.filnamn, "r") as fil: #Öppnar filan i "r" alltså läsläge.
                for rad in fil: #Går igenom varje rad i filen med en for loop.
                    författare, titel, årtal, utlånad = rad.strip().split(",") #Delar upp raden författare, titel och ifall den är utlånad eller inte.
                    böcker.append(Bok(författare, titel, int(utlånad))) #Lägger till ett bok objekt och lägger till det i listan med hjälp av "append".
        return böcker #Retunerar boklista

    def spara_till_fil(self):
        with open(self.filnamn, "w") as fil: #Öppnar filen i "w" skrivläge.
            for bok in self.böcker: #Upprepar varje bok i listan genom en for loop.
                fil.write(f"{bok.författare},{bok.titel},{int(bok.utlånad)}\n") #Skriver ner alla bokens attribut till filen. författare, titel och utlånad status. /n används för att skriva ut en ny rad.

    def hitta_titel(self, titel):
        return [bok for bok in self.böcker if bok.titel.lower() == titel.lower()] #Retunerar en lista med böcker som matchar titeln.

    def hitta_författare(self, författare):
        return [bok for bok in self.böcker if bok.författare.lower() == författare.lower()] #Retunerar en lista med böcker som matchar författaren.

    def låna_bok(self, titel):
        for bok in self.hitta_titel(titel): #Går över böcker som matchar titeln.
            if not bok.utlånad: #Kontrollerar om boken inte är utlånad.
                bok.utlånad = True #Sätter boken som utlånad.
                self.spara_till_fil() #Sparar ändringen till filen.
                return f"Boken '{titel}' är nu utlånad." #Retunerar meddelande att boken är nu utlånad.
        return f"Boken '{titel}' finns inte eller är redan utlånad." #Retunerar felmeddelande om boken inte kan lånas.

    def lämna_tillbaka(self, titel):
        for bok in self.hitta_titel(titel): #Går över böcker som matchar titeln
            if bok.utlånad: #Kontrollerar om boken är utlånad.
                bok.utlånad = False #Sätter boken som återlämnad.
                self.spara_till_fil() #Sparar ändringen till filen.
                return f"Boken '{titel}' har återlämnats till biblioteket." #Retunerar ett meddelande att boken är återlämnad.
        return f"Boken '{titel}' finns inte eller är redan återlämnad." #Retunerar felmeddelande att boken inte går att återlämnas.

    def lägg_till_bok(self, författare, titel):
        if not self.hitta_titel(titel): #Kontrollerar om boken inte redan finns.
            self.böcker.append(Bok(författare, titel)) #Skapar ett nytt "bok"ojekt och lägger till den i listan.
            self.spara_till_fil() #Sparar ändringen till filen
            return f"Boken '{titel}' av {författare} är nu tillagd i biblioteket." #Retunerar meddlande att boken är tillagd.
        return f"Boken '{titel}' finns redan i biblioteket." #Retunerar felmeddelande att boken redan finns.

    def ta_bort_bok(self, titel):
        bok_till_borttagning = self.hitta_titel(titel) #Hittar boken som ska tas bort.
        if bok_till_borttagning: #Kontrollerar ifall boken finns.
            self.böcker.remove(bok_till_borttagning[0]) #Tar bort boken från listan
            self.spara_till_fil() #Sparar ändringen till filen.
            return f"Boken '{titel}' har tagits bort." #retunerar bekräftelse att boken har tagits bort.
        return f"Boken '{titel}' hittas inte." # retunerar felmeddelande att boken inte hittas.

    def lista_böcker(self):
        return "\n".join(str(bok) for bok in self.böcker) # Retunerar Strängar som reprensenterar alla böcker i listan.
    
    def sortera_böcker(self, efter_titel=True):
        self.böcker.sort(key=lambda bok: bok.titel if efter_titel else bok.författare) # Sorterar böckerna efter title eller författare.
        return self.lista_böcker() #Retunerar den sorterade listan.

# ------------------------------ Huvudprogram --------------------------------- #
def main():
    bibliotek = Bibliotek() #skapar biblioteks objekt.
    meny_val = "" #Lägger till menyval med en tom sträng.

    while meny_val != "q": #loppar igenom menyn tills användaren väljer att sluta genom att skriva "q".
        print(
        """
                                          --- MENY ---
                Välkommen till biblioteks-simulatorn. Välj ett av alternativen nedan:
            1. Sök efter titel                                  2. Sök efter författare
            3. Låna bok                                         4. Återlämna bok
            5. Lägg till ny bok                                 6. Ta bort bok
            7. Lista alla böcker                                8. Sortera böcker
                                        q. Avsluta
        ---------------------------------------------------------------------------------------
        """) #Skrivet ut en meny.

        meny_val = input("-> ") #Tar emot användarens val från menyn.

        if meny_val == "1":
            titel = input("Ange titel: ") #Ber användaren att ange titel.
            resultat = bibliotek.hitta_titel(titel) #Hittar bok som matchar titeln.
            for bok in resultat: #Går över matchande böcker.
                print(bok) #Ange ut boken.
        elif meny_val == "2":
            författare = input("Ange författare: ") #Ber användaren att ange författare.
            resultat = bibliotek.hitta_författare(författare) #Hittar böcker som matchar förattaren.
            for bok in resultat: #Går över matchande böcker.
                print(bok) #Skriver ut boken.
        elif meny_val == "3":
            titel = input("Ange boken du vill låna: ") #Ber användaren att ange boken som den vill låna.
            print(bibliotek.låna_bok(titel)) #Försöker låna boken och skriver ut resultatet.
        elif meny_val == "4":
            titel = input("Ange titel på boken du vill återlämna: ")#Ber användaren att ange boken som den vill återlämna.
            print(bibliotek.lämna_tillbaka(titel))#Försöker återlämna boken och skriver ut resultatet.
        elif meny_val == "5":
            författare = input("Ange författare: ") #Be användaren att ange författaren.
            titel = input("Ange titeln på den nya boken: ") #Be använderen att ange titeln på den nya boken.
            print(bibliotek.lägg_till_bok(författare, titel)) #Försöker lägg till boken och skriver ut resultatet.
        elif meny_val == "6":
            titel = input("Ange titeln på boken du vill ta bort: ") #Ber användaren att ange titeln som den vill ta bort.
            print(bibliotek.ta_bort_bok(titel)) #Försöker ta bort boken och skriver ut resultatet.
        elif meny_val == "7":
            print(bibliotek.lista_böcker()) #Skriver ut en lista över alla böcker i biblioteket.
        elif meny_val == "8":
            print(bibliotek.sortera_böcker()) #Skriver ut en sorterad lista över alla böcker i biblioteket.
        elif meny_val == "q":
            print("Tack för att du använde biblioteket") #Skriver ut tack meddelande till användaren.
            quit #Avslutar programet.
        else:
            print("Ogiltigt val. Du kan bara skriva 1-8 och bokstaven q om du vill avsluta. Försök igen.") #Skriver ut felmeddelande vid ett ogiltigt val.

print(
"""
                                   .--.                   .---.
                               .---|__|           .-.     |~~~|
                            .--|===|--|_          |_|     |~~~|--.--.
                            |  |===|  |'\     .---!~|  .--|   |--|--|
                            |%%|   |  |.'\    |===| |--|%%|   |  |  |
                            |%%|   |  |\.'\   |   | |__|  |   |  |  |
                            |B | I |B | \L \  |=I=|O|T=|E | K |E |T |
                            |  |   |__|  \.'\ |   |_|__|  |~~~|__|__|
                            |  |===|--|   \.'\|===|~|--|%%|~~~|--|--|
                            ^--^---'--^    `-'`---^-^--^--^---'--'--'
""")

main() #Startar huvudprogrammet.