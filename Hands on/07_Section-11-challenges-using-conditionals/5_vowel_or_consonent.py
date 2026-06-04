print('A program to demonstrate if the alphabet entered is a vowel or a consonent')

vowel = {'a','e','i','o','u'}
enter_alphabet = input('Enter an alphabet of your choice ')

if(enter_alphabet in vowel):
    print('The alphabet entered is a vowel')
else:
    print('It is a consonent')
