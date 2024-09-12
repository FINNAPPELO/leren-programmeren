toegangsticket =float(input('hoeveel koste 1 toegangsticket: '))
mensen = int(input("met hoeveel mensen was je: "))
vip = ((9 * 0.35)*mensen)
alle_kosten = (toegangsticket+vip)

print(f"Dit geweldige dagje-uit met 4 mensen in de Speelhal met 45 minuten VR kost je maar {alle_kosten} euro")