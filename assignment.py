#!python3
# Volume Calculator
# Feel free to rename your variables
import math
pi = math.pi
def title():
    # Will display a title screen
    # input parameters: none needed
    # output parameters: None
    # Author: Copper
    # Modified:
    # title
    return None

def instructions():
    # Will display instructions
    # input parameters: none needed
    # output parameters: None
    # Author:
    # Modified:
    return None

def main():
    # main block of code that will run your program and control program flow
    # You will need to include a while loop to keep repeating the commands until
    # the user chooses to exit
    title()

main()





























































#cubevolume

def CubeVolume2(a):
    x = (a * a * a)
    return x

#conevolume
def ConeVolume1(r,h):
    #r is raduis
    #h is height
    x = pi * (r**2) * (h / 3)
    return x

#pyramidvolume
def pyramid1(l,w,h):
    x = (l * w * h /3)
    return x

#triangularprism
def triangularprism1(a,b,c,h):
    x = 0.25 * h * math.sqrt( (-a **4) + 2 * ((a * b)**2) + 2 * ((a * c)**2) - (b**4) + 2 * ((b * c)**2) - (c**4)) 
    return x

#squareprism
def squareprism1(a,h):
    x = ((a**2) * h)
    return x 

#cylinder
def Cylinder(r,h):
    x = pi * (r**2) * h
    return x

#hemisphere
def Hemisphere(r):
    x = (2/3) * pi * (r**3)
    return x

#ellipsoid
def Ellipsoid(a,b,c):
    x = (4/3) * pi * a * b * c
    return x

#rectangularprism
def rectangularprism(l,w,h):
    x = l * w * h
    return x