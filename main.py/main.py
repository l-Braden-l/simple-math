#Braden Leach
#Sep 25 2024
#simple math

#practice 1 


#the actual number
num1 = 3
num2 = 4
#calculations
sum = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2
remainder =num1 % num2
#display
print(f'{num1} plus {num2} = {sum} ')
print(f'{num1} minus {num2} = {difference} ')
print(f'{num1} times {num2} = {product} ')
print(f'{num1} divided by {num2} = {quotient} ')
print(f'{num1} remainder {num2} = {remainder} ')



#practice 2


#input
length = float(input('enter the length of a rectangular room (in feet):\n'))
width =float(input('enter the width of a rectangular room (in feet):\n'))
#math
area = length * width
#display
print(f'the area of your room is {area} feet squared')



#practice 3 


#part 1 
name ='Braden'
age = 17
fav_color = 'Blue'
message = 'My name is {0} and I am {1} years old. {2} is my favorite color'.format(name,age,fav_color)
print(message)
#part 2 
burger = float(input('put the amount a burger would cost:\n'))
fries = float(input('put the amount fries would cost:\n'))
coke = float(input('put the amount a coke would cost:\n'))

price = coke + fries + burger *1.06
sales_tax = price * 0.026
print(f'The total amount of tax from the three items is ${sales_tax:.2f}. As well as the total price is ${price:.2f}')
#part 3
fri_name = 'Dakota'
school = 'buckley'
message = 'My friend {0} goes to the same school as me, Which is {1}'.format(fri_name,school)
print(message)