# This program says hello and asks for my name.

# print('Hello, world!')
# print('What is your name?')    # ask for their name
# myName = input()
# print('It is good to meet you, ' + myName)
# print('The length of your name is:')
# print(len(myName))
# print('What is your age?')    # ask for their age
# myAge = input()
# print('You will be ' + str(int(myAge) + 1) + ' in a year.')
# print(int(99.99))

# name = input("what is your name:")
# age = int(input("How old are you?: "))
# if name == 'Alice':
#     print('Hi, Alice.')
# elif age < 12:
#     print('You are not Alice, kiddo.')
# elif age > 2000:
#     print('Unlike you, Alice is not an undead, immortal vampire.')
# elif age > 100:
#     print('You are not Alice, grannie.')
# spam = 0
# while spam < 5:
#     print('hi', spam, '')
#     spam += 1
# name = ''
# while name != 'your name':
#     print('Please type your name.')
#     name = input()
#     if name == 'your name':
#         break
# print('Thank you!')

# name = ''
# while True:
#     print('Who are you?')
#     name = input()
#     if name != 'Joe':
#         continue
#     print('hello Joe! What is your password? it is a fish')
#     password = input()
#     if password == 'swordfish':
#         break
# print('acces granted.')

total = 0
for num in range(101):
    total = total + num
print(total)
