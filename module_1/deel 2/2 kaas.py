geel = input('is de kaas geel ?')
if geel == "ja":
    gaaten = input('zitten er gaaten in de kaas? ')
    if gaaten=='ja':
        duur = input("is de kaas belachelijk duur? ")
        if duur == "ja":
            print("is je kaas emmenthaler ")
        else:
            print("is je kaas leerdammer ")
    else:
        hard = input("is je kaas hard als steen? ")
        if hard == 'ja':
            print("is je kaas parmigiano reggiano ")
        else:
            print("is je kaas goudse kaas ")
else:
    schimmel = input("heeft de kaas blauwe schimmel? ") 
    if schimmel=='ja':
        korst1 = input('heeft uw kaas korst? ')  
        if korst1 == "ja":
            print("is je kaas camembert")       
        else:
            print("is je kaas mozzerella ")
    else:
        korst2=input("heeft uw kaas korst? ")
        if korst2 == 'ja':
            print('is je kaas bleu de rochbaron')
        else:
            print("is je kaas foume d'ambert")