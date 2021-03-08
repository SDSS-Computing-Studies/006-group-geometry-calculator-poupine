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
    print("List of shapes: Cube, Cone, Right Rectangular Prism, Cylinder, Sphere, Pyramid, Triangular prism, Square prism, Circular prism, Hemisphere, Ellipsoid, Spherical Cap, Conical Frustum")
    return None

def getParams(shape):
    prompts

    if shape == "Cube":
        prompts = {"Enter a side. "}
    elif shape == "Cone":
        prompts = {"Enter the radius. ", "Enter the Height. "}
    elif shape == "Cylinder":
        prompts = {"Enter the radius. ", "Enter the Height. "}
    elif shape == "Sphere":
        prompts = {"Enter the radius. "}
    elif shape == "Pyramid":
        prompts = {"Enter the length. ", "Enter the width. ", "Enter the Height. "}
    elif shape == "Triangular prism":
        prompts = {"Enter a base side. ", "Enter a base side. ", "Enter a base side. ", "Enter the height. "}
    elif shape == "Square prism":
        prompts = {"Enter a base side. ", "Enter the height. "}
    elif shape == "Circular prism":
        prompts = {"Enter the base. ", "Enter the height. "}
    elif shape == "Hemisphere":
        prompts = {"Enter the radius. "}
    elif shape == "Ellipsoid":
        prompts = {"Enter a radius. ", "Enter a radius. ", "Enter a radius. "}
    elif shape == "Spherical Cap":
        prompts = {"Enter a radius. ", "Enter a radius. ", "Enter the height. "}
    elif shape == "Conical Frustum":
        prompts = {"Enter a radius. ", "Enter a radius. ", "Enter the height. "}
    elif shape == "Right Rectangular Prism":
        prompts = {"Enter the length. ", "Enter the width. ", "Enter the height. "}

    return prompts

def getInputs(questions):

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

def inputSphere(r):
    v = math.pi() * 3/4 * r**3
    return v
