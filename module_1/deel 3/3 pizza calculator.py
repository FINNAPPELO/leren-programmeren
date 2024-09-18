#Finn, Appelo, opdracht, pizza calculator
groote=int(input('hoeveel large pizzas wilt u: ')) #vragen wat voor pizza iemand wil
medium=int(input('hoeveel medium pizzas wilt u: '))
smal=int(input("hoeveel smal pizzas wilt u:"))
#koste met geen pizza's 
smal_k= 10  #koste smal pizza
medium_k= 11.50 #koste medium pizza
large_k= 17.50  #koste large pizza

t_groote=groote*large_k
t_medium=medium*medium_k
t_smal=smal*smal_k
totaal= t_groote+t_medium+t_smal
print(" ----------------------------------------------------")     #bonnetje 
print(f"|  large pizzas:     {groote} x {large_k}  = {t_groote} ")
print(f"|  medium pizzas:    {medium} x {medium_k} = {t_medium} ")
print(f"|  smal pizzas:      {smal}  x {smal_k}   = {t_smal}")
print(f"| totale kosten pizza's     {totaal}    ")
print(" ----------------------------------------------------")