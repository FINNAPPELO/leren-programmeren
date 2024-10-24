woort_vervangers = {
    "hart": "ingang",
    "schubben": "teennagels",
    "vurige": "waterende",
    "draak": "geit",
    "vlammenzee": "golf van water",
    "schild": "zwemvest",
    "magie": "plastic",
    "boom": "houten paal",
    "huis": "woning",
    "kat": "poes",
    "hond": "dier",
    "fiets": "tweewieler",
    "auto": "voertuig",
    "stad": "gemeente",
    "land": "natie",
    "zee": "ocean",
    "berg": "heuvel",
    "rivier": "stroom",
    "brug": "overgang",
    "school": "onderwijsinstelling",
    "leraar": "docent",
    "boek": "geschrift",
    "pen": "schrijfgereedschap"
}
ingaand = input("vul hier tekst in")
worden = ingaand.split() 
vertalde_woorden = [woort_vervangers.get(wort, wort) for wort in worden] #tijden het verwerken is wort elke keer het wort waarmee die werkt
uitgaand = " ".join(vertalde_woorden) 
print("omvormde text:")
print(uitgaand)
