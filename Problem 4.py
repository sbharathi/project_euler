
#problem 4
# built-in function for flipping str, x = x[::-1]

multiplier1 = 100
multiplier2 = 100
op = 0
product1 = multiplier1*multiplier2

for x in range(900) :
    product1 = multiplier1*multiplier2
    y = str(product1)
    #print (y)
    z = (y[::-1])
    if z == y :
        op = product1
    multiplier1 = multiplier1 + 1
    multiplier2 = multiplier2 + 1
