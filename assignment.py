#!python3
# Volume Calculator
# Feel free to rename your variables
import math

def cylinder(r,h):
    # r is radius
    # h is height
    v = math.pi() * r**2 * h
    return v

def sphericalCap(r,h):
    v = (math.pi() * h * (3 * r**2 + h**2)) / 6
    return v

def conicalFrustum(r1,r2,h):
    v = (1 / 3) * math.pi() * h * (r1**2 + r2**2 + (r1 * r2))
    return v 

def Sphere(r):
    v = math.pi() * 3/4 * r**3
    return v

#cubevolume
def Cube(a):
    x = (a * a * a)
    return x

#conevolume
def ConeVolume(r,h):
    #r is raduis
    #h is height
    x = math.pi() * (r**2) * (h / 3)
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
    x = math.pi() * (r**2) * h
    return x

#hemisphere
def Hemisphere(r):
    x = (2/3) * math.pi() * (r**3)
    return x

#ellipsoid
def Ellipsoid(a,b,c):
    x = (4/3) * math.pi() * a * b * c
    return x

#rectangularprism
def rectangularprism(l,w,h):
    x = l * w * h
    return x

def title():
    print("|========================|")
    print("|=== Volume Calulator ===|")
    print("|========================|")
    print("| [Cube]          [Cone] |")
    print("| [Sphere]     [Pyramid] |")
    print("| [Cylinder] [Ellipsoid] |")
    print("|   [Triangular prism]   |")
    print("|     [Square prism]     |")
    print("|    [Circular prism]    |")
    print("|   [Rectangular Prism]  |")
    print("|      [Hemisphere]      |")
    print("|    [Spherical Cap]     |")
    print("|    [Conical Frustum]   |")
    print("\n")
    print("Created by: Poupine")
    return None

def instructions():
    print("\n")
    print("- Type in the shape you want to find the volume with. !! (CASE SENSITIVE) !!")
    print("- You will be asked to enter in the parameters of the shape depending on the one you choose.")
    print("- If you want to quit, type \"Quit\" at any point of time when you're not current in an equation.")
    print("\n")
    print("List of shapes: Cube, Cone, Right Rectangular Prism, Cylinder, Sphere, Pyramid, Triangular prism, Square prism, Circular prism, Hemisphere, Ellipsoid, Spherical Cap, Conical Frustum")
    return None

def getParams(shape):
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
    return prompts

def getInputs(questions):
    measurments = [0]
    for i in range(0,len(questions)):
        measurments.append(float(input(questions[i])))
    return measurments

def main(): 
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
                    e = Cube(inputs)
                elif shape == "Cone":
                    e = ConeVolume(inputs)
                elif shape == "Cylinder":
                    e = cylinder(inputs)
                elif shape == "Sphere":
                    e = Sphere(inputs)
                elif shape == "Pyramid":
                    e = pyramid1(inputs)
                elif shape == "Triangular prism":
                    e = triangularprism1(inputs)
                elif shape == "Square prism":
                    e = squareprism1(inputs)
                elif shape == "Circular prism":
                    e = Cylinder(inputs)
                elif shape == "Hemisphere":
                    e = Hemisphere(inputs)
                elif shape == "Ellipsoid":
                    e = Ellipsoid(inputs)
                elif shape == "Spherical Cap":
                    e = sphericalCap(inputs)
                elif shape == "Conical Frustum":
                    e = conicalFrustum(inputs)
                elif shape == "Right Rectangular Prism":
                    e = rectangularprism(inputs)
                print(e)

    
title()
main()

