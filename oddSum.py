def oddSum(x):
    try:
        y = int(x)
    except ValueError:
        return 'not an integer'
    output = 0
    if (y<0):
        return 'not positive'
    for val in range(0,y):
        if((val%3==0) or (val%5==0)):
            output+=val
    return output
output = oddSum(input('Please enter a value for \'X\' that is an integer:'))
print('The calculated output is: ' + str(output))