#BMI-1
height=int(input())
weight=int(input())
a=(height*height)
bmi=(weight/a)
print(bmi)

#simpleintrest
p=float(input(""))
t=int(input(""))
r=float(input(""))
simple_interest=(p*t*r)/100
print(simple_interest)

#areaofcircle
from math import pi
r = float(input())
area = pi * r ** 2
print(str(area))

#acceleration using distance and time:
time=float(input())
distance=float(input())
acc=((2 * distance) / (time ** 2))
print(f"The acceleration is: {acc:.2f} m/s^2")

#velocity using mass and force
m = float(input())
f = float(input())
t = float(input())
v1 = float(input())
acc = f/ m
v = v1+ acc* t
print(v)

#star pyramid
rows = int(input(""))
k = 0
for i in range(1, rows+1):
    for space in range(1, (rows-i)+1):
        print(end="  ")
    while k!=(2*i-1):
        print("* ", end="")
        k += 1
    k = 0
    print()


#convert kms to miles
km = float(input(""))
cf = 0.621371
miles = km * cf
print('%0.2f kilometers is equal to %0.2f miles' %(km,miles))

#programme to find joules
force=float(input())
distance=float(input())
energy=(force*distance)
print(energy)

#eulers distance formula
import math

def euler_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    x1 = float(input("Enter the x-coordinate of the first point: "))
    y1 = float(input("Enter the y-coordinate of the first point: "))
    x2 = float(input(""))
    y2 = float(input(""))
    distance = euler_distance(x1, y1, x2, y2)
    print(f"The distance between the two points is: {distance:.2f}")

