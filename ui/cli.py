import json
import os
from models.recept import Recept
from models.ingredient import Ingrediënt
from models.stap import Stap

# ---------- JSON opslag ----------
DATA_FILE = os.path.join("data", "recepten.json")

def save_recepten(recepten):
    os.makedirs("data", exist_ok=True)
    data = []
    for r in recepten:
        data.append({
            "naam": r.naam,
            "omschrijving": r.omschrijving,
            "ingredienten": [
                {"naam": ing.naam, "hoeveelheid": ing.hoeveelheid, "eenheid": ing.eenheid}
                for ing in r.ingrediënten
            ],
            "stappen": [st.tekst for st in r.stappen],
        })
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print("✅ Recepten opgeslagen naar data/recepten.json")

def load_recepten():
    if not os.path.exists(DATA_FILE):
        return seed_recepten()
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        recepten = []
        for r in data:
            ingrediënten = [Ingrediënt(i["naam"], i["hoeveelheid"], i["eenheid"]) for i in r["ingredienten"]]
            stappen = [Stap(s) for s in r["stappen"]]
            recepten.append(Recept(r["naam"], r["omschrijving"], ingrediënten, stappen))
        return recepten
    except Exception as e:
        print(f"⚠️ Kon JSON niet laden ({e}). Seed data wordt gebruikt.")
        return seed_recepten()

# ---------- Seed data (incl. vegan) ----------
def seed_recepten():
    pasta = Recept(
        "Pasta pesto",
        "Snelle pasta met pesto.",
        [Ingrediënt("Spaghetti", 75, "g"),
         Ingrediënt("Pesto", 20, "g")],
        [Stap("Kook de spaghetti."),
         Stap("Roer de pesto erdoor.")]
    )

    kip_kerrie = Recept(
        "Kip Kerrie",
        "Kip kerrie zonder pakjes en zakjes.",
        [Ingrediënt("Kipfilet", 500, "gram"),
         Ingrediënt("Sperziebonen", 400, "gram"),
         Ingrediënt("Rijst", 200, "gram")],
        [Stap("Kook de rijst en sperziebonen."),
         Stap("Snijd de kip in blokjes en bak ze gaar."),
         Stap("Voeg kerrie en kokosmelk toe en laat kort pruttelen.")]
    )

    quiche = Recept(
        "Gehakt quiche met paprika",
        "Een heerlijke quiche met gehakt en paprika.",
        [Ingrediënt("Gehakt", 300, "gram"),
         Ingrediënt("Paprika", 2, "stuks"),
         Ingrediënt("Bladerdeeg", 5, "plakken")],
        [Stap("Verwarm de oven voor op 200°C."),
         Stap("Bak het gehakt rul en voeg paprika toe."),
         Stap("Bekleed de vorm met bladerdeeg en vul met het mengsel."),
         Stap("Bak 30 minuten in de oven.")]
    )

    vegan_chili = Recept(
        "Vegan Chili Sin Carne",
        "Een plantaardige chili met bonen en groenten.",
        [Ingrediënt("Kidneybonen", 400, "g"),
         Ingrediënt("Mais", 150, "g"),
         Ingrediënt("Paprika", 1, "stuk"),
         Ingrediënt("Tomatenblokjes", 400, "g")],
        [Stap("Snijd de paprika in stukjes."),
         Stap("Bak de paprika kort aan."),
         Stap("Voeg tomatenblokjes, kidneybonen en mais toe."),
         Stap("Laat 15 minuten sudderen en breng op smaak met kruiden.")]
    )

    return [pasta, kip_kerrie, quiche, vegan_chili]

# ---------- Helpers ----------
def _print_detail(r: Recept):
    print(f"\n{r.naam}\n{r.omschrijving}\n\n• Ingrediënten:")
    for ing in r.ingrediënten:
        print(f"  - {ing.naam}: {ing.hoeveelheid:g} {ing.eenheid}")
    print("\nStappen:")
    for nr, st in enumerate(r.stappen, start=1):
        print(f"  {nr}. {st.tekst}")

# ---------- FR-1: tonen ----------
def toon_recepten(recepten):
    if not recepten:
        print("Geen recepten beschikbaar.")
        return
    for idx, r in enumerate(recepten, start=1):
        print(f"{idx}. {r.naam}")
    sel = input("Kies nummer (Enter = terug): ").strip()
    if sel:
        try:
            i = int(sel) - 1
            if 0 <= i < len(recepten):
                _print_detail(recepten[i])
        except ValueError:
            print("Geef een geldig nummer op.")

# ---------- FR-2: toevoegen ----------
def voeg_recept_toe(recepten):
    print("\n— Recept toevoegen —")
    naam = input("Naam: ").strip()
    omschrijving = input("Omschrijving: ").strip()
    ingrediënten, stappen = [], []

    while True:
        ing_naam = input("Ingrediënt-naam (Enter = stoppen): ").strip()
        if not ing_naam:
            break
        try:
            hoeveelheid = float(input("  Hoeveelheid: "))
        except ValueError:
            print("  Ongeldige hoeveelheid."); continue
        eenheid = input("  Eenheid (g/ml/stuks): ").strip()
        ingrediënten.append(Ingrediënt(ing_naam, hoeveelheid, eenheid))

    while True:
        stap_tekst = input("Stap (Enter = stoppen): ").strip()
        if not stap_tekst:
            break
        stappen.append(Stap(stap_tekst))

    if naam and omschrijving and ingrediënten and stappen:
        recepten.append(Recept(naam, omschrijving, ingrediënten, stappen))
        print(f"✅ Recept '{naam}' toegevoegd!")
    else:
        print("⚠️ Recept is niet volledig ingevuld.")

