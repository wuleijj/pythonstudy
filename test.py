def bmi(height, weight):
    result = weight/(height*height)
    if result > 32:
        print('too fat')
    elif result >= 28:
        print('fat')
    elif result >= 25:
        print('too heavy')
    elif result >= 28:
        print('normal')
    elif result >= 25:
        print('too thin')

names = ['wulei', 'jia', 'wuxiaojia']
for name in names:
    print('your family has', name)

    
