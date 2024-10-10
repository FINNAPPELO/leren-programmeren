tupele=('maandag','dinsdag','woensdag','donderdag','vrijdag','zaterdag','zondag')
print({tupele})
l_tup=len(tupele)
for i in range(l_tup):
    print(f'- {tupele[i]}')
print(' ')
print(f'de weekenddagenen  zijn {tupele[5]} & {tupele[6]}')
print(f'de werkdagen zijn {tupele[0]}, {tupele[1]}, {tupele[2]}, {tupele[3]} & {tupele[4]}')
print(' ')
print(f'alle dagen in omgekeerde volgworde zijn:   {tupele[6]} -> {tupele[5]} -> {tupele[4]} -> {tupele[3]} -> {tupele[2]} -> {tupele[1]} -> {tupele[0]} ')
print('de werkdagen in omgekeerde volgworde zijn ')
for  i in range(4,-1,-1):   
    print(f'- {tupele[i]}')
print(f'de weekenddagen in omgekeerde volgworde zijn {tupele[6]} &  {tupele[5]}')


