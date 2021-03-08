#!python3
# Volume Calculator
# Feel free to rename your variables
import math
pi = math.pi()

def title():
    print("========================")
    print("=== Volume Calulator ===")
    print("========================")
    print("\n")
    print("Created by: Poupine")
    print("\n")
    return None

def instructions():
    print("- Type in the shape you want to find the volume with. !! (CASE SENSITIVE) !!")
    print("- You will be asked to enter in the parameters of the shape depending on the one you choose.")
    print("- If you want to quit, type \"Quit\" at any point of time when you're not current in an equation.")
    print("\n")
    print("List of shapes: Cube, Cone, Cylinder, Sphere, Pyramid, Triangular prism, Square prism, Circular prism, Hemisphere, Ellipsoid, Spherical Cap, Conical Frustum, Ellipsoid Volume")
    return None

def getParams(shape):
    # Will create a list of questions to be asked depending on the shape.
    # These will be asked so that the user can enter in appropriate values
    # input parameter: string 
    # output parameter: return a list containing the prompts for each shape:
    # example: ["Enter the radius:","Enter the slant height:","Enter the height:"]
    prompts

    return prompts

def getInputs(questions):
    # Will prompt the user for inputs for the shape they.
    # These will be asked so that the user can enter in appropriate values
    # It will turn all the input data into a list
    # input parameter: list containing the prompts/questions
    # output parameter: return a list containing all the measurements of the shape
    measurements
    
    return measurements

def main():
    # main block of code that will run your program and control program flow
    # You will need to include a while loop to keep repeating the commands until
    # the user chooses to exit
    title()
    main()

title()
instructions()

def inputCylinderV():
    x = float(input("Enter the radius; "))
    y = float(input("Enter the height: "))
    return x,y

def cylinderV(r,h):
    # r is radius
    # h is height
    v = math.pi() * r**2 * h
    return v

def sphericalCap(r,h):
    v = (pi * h * (3 * r**2 + h**2)) / 6
    return v

def conicalFrustum(r1,r2,h):
    v = (1 / 3) * pi * h * (r1**2 + r2**2 + (r1 * r2))
    return v 