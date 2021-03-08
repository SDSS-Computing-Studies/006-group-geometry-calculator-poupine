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
    else:
        return False

    return prompts

def getInputs(questions):

    measurements
    
    return measurements

def main():
    title()
    instructions()
    prompt
    shape
    shape = str(input("Please enter a shape."))
    prompt = getParams(shape)
    if prompt == False:
        main()
    else:
        getInputs(shape)

        

def inputCylinderV():
    x = float(input("Enter the radius; "))
    y = float(input("Enter the height: "))
    return x,y

def cylinder2(r,h):
    # r is radius
    # h is height
    v = math.pi() * r**2 * h
    return v

def inputSphere(r):
    v = math.pi() * 3/4 * r**3
    return v
