import math
def area_of_triangle():
    b = int(input("Input the base : "))
    h = int(input("Input the height : "))
    area = b*h/2
    print("area = ", area)

def area_of_circle():
    r = int(input("Input the radius of the cricle:"))
    P = math.pi
    area = P*r*r
    print("area of circle = ",area)
    

def area_of_square():
    s = int(input("Input the side of square:"))
    area = s*s
    print("area of square = ",area)
    

def area_of_rectangle():
    l = int(input("Input the length of rectangle:"))
    b = int(input("Input the breadth of rectangle:"))
    area = l*b
    print("area of rectangle = ",area)

def Area():
    Flag = True
    while Flag:
        # Take input from the user
            print("1. Area of triangle")
            print("2. Area of circle")
            print("3. Area of square")
            print("4. Area of rectangle")
            print("5. BACK")
            choice = int(input("Enter choice(1/2/3/4/5): "))
            if choice > 6:
                continue
        # Check if choice is one of the four options
            if choice == 1:
                area_of_triangle()
                
            elif choice == 2:
                area_of_circle()
            elif choice == 3:
                area_of_square()
            elif choice == 4:
                area_of_rectangle()
                break
            elif choice == 5:
                print("Thank you for using Area Calculator !!")
                break
            else:
                print("invalid input")

            

