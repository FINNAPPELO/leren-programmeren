Begin

    Maak een lege lijst "deelnemers"

    // Vraag namen op totdat er minimaal 3 unieke namen zijn
    Terwijl de lengte van "deelnemers" < 3:
        Vraag de gebruiker om een naam in te voeren
        Als de naam nog niet in de lijst "deelnemers" staat:
            Voeg de naam toe aan de lijst "deelnemers"
        Anders:
            Toon een foutmelding: "Deze naam is al ingevoerd."

    // Bij 3 of meer namen, geef de keuze om lootjes te trekken of een extra naam in te voeren
    Toon de vraag: "Wil je nog een naam invoeren? (ja/nee)"
    Lees antwoord "ja/nee"

    Als het antwoord "ja" is:
        Terwijl de lengte van "deelnemers" < 4:
            Vraag de gebruiker om een naam in te voeren
            Als de naam nog niet in de lijst "deelnemers" staat:
                Voeg de naam toe aan de lijst "deelnemers"
            Anders:
                Toon een foutmelding: "Deze naam is al ingevoerd"

    // Als er 3 of meer deelnemers zijn, kan lootjes worden getrokken
    Maak een lijst "lootjes" die gelijk is aan de lijst van "deelnemers"
    Schud de lijst "lootjes" willekeurig

    // Zorg ervoor dat niemand zijn eigen naam heeft
    Maak een lege lijst "verdeling" voor lootjes
    Voor elke deelnemer in "deelnemers":
        Terwijl de naam van de deelnemer gelijk is aan het lootje in "lootjes" (d.w.z. niemand mag zijn eigen naam trekken):
            Schud de lijst "lootjes" opnieuw
        Verdeel het lootje van de deelnemer en verwijder dit lootje uit de lijst

    // Toon de uiteindelijke verdeling van lootjes
    Voor elke deelnemer in "deelnemers":
        Print de naam van de deelnemer en het bijbehorende lootje

Einde
