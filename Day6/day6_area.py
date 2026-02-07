def calc_rectangle(length, width):
    area=length * width
    perimeter=2*(length + width)
    return area, perimeter
length = float(input("Enter the length of the rectangle: "))
width= float(input("Enter the width of the rectangle: "))
calculated=calc_rectangle(length, width)
print("The area of triangle is:",calculated[0])
print("The perimeter of triangle is:",calculated[1])