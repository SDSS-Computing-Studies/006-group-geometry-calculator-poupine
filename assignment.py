#!python3
# Volume Calculator
# Feel free to rename your variables
import math
def cylinder(r,h):
    # Will calculate the volume for a Cylinder.
    # input parameters: Raidus and height of the Cylinder
    # output parameters: Volume
    # Author: Nolan
    # Modified March 10th, 2021
    v = (math.pi * r**2 * h)
    return v

def sphericalCap(r,h):
    # Will calculate the volume for a Spherical Cap.
    # input parameters: Radius and Height of the object
    # output parameters: Volume
    # Author: Nolan
    # Modified March 10th, 2021
    v = (math.pi * h * (3 * r**2 + h**2)) / 6
    return v

def conicalFrustum(r1,r2,h):
    # Will calculate the volume for a Conical Frustum.
    # input parameters: 3x Radius of the object
    # output parameters: Volume
    # Author: Nolan
    # Modified March 10th, 2021
    v = (1 / 3) * math.pi * h * (r1**2 + r2**2 + (r1 * r2))
    return v 

def Sphere(r):
    # Will calculate the volume for a Sphere.
    # input parameters: Radius of the sphere.
    # output parameters: Volume
    # Author: Nolan
    # Modified March 10th, 2021
    v = math.pi * 3/4 * r**3
    return v

#cubevolume
def Cube(a):
    # Will calculate the volume for a Cube.
    # input parameters: Side length of the cube.
    # output parameters: Volume
    # Author: Liam
    # Modified March 10th, 2021
    x = a * a * a
    return x

#conevolume
def ConeVolume(r,h):
    # Will calculate the volume for a Cone.
    # input parameters: Radius and height of the Cone.
    # output parameters: Volume
    # Author: Liam
    # Modified March 10th, 2021
    print(r, h)
    x = math.pi * (r**2) * (h / 3)
    return x

#pyramidvolume
def pyramid1(l,w,h):
    # Will calculate the volume for a Pyramid.
    # input parameters: Length, width and height of the Pyramid.
    # output parameters: Volume
    # Author: Liam
    # Modified March 10th, 2021
    x = (l * w * h /3)
    return x

#triangularprism
def triangularprism1(a,b,c,h):
    # Will calculate the volume for a Square Prism.
    # input parameters: Base side length and Height of the square prism
    # output parameters: Volume
    # Author: Liam
    # Modified March 10th, 2021
    x = 0.25 * h * math.sqrt( (-a **4) + 2 * ((a * b)**2) + 2 * ((a * c)**2) - (b**4) + 2 * ((b * c)**2) - (c**4)) 
    return x

#squareprism
def squareprism1(a,h):
    # Will calculate the volume for a Square Prism.
    # input parameters: Base side length and Height of the square prism
    # output parameters: Volume
    # Author: Liam
    # Modified March 10th, 2021
    x = ((a**2) * h)
    return x 

#hemisphere
def Hemisphere(r):
    # Will calculate the volume for an Hemisphere.
    # input parameters: Radius of the Hemisphere
    # output parameters: Volume
    # Author: Liam
    # Modified March 10th, 2021
    x = (2/3) * math.pi * (r**3)
    return x

#ellipsoid
def Ellipsoid(a,b,c):
    # Will calculate the volume for an Ellipsoid.
    # input parameters: 3x radius of the Ellipsoid
    # output parameters: Volume
    # Author: Liam
    # Modified March 10th, 2021
    x = (4/3) * math.pi * a * b * c
    return x

#rectangularprism
def rectangularprism(l,w,h):
    # Will calculate the volume for a rectangular prism.
    # input parameters: Length, width and height of the rectangular prism
    # output parameters: Volume
    # Author: Liam
    # Modified March 10th, 2021
    x = l * w * h
    return x

#Circularprism
def Rightsquarepyramid(a,h):
    # Will calculate the volume for a right square pyramid.
    # input parameters: Area and height of the pyramid
    # output parameters: Volume
    # Author: Liam
    # Modified March 10th, 2021
    x = (a**2) * (h/3)
    return x

def title():
    # Will display the title screen to the user.
    # input parameters: None
    # output parameters: None
    # Author: Liam
    # Modified March 10th, 2021
    print("|========================|")
    print("|=== Volume Calulator ===|")
    print("|========================|")
    print("| [Cube]          [Cone] |")
    print("| [Sphere]     [Pyramid] |")
    print("| [Cylinder] [Ellipsoid] |")
    print("|   [Triangular prism]   |")
    print("|     [Square prism]     |")
    print("| [Right square pyramid] |")
    print("|   [Rectangular Prism]  |")
    print("|      [Hemisphere]      |")
    print("|    [Spherical Cap]     |")
    print("|    [Conical Frustum]   |")
    print("\n")
    print("Created by: Poupine")
    return None

