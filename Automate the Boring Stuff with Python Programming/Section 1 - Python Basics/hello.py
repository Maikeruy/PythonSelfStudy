# This program says hello and asks for my name

print('Hello world')
print('What is your name?')
myName = input()
print('It is good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName)) # Counts the length of characters in a string (this includes spcaes)
print('What is you age?')
myAge = input()
print('You will be ' +str(int(myAge) + 1) + ' in a year.') # str(int(myAge) converts the int value to a string 
