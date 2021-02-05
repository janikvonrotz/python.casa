print('%s ist %d Jahre alt.' % ('Matthias', 11))
print('1/7 mit drei Nachkommastellen: %.3f' % (1/7))

print('{} ist {} Jahre alt.'.format('Sebastian', 13))
print('{name} ist {alter} Jahre alt.'.format(alter=13, name='Sebastian'))

alter=26/3
name='Sebastian'
print(f'{name} ist {alter:.3} Jahre alt.')