tupele = ('maandag', 'dinsdag', 'woensdag', 'donderdag', 'vrijdag', 'zaterdag', 'zondag')
print({tupele})
l_tup = len(tupele)
for i in range(l_tup):
    print(f'- {tupele[i]}')
print(' ')
print('de weekenddagen zijn:')
for i in range(5, 7):  
    print(f'- {tupele[i]}')
print('de werkdagen zijn:')
for i in range(5):
    if i < 4:
        print(f'- {tupele[i]}')
    else:
        print(f'& {tupele[i]}')
print(' ')
print("de week dagen in verkerde volgworde")
for i in reversed(range(7)):
    print(f'- {tupele[i]}')
print('de werkdagen in omgekeerde volgorde zijn ')
for i in range(4, -1, -1):
    print(f'- {tupele[i]}')
print(  'de weekenddagen in omgekeerde volgorde zijn ')

for i in reversed(range(5, 7)):  
    print(f'- {tupele[i]}')