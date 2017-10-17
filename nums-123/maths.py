import math

# learning some basic commands

round(2.1)
math.floor(1.5) # gives us 1
math.ceil(2.1) # gives us 3
math.pi # gets pi
math.e # exponental to a few decimal places

# also has standard trigonometry functions
# however keep in mind that these functions
# take the numbers in radients and not degree

math.sin(math.pi / 2) # we get 1.0 (it returns it as a float)

math.sin(math.pi) # we get almost zero

math.floor(math.sin(math.pi)) # to floor to zero
math.cos(0) # gets us 1.0
math.asin(0) # gets us 0
math.acos(0) # 1.5707 which is pretty accurate

#hypotenuse of a right angled triangle where A and B are the small sides
# and C is the long side we can use the square root of A & B squared

math.hypot(3,4) # 3*3 =9 , 4 * 4 = 16 , 16+9 = 25, square root is 5

math.pow(2,3) # gets 2 to the power of 3 which = (8)
## can also do
2 ** 3 # this returns it as a integer instead of a float

math.exp(2) # find the exponental of a number

math.log(math.e) # gets us 1
math.log10(1000) # = 10
math.log2(8) # = 3 

