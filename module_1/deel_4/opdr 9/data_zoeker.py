# toets_data has name:score combinations separated by a komma
def  toets_data (data:str = 'Sofie:8,Emma:7,Ahmed:9,Daan:6,Lisa:8,Fatima:7,Ruben:9,Ayoub:6,Bram:6,Maria:7',separator:str=',' ,position:int=8):

    
    splitted_strings =data.split(separator) # string splits itself into collection of strings
    if 0 <= position< len(splitted_strings):
        return  splitted_strings[position] # read value at position of split_values
    else:
        return  None
print(toets_data(position=1))