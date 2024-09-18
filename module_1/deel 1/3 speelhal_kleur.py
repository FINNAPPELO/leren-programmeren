from termcolor import colored, cprint, COLORS
toegangsticket =(7.45 * 4 )
vip = ((9 * 0.35)*4)
alle_kosten = (toegangsticket+vip)
print(alle_kosten)
print(f"Dit geweldige dagje-uit met 4 mensen in de Speelhal met 45 minuten VR kost je maar {colored(alle_kosten,'red', attrs=['bold'])} euro")
