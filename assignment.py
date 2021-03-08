#!python3
# Volume Calculator
# Feel free to rename your variables
import math

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























#me
def CubeVolume1():
    v = float(input("What is Edge"))
    return v

def CubeVolume2(a):
    x = (a * a * a)
    return x

def CubeSurfaceArea1():
    a = float(input("What is Edge"))
    return a 

def CubeSurfacerea2(a):
    x = (a * a * 6)
    return x

def ConeVolume1(r,h):
    #r is raduis
    #h is height
    x = math.pi * (r**2) * (h // 3)
    return x

def ConeVolume2():
    r = float(input("What is radius"))
    h = float(input("What is height"))
    return r,h
