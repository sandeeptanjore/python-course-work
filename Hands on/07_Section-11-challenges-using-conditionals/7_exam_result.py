print('A program to demonstrate the exam result')

maths = int(input('Enter the marks secured (between 0 and 100) in Maths '))
physics = int(input('Enter the marks secured (between 0 and 100) in Physics '))
chemistry = int(input('Enter the marks secured (between 0 and 100) in Chemistry '))

if (maths >=45 and maths<=100):
    print('You have successfully passed Maths exam')
else:
    print('You have failed your Maths exam')


if (physics >=45 and physics<=100):
    print('You have successfully passed Physics exam')
else:
    print('You have failed your Physics exam')

if (chemistry >=45 and chemistry<=100):
    print('You have successfully passed Chemistry exam')
else:
    print('You have failed your Chemistry exam')

if (maths>=45 and physics >=45 and chemistry>=45) : 
   print('You have successfully passed all the exams')
else:
    print('You have failed in your exams')