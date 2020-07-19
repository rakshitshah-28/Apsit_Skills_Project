import math
def rightAngledTri(a,b):
    ans = math.sqrt(a**2 + b**2)
    print("The hypotenuse of",a,"and",b,"is",ans)
    return ans
def hypotenuse():
    x = input("Enter the first side of right angled triangle:")
    y = input("Enter the second side of right angled triangle:")
    x = float(x)
    y = float(y)
    if (x<=0.0 or y<=0.0):
        print("Enter valid numbers!!")
    #print(type(x))
    else:
        rightAngledTri(x,y)
        print("\nThank you for using HYPOTENUSE Calculator !!")