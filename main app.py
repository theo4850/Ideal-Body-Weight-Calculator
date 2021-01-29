import math

print('Diclaimer: The program is not made from doctors so the results might be wrong.', '\n',
'If you want accurate results, you should see a doctor.')

sex = input('Please enter your sex(man or woman): ')
age = int(input('Please enter your age: '))
height = float(input('Please enter your height(m), (eg. 1.70): '))
actual_weight = float(input('Please enter you actual weight(kg): '))
if age < 18:
    bmi = int(input('Please enter your body mass index: '))

def checking_body_weight(x, y, z, a):
    if x == 'man':
        ibd = 50 + 2.3 * z
        nbd = ibd + (0.25 * (a - ibd))
    elif x == 'woman':
        ibd = 45.5 + 2.3 * z
        nbd = ibd + (0.25 * (a - ibd))
    return ibd, nbd

def children_ideal_body_weight(x, y):
    ideal_body_weight = x * 0.5 * (y)^2
    return ideal_body_weight

def lose_add_weight(ib, nb):
    if ib > actual_weight and nb > actual_weight:
        print('You should add weight.')
    elif ib == actual_weight and nb > actual_weight:
        print('You have the ideal body weight but you need to add weight to have the nutrition body weight')
    elif ib < actual_weight and nb > actual_weight:
        print('You need to add some more weight to have the nutrition weight.')
    elif nb == actual_weight:
        print('You have the perfect body weight for you.')
    elif nb < actual_weight:
        print('You need to lose some weight.')

while True:
    select = input('Press Enter or 'q' for exit: ')

    if select == 'q':
        Break;

    if age >= 18:
        b, c = checking_body_weight(sex, age, height, actual_weight)
        print('Your ideal body weight is ', b, 'and your nutrition body weight is ', c, '\n')
        abc = lose_add_weight(b, c)
    elif age < 18:
        d = children_ideal_body_weight(bmi, height)
        print('your ideal body weight is ', d)

print('End of program!', '\n', 'Thank you for using our program!')