def instructions():
    # Will display the instructions to the user.
    # input parameters: None
    # output parameters: None
    # Author: Ethan
    # Modified March 10th, 2021
    print("\n")
    print("- Type in the shape you want to find the volume with. !! (CASE SENSITIVE) !!")
    print("- You will be asked to enter in the parameters of the shape depending on the one you choose.")
    print("- If you want to quit, type \"Quit\" at any point of time when you're not current in an equation.")
    print("\n")
    print("List of shapes: Cube, Cone, Right Rectangular Prism, Cylinder, Sphere, Pyramid, Triangular prism, Square prism, Right square pyramid, Hemisphere, Ellipsoid, Spherical Cap, Conical Frustum")
    return None

def getParams(shape):
    # Will help select the prompts needed for the equations.
    # input parameters: Shape of Object
    # output parameters: Table of prompts
    # Author: Ethan
    # Modified March 10th, 2021
    prompts = []
    if shape == "Cube":
        prompts = ["Enter a side. "]
    elif shape == "Cone":
        prompts = ["Enter the radius. ", "Enter the Height. "]
    elif shape == "Cylinder":
        prompts = ["Enter the radius. ", "Enter the Height. "]
    elif shape == "Sphere":
        prompts = ["Enter the radius. "]
    elif shape == "Pyramid":
        prompts = ["Enter the length. ", "Enter the width. ", "Enter the Height. "]
    elif shape == "Triangular prism":
        prompts = ["Enter a base side. ", "Enter a base side. ", "Enter a base side. ", "Enter the height. "]
    elif shape == "Square prism":
        prompts = ["Enter a base side. ", "Enter the height. "]
    elif shape == "Circular prism":
        prompts = ["Enter the base. ", "Enter the height. "]
    elif shape == "Hemisphere":
        prompts = ["Enter the radius. "]
    elif shape == "Ellipsoid":
        prompts = ["Enter a radius. ", "Enter a radius. ", "Enter a radius. "]
    elif shape == "Spherical Cap":
        prompts = ["Enter a radius. ", "Enter a radius. ", "Enter the height. "]
    elif shape == "Conical Frustum":
        prompts = ["Enter a radius. ", "Enter a radius. ", "Enter the height. "]
    elif shape == "Right Rectangular Prism":
        prompts = ["Enter the length. ", "Enter the width. ", "Enter the height. "]
    elif shape == "Right square pyramid":
        prompts = ["Enter a side. ", "Enter the height. "]
    return prompts

def getInputs(questions):
    # Will generate the chosen questions and prompt the user
    # input parameters: Questions table
    # output parameters: The inputs that the user submitted for each
    # Author: Nolan
    # Modified March 10th, 2021 by Liam
    measurments = []
    for i in range(0,len(questions)):
        measurments.append(float(input(questions[i])))
    return measurments

def main(): 
    # Main function that runs everything
    # input parameters: None
    # output parameters: Final Volume
    # Author: Ethan
    # Modified March 10th, 2021
    quit = False
    while quit == False:
        instructions()
        prompt = ""
        shape = ""
        shape = str(input("Please enter a shape. ")).strip()
        if shape == "Quit":
            quit = True
        else:
            prompt = getParams(shape)
            if prompt == False:
                main()
            else:
                inputs = getInputs(prompt)
                e = 0
                if shape == "Cube":
                    e = Cube(inputs[0])
                elif shape == "Cone":
                    e = ConeVolume(inputs[0], inputs[1])
                elif shape == "Cylinder":
                    e = cylinder(inputs[0], inputs[1])
                elif shape == "Sphere":
                    e = Sphere(inputs[0], inputs[1])
                elif shape == "Pyramid":
                    e = pyramid1(inputs[0], inputs[1], inputs[2])
                elif shape == "Triangular prism":
                    e = triangularprism1(inputs[0], inputs[1], inputs[2], inputs[3])
                elif shape == "Square prism":
                    e = squareprism1(inputs[0], inputs[1])
                elif shape == "Hemisphere":
                    e = Hemisphere(inputs[0])
                elif shape == "Ellipsoid":
                    e = Ellipsoid(inputs[0], inputs[1], inputs[2])
                elif shape == "Spherical Cap":
                    e = sphericalCap(inputs[0], inputs[1], inputs[2])
                elif shape == "Conical Frustum":
                    e = conicalFrustum(inputs[0], inputs[1], inputs[2])
                elif shape == "Right Rectangular Prism":
                    e = rectangularprism(inputs[0], inputs[1], inputs[2])
                elif shape == "Right square pyramid":
                    e = Rightsquarepyramid(inputs[0], inputs[1],)
                if e > 0:
                    print("The volume of the " + str(shape) + " is " + str(e))

    
title()
main()