# ---------- FR-3: verwijderen ----------
def verwijder_recept(recepten):
    if not recepten:
        print("Geen recepten om te verwijderen."); return
    for idx, r in enumerate(recepten, start=1):
        print(f"{idx}. {r.naam}")
    sel = input("Welk nummer verwijderen? ").strip()
    try:
        i = int(sel) - 1
        if 0 <= i < len(recepten):
            verwijderd = recepten.pop(i)
            print(f"🗑️ Recept '{verwijderd.naam}' verwijderd.")
        else:
            print("Ongeldig nummer.")
    except ValueError:
        print("Geef een geldig nummer op.")

# ---------- FR-4: bewerken ----------
def bewerk_recept(recepten):
    if not recepten:
        print("Geen recepten om te bewerken."); return
    for idx, r in enumerate(recepten, start=1):
        print(f"{idx}. {r.naam}")
    sel = input("Welk recept wil je bewerken? (nummer) ").strip()
    try:
        i = int(sel) - 1
        if not (0 <= i < len(recepten)):
            print("Ongeldig nummer."); return
    except ValueError:
        print("Geef een geldig nummer op."); return

    r = recepten[i]
    print(f"\n— Bewerken: {r.naam} —")
    print("1) Naam wijzigen")
    print("2) Omschrijving wijzigen")
    print("3) Ingrediënt toevoegen")
    print("4) Ingrediënt verwijderen")
    print("5) Stap toevoegen")
    print("6) Stap verwijderen")
    keuze = input("> ").strip()

    if keuze == "1":
        nieuwe = input("Nieuwe naam: ").strip()
        if nieuwe: r.naam = nieuwe; print("Naam aangepast.")
    elif keuze == "2":
        nieuwe = input("Nieuwe omschrijving: ").strip()
        if nieuwe: r.omschrijving = nieuwe; print("Omschrijving aangepast.")
    elif keuze == "3":
        naam = input("Ingrediënt-naam: ").strip()
        try: hoeveelheid = float(input("Hoeveelheid: "))
        except ValueError: print("Ongeldige hoeveelheid."); return
        eenheid = input("Eenheid: ").strip()
        r.ingrediënten.append(Ingrediënt(naam, hoeveelheid, eenheid))
        print("Ingrediënt toegevoegd.")
    elif keuze == "4" and r.ingrediënten:
        for idx, ing in enumerate(r.ingrediënten, start=1):
            print(f"{idx}. {ing.naam} ({ing.hoeveelheid:g} {ing.eenheid})")
        try:
            j = int(input("Welk nummer verwijderen? ")) - 1
            weg = r.ingrediënten.pop(j); print(f"Ingrediënt '{weg.naam}' verwijderd.")
        except: print("Ongeldig nummer.")
    elif keuze == "5":
        tekst = input("Nieuwe stap: ").strip()
        if tekst: r.stappen.append(Stap(tekst)); print("Stap toegevoegd.")
    elif keuze == "6" and r.stappen:
        for idx, st in enumerate(r.stappen, start=1):
            print(f"{idx}. {st.tekst}")
        try:
            k = int(input("Welk nummer verwijderen? ")) - 1
            weg = r.stappen.pop(k); print(f"Stap '{weg.tekst}' verwijderd.")
        except: print("Ongeldig nummer.")

# ---------- FR-5: zoeken ----------
def zoek_recepten(recepten):
    if not recepten:
        print("Geen recepten om te zoeken."); return
    print("\n— Zoeken —")
    print("1) Op naam")
    print("2) Op ingrediënt")
    keuze = input("> ").strip()

    term = input("Zoekterm: ").strip().lower()
    hits = []
    if keuze == "1":
        hits = [r for r in recepten if term in r.naam.lower()]
    elif keuze == "2":
        hits = [r for r in recepten if any(term in ing.naam.lower() for ing in r.ingrediënten)]

    if not hits: print("Geen resultaten."); return
    for idx, r in enumerate(hits, start=1):
        print(f"{idx}. {r.naam}")
    sel = input("Kies nummer (Enter = terug): ").strip()
    if sel:
        try:
            i = int(sel) - 1
            if 0 <= i < len(hits):
                _print_detail(hits[i])
        except: print("Ongeldig nummer.")

# ---------- Hoofdmenu (Week 4) ----------
def start():
    recepten = load_recepten()  # ← laad bij start
    while True:
        print("\n=== Receptenboek (Week 4) ===")
        print("1) Recepten tonen")
        print("2) Recept toevoegen")
        print("3) Recept verwijderen")
        print("4) Recept bewerken")
        print("5) Zoeken")
        print("6) Opslaan")
        print("0) Afsluiten")
        keuze = input("> ").strip()

        if keuze == "1": toon_recepten(recepten)
        elif keuze == "2": voeg_recept_toe(recepten)
        elif keuze == "3": verwijder_recept(recepten)
        elif keuze == "4": bewerk_recept(recepten)
        elif keuze == "5": zoek_recepten(recepten)
        elif keuze == "6": save_recepten(recepten)
        elif keuze == "0":
            save_recepten(recepten)  # ← auto-save bij afsluiten
            break
        else:
            print("Ongeldige keuze.")
