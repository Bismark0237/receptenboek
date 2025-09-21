from models.recept import Recept
from models.ingredient import Ingrediënt
from models.stap import Stap

def seed_recepten():
    pasta = Recept(
        "Pasta pesto",
        "Snelle pasta met pesto.",
        [
            Ingrediënt("Spaghetti", 75, "g"),
            Ingrediënt("Pesto", 20, "g"),
        ],
        [
            Stap("Kook de spaghetti."),
            Stap("Roer de pesto erdoor."),
        ],
    )

    kip_kerrie = Recept(
        "Kip Kerrie",
        "Kip kerrie zonder pakjes en zakjes.",
        [
            Ingrediënt("Kipfilet", 500, "gram"),
            Ingrediënt("Sperziebonen", 400, "gram"),
            Ingrediënt("Rijst", 200, "gram"),
        ],
        [
            Stap("Kook de rijst en sperziebonen."),
            Stap("Snijd de kip in blokjes en bak ze gaar."),
            Stap("Voeg kerrie en kokosmelk toe en laat kort pruttelen."),
        ],
    )

    quiche = Recept(
        "Gehakt quiche met paprika",
        "Een heerlijke quiche met gehakt en paprika.",
        [
            Ingrediënt("Gehakt", 300, "gram"),
            Ingrediënt("Paprika", 2, "stuks"),
            Ingrediënt("Bladerdeeg", 5, "plakken"),
        ],
        [
            Stap("Verwarm de oven voor op 200°C."),
            Stap("Bak het gehakt rul en voeg paprika toe."),
            Stap("Bekleed de vorm met bladerdeeg en vul met het mengsel."),
            Stap("Bak 30 minuten in de oven."),
        ],
    )

    return [pasta, kip_kerrie, quiche]

def start():
    recepten = seed_recepten()
    while True:
        print("\n=== Receptenboek (Week 1) ===")
        print("1) Recepten tonen")
        print("0) Afsluiten")
        keuze = input("> ").strip()
        if keuze == "1":
            for idx, r in enumerate(recepten, start=1):
                print(f"{idx}. {r.naam}")
            sel = input("Kies nummer (Enter = terug): ").strip()
            if sel:
                try:
                    i = int(sel) - 1
                    if 0 <= i < len(recepten):
                        r = recepten[i]
                        print(f"\n{r.naam}\n{r.omschrijving}\n\n• Ingrediënten:")
                        for ing in r.ingrediënten:
                            print(f"  - {ing.naam}: {ing.hoeveelheid:g} {ing.eenheid}")
                        print("\nStappen:")
                        for nr, st in enumerate(r.stappen, start=1):
                            print(f"  {nr}. {st.tekst}")
                    else:
                        print("Ongeldig nummer.")
                except ValueError:
                    print("Geef een geldig nummer op.")
        elif keuze == "0":
            break
        else:
            print("Ongeldige keuze.")
