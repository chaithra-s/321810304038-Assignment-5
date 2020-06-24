# area of circlr using math function
import math
r=float(input("Enter yhe radius of the circle:"))
area=math.pi*r*r
print("%.2f" %area)

#area of regular polygon using math function
from math import tan,pi
n_sides=int(input("Input number of sides:"))
s_length=float(input("Input the length of a side:"))
p_area=n_sides*(s_length**2)/(4*tan(pi/n_sides))
print("The area of the polygon is:",p_area)

#area of segment of a circle
r=int(input ("enter a radius"))
from math import pi
x=float(input("angle"))
area=(pi*r**2)*(x/360)
print("area of segment of circle",area)


#shuffle the list
import random
test_list=[100,1,2,3,30,40,"hai","hello"]
print("The original lust is:"+ str(test_list))
random.shuffle(test_list)
print("The shuffled list is:"+str(test_list))

#generating random numbers
import random
rnum=random.randrange(1,10000,50)
print("Random integer:",rnum)

#program using math module
import math
print(math.sin(math.pi/3))
print(math.cos(math.pi))
print(math.tan(math.pi/2))
print(math.sin(0.8660254037844386))
print(math.pow(5,8))
print(math.sqrt(400))
print(math.exp(5))
print(math.log2(1024))
print(math.log10(1024))
print(math.floor(23.56).math.ceil(23.56))