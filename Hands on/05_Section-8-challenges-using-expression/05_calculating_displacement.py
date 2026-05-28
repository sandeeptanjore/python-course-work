# Calculating Displacement (distance) of an object 
# formula = d = (v*v-u*u)2a

initial_velocity = int(input('Enter the initial velocity of the object:'))
final_velocity = int(input('Enter the final velocity of the object:'))
acceleration = int(input('Enter the acceleration of the object:'))

distance = ((final_velocity *final_velocity) - (initial_velocity*initial_velocity))/(2*acceleration)
#distance = (final_velocity *final_velocity - initial_velocity*initial_velocity)/(2*acceleration)

print('The total distance covered by the object is:', distance)