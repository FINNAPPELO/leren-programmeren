#Finn, Appelo, opdracht, pizza calculator
groote=input('welke maat pizza wilt u smal medium or large: ') #vragen wat voor pizza iemand wil
aantal = int(input("hoeveel pizzas wilt u ?")) #vragen hoevel pizza's
koste = 0 #koste met geen pizza's 
smal= 10  #koste smal pizza
medium= 11.50 #koste medium pizza
large= 17.50  #koste large pizza
if groote == 'smal':         #als die klijne pizza is
    koste =  10*aantal
    pp=10
elif groote == 'medium':  #als die medium pizza is
    koste =11.50*aantal
    pp=11.50
elif groote == 'large': #als die large pizza is 
    koste = 17.50*aantal
    pp=17.50
print(" ----------------------------------------------------")     #bonnetje 
print(f"| groote van pizza:      {groote}   ")
print(f"| aantal pizza's:        {aantal}   ")
print(f"| koste per pizza:       {pp}       ")
print(f"| totale kosten pizza's  {koste}    ")
print(" ----------------------------------------------------")