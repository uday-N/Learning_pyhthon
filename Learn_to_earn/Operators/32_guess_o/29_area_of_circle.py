#  write a program to find the area of the circle
# with the formula area = pi*r^2, use pi as 3.14

# logic building
# // step01 //
# Figure out the inputs and outputs
# input > r > datatype > float
# pi = 3.14
# power > ** / power()
# o/p > float - area, print area

# // step02 //
# rough logic, area = 3.14*(r ** 2)

# // step03 //

r = float(input("Enter the radius of the circle:\n"))
area = 3.14*(r ** 2)
print(f"area of circle is : {area}")