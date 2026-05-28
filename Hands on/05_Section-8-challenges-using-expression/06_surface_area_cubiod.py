# Calculate the surface area of cuboid

# cuboid = 3 dimensional figure with 6 surfaces
# A rectangular figure that is 3d is called as cubiod
# total surface area = finding areas of all the sides
# front_and_back_face_surface_area = 2(length * height)
# top_and_bottom_surface_area = 2(length*breadth)
# lhs_and_rhs_surface_area = 2(breadth*height)
# total_surface_area = front_and_back_face_surface_area + 
#                      top_and_bottom_surface_area + 
#                      lhs_and_rhs_surface_area           

length = int(input('Enter the length of the cubiod:'))                  
breadth = int(input('Enter the breadth of the cubiod:'))
height = int(input('Enter the height of the cubiod:'))

#Calculations
front_and_back_face_surface_area = 2*(length * height)
top_and_bottom_surface_area = 2*(length*breadth)
lhs_and_rhs_surface_area = 2*(breadth*height)

total_surface_area = front_and_back_face_surface_area +top_and_bottom_surface_area +lhs_and_rhs_surface_area
print('The total surface area of a cuboid is:', total_surface_area)