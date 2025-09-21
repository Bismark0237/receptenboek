from models.recept import Recept
from models.ingredient import Ingrediënt
from models.stap import Stap

# ————— Seed data (mag je aanpassen) —————
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

# ————— Week 2 functies —————
def toon_recepten(recepten):
    if not recepten:
        print("Geen recepten beschikbaar.")
        return
    for idx, r in enumerate(recepten, start=1):
        print(f"{idx}. {r.naam}")
    sel = input("Kies nummer (Enter = terug): ").strip()
    if not sel:
        return
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

def voeg_recept_toe(recepten):
    print("\n— Recept toevoegen —")
    naam = input("Naam: ").strip()
    omschrijving = input("Omschrijving: ").strip()

    ingrediënten = []
    while True:
        ing_naam = input("Ingrediënt-naam (Enter = stoppen): ").strip()
        if not ing_naam:
            break
        try:
            hoeveelheid = float(input("  Hoeveelheid: "))
        except ValueError:
            print("  Ongeldige hoeveelheid, probeer opnieuw.")
            continue
        eenheid = input("  Eenheid (g/ml/stuks): ").strip()
        ingrediënten.append(Ingrediënt(ing_naam, hoeveelheid, eenheid))

    stappen = []
    while True:
        stap_tekst = input("Stap (Enter = stoppen): ").strip()
        if not stap_tekst:
            break
        stappen.append(Stap(stap_tekst))

    if naam and omschrijving and ingrediënten and stappen:
        recepten.append(Recept(naam, omschrijving, ingrediënten, stappen))
        print(f"Recept '{naam}' toegevoegd!")
    else:
        print("Recept is niet volledig ingevuld (naam/omschrijving/ingrediënten/stappen vereist).")

def verwijder_recept(recepten):
    if not recepten:
        print("Geen recepten om te verwijderen.")
        return
    for idx, r in enumerate(recepten, start=1):
        print(f"{idx}. {r.naam}")
    sel = input("Welk nummer wil je verwijderen? ").strip()
    try:
        i = int(sel) - 1
        if 0 <= i < len(recepten):
            verwijderd = recepten.pop(i)
            print(f"Recept '{verwijderd.naam}' verwijderd.")
        else:
            print("Ongeldig nummer.")
    except ValueError:
        print("Geef een geldig nummer op.")

# ————— Hoofdmenu —————
def start():
    recepten = seed_recepten()
    while True:
        print("\n=== Receptenboek (Week 2) ===")
        print("1) Recepten tonen")
        print("2) Recept toevoegen")
        print("3) Recept verwijderen")
        print("0) Afsluiten")
        keuze = input("> ").strip()

        if keuze == "1":
            toon_recepten(recepten)
        elif keuze == "2":
            voeg_recept_toe(recepten)
        elif keuze == "3":
            verwijder_recept(recepten)
        elif keuze == "0":
            break
        else:
            print("Ongeldige keuze.")
