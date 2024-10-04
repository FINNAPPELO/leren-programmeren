
def getal(nr1:int ,nr2:int )-> int :
   
   if nr1>nr2:
      return f'Maximum: {nr1} en minimum: {nr2}'
   if nr1<nr2:
        return f'Maximum: {nr2} en minimum: {nr1}'
   if nr1==nr2 :
            return f'bijde getallen zijn eve groot'
            
print(getal(7,7))
print(getal(7,64))
print(getal(64,7))