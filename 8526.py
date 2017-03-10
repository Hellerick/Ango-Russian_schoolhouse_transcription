NUM = """+---+---+---+---+
! * ! --+-- ! --+
! * +-- ! --+ * !
+---+---+---+---+"""

chars = ' !*+-'
lines = NUM.split('\n')
linelength = len(lines[0])
print(f'Linelength: {linelength}')
print(lines)
for c in chars: print(ord(c))
hex = ''.join(lines)
hex = ''.join(f'{(ord(c)-32):x}' for c in hex)
dec = int(hex, 16)
print(hex)
print(dec)

print('\n'.join([''.join([chr(int(c,16)+32) for c in line]) for line in ['{:x}'.format(5628160376291745434911606949745546426697993755768853346220297602522329689412591067)[i*17:(i+1)*17] for i in range(4)]]))