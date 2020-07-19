import math
def per_of_triangle():
    a = int(input("Input the side 1 of traingle :"))
    b = int(input("Input the side 2 of traingle :"))
    c = int(input("Input the side 3 of traingle :"))
    perimeter = a+b+c
    print("Perimeter of Triangle = ",perimeter)

def per_of_circle():
    r = int(input("Input the Radius of Cirlce :"))
    P = math.pi
    perimeter = 2*P*r 
    print("Circumference of Circle is :",perimeter)

def per_of_square():
    s = int(input("Input the side of square :"))
    perimeter = 4*s
    print("perimeter of square is =",perimeter)

def per_of_rectangle():
    l = int(input("Input the length of rectangle:"))
    b = int(input("Input the breadth of rectangle:"))    
    perimeter = l+l+b+b
    print("Perimeter of rectangle is =",perimeter)

def Perimeter():
    Flag = True
    while Flag:
    # Take input from the user
            print("1. Perimeter of triangle")
            print("2. Circumference of circle")
            print("3. Perimeter of square")
            print("4. Perimeter of rectangle")
            print("5. BACK")
            choice = int(input("Enter choice(1/2/3/4/5): "))
            if choice > 6:
                print("please input the correct value!!!")
                continue
        # Check if choice is one of the four options
            if choice == 1:
                per_of_triangle()
            elif choice == 2:
                per_of_circle()
            elif choice == 3:
                per_of_square()
            elif choice == 4:
                per_of_rectangle()
                break
            elif choice == 5:
               print("Thank you for using Perimeter Calculator !!")
               break
            else:
                print("invalid input")             

