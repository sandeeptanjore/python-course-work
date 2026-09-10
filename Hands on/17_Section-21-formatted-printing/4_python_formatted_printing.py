name = 'Raj'
roll = 25
avg = 5.9

print('{0}====={1}===={2}'.format(name,roll,avg))

#print('{} '.format(data))

item='Memory'
size = 32
price= 11.75
print('{0}GB {1} in ${2}'.format(size,item,price))

print('{1}GB {2} in ${0}'.format(price,size,item))

print('{0} of {1}GB for ${2}'. format(item,size,price))

data = 100
print('start {0:15} end'.format(data))

print('start {0:<15} end'.format(data))

print('start {0:^15} end'.format(data))

data1 =123456789
print('start {0:^15,} end'.format(data1))
print('start {0:^15%} end'.format(data1))
print('start {0:^15_} end'.format(data1))

data2= 123.123456789
print('start {0:^15.2f} end'.format(data2))
print('start {0:^15.3f} end'.format(data2))
print('start {0:^15.1f} end'.format(data2))
print(' ')

# easy method of doing the same thing from the above
print(f'{size}GB {item:^6} in ${price}')

quantity = 5
price = 11.7534

print(f'Total: ${quantity * price:.2f}')

