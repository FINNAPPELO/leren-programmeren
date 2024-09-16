i=0

while i < 1:
    
    aantal=str((input("hoeveel smal pizzas wilt u? ")))
    if aantal.isdigit() is True:
        aantal=int(aantal)
        print('sg')
        i =+ 1
        print(" ----------------*****pizza bon*****-----------------------")  
        print(f"| groote van pizza:       smal      ")
        print(f"| aantal pizza's:         {aantal}   ")
        print(f"| koste per pizza:        10      ")
        print(f"| totale kosten pizza's   {aantal*10}    ")
        print(" ----------------------------------------------------------")
        
    else:
        print("dit is geen heel nummer  ")


   


