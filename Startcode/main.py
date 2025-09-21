from recept import Recept 
#from ingrediënt import Ingredient
#from stap import Stap

def main():
    recepten = []

    recept1 = Recept("Kip Kerrie", "Kip kerrie zonder pakjes en zakjes")
    #recept1.voeg_ingredient_toe(Ingredient("kip", 500, "gram"))
    #recept1.voeg_ingredient_toe(Ingredient("sperziebonen", 400, "gram"))

    #recept1.voeg_stap_toe(Stap("Kook de rijst en zet een pan water met een snuf zout op het vuur voor de sperziebonen."))
    #recept1.voeg_stap_toe(Stap("Snijd de kip in kleine blokjes, snipper het uitje, snijd de knoflook fijn en snijd de kontjes van de sperziebonen (was ze ook even)."))

    #recepten.append(recept1)

    recept2 = Recept("Gehakt quiche met paprika", "Een heerlijke quiche met gehakt en paprika.")

    # enz.. enz..
    # Veel succes!

if __name__ == "__main__":
    main()
