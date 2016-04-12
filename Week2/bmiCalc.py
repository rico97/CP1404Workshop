print('Body-mass-index calculator, by Rico')

weight=float(input('Please enter your weight in kgs:'))
height=float(input('Please enter your height in m:'))

bmi=weight/height**2

print('Therefore your BMI value is:',bmi)
print('Thank you